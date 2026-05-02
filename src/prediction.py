import os                               # Importujemy moduł os, który pozwala na interakcję z systemem plików, np. do sprawdzania istnienia plików czy tworzenia ścieżek
import pandas as pd                     # Importujemy bibliotekę pandas, która jest używana do manipulacji danymi i tworzenia DataFrame'ów, co ułatwia pracę z danymi tabelarycznymi
import numpy as np                      # Importujemy bibliotekę numpy, która jest używana do operacji na tablicach i macierzach, co jest przydatne do obliczeń numerycznych
from datetime import timedelta          # Importujemy datetime i timedelta, które są używane do operacji na datach i czasie, np. do obliczania różnic między datami

# Piotr Bacior - 15 722 - 2026 - Python - MH


# Definiuję funkcję predict_goal_date, która wykorzystuje algorytm regresji liniowej do przewidywania daty osiągnięcia celu wagowego na podstawie danych historycznych zapisanych w pliku CSV. Dane wejściowe to nazwa pliku CSV oraz docelowa waga, a wynik to przewidywana data osiągnięcia tej wagi w formacie string.
def predict_goal_date(csv_filename: str, target_weight: float) -> str : 

    """
    Algorytm Machine Learning (Regresja Liniowa) przewidujący datę osiągnięcia celu wagowego.
    """

    # Sprawdzamy, czy plik CSV z danymi historycznymi istnieje. Jeśli nie, zwracamy komunikat o braku danych.
    if not os.path.exists(csv_filename) : 

        # Jeśli plik nie istnieje, zwracamy komunikat o braku danych historycznych, co oznacza, że nie możemy przewidzieć daty osiągnięcia celu wagowego
        return "Brak danych historycznych. Nie można przewidzieć daty osiągnięcia celu wagowego."
    
    
    # Jeśli plik istnieje, wczytujemy dane z pliku CSV do DataFrame'a za pomocą biblioteki pandas, co pozwala nam na łatwą manipulację danymi i przygotowanie ich do analizy
    try : 

        # Wczytujemy dane z pliku CSV, zakładając, że wartości są oddzielone średnikami
        df = pd.read_csv(csv_filename, sep=';') 

        # Jeżeli DataFrame jest pusty lub zawiera mniej niż 2 wiersze, zwracamy komunikat o niewystarczającej ilości danych, ponieważ regresja liniowa wymaga co najmniej dwóch punktów danych do obliczenia linii trendu
        if df.empty or len(df) < 2 :

            # Jeśli dane są niewystarczające, zwracamy komunikat o potrzebie co najmniej 2 wpisów, aby móc przewidzieć datę osiągnięcia celu wagowego
            return "Niewystarczająca ilość danych historycznych. Potrzebne są co najmniej 2 wpisy, aby przewidzieć datę osiągnięcia celu wagowego."
        
        # Konwertujemy kolumnę 'Data i czas' na format daty i czasu, co pozwala nam na wykonywanie operacji na datach, takich jak obliczanie różnic między datami czy konwersja do formatu numerycznego dla regresji liniowej
        df['Data i czas'] = pd.to_datetime(df['Data i czas'])

        # Sortujemy dane według kolumny 'Data i czas', co jest ważne, aby mieć chronologiczny porządek danych, co jest kluczowe dla analizy trendów i przewidywania przyszłych wartości na podstawie danych historycznych
        df = df.sort_values('Data i czas')

        # Pobieramy pierwszą datę z kolumny 'Data i czas', co jest potrzebne do obliczenia liczby dni od tej daty do każdej kolejnej daty, co jest kluczowe dla regresji liniowej, która będzie używać tych wartości jako zmiennej niezależnej (X) do przewidywania wagi (Y)
        first_date = df['Data i czas'].min()  

        # Tworzymy nową kolumnę 'Days', która zawiera liczbę dni od pierwszej daty do każdej daty w kolumnie 'Data i czas', co pozwala nam na przekształcenie danych czasowych na format numeryczny, który jest wymagany do przeprowadzenia regresji liniowej
        df['Days'] = (df['Data i czas'] - first_date).dt.days


        # Pomiary muszą pochodzić z przynajmniej dwóch różnych dni

        # Jeśli wszystkie pomiary pochodzą z tego samego dnia, to nie możemy przeprowadzić regresji liniowej, ponieważ nie mamy zmiennej niezależnej (X) o różnych wartościach, co jest konieczne do obliczenia linii trendu i przewidywania przyszłych wartości na podstawie danych historycznych
        if df['Days'].nunique() < 2 :

            # Jeśli wszystkie pomiary pochodzą z tego samego dnia, zwracamy komunikat o potrzebie pomiarów z przynajmniej dwóch różnych dni, aby móc przeprowadzić regresję liniową i przewidzieć datę osiągnięcia celu wagowego
            return "Wszystkie pomiary pochodzą z tego samego dnia. Potrzebne są pomiary z przynajmniej dwóch różnych dni, aby przeprowadzić regresję liniową i przewidzieć datę osiągnięcia celu wagowego."
        

        # -- Regresja liniowa - Machine Learning --

        # y = a*x + b (a -> slope (nachylenie), b -> intercept (punkt przecięcia))

        # Obliczamy współczynnik kierunkowy (slope) i punkt przecięcia (intercept) linii regresji liniowej za pomocą funkcji polyfit z biblioteki numpy, która dopasowuje linię do danych, gdzie 'Days' jest zmienną niezależną (X), a 'Waga (kg)' jest zmienną zależną (Y). Współczynnik kierunkowy (slope) wskazuje, jak szybko waga zmienia się w czasie, a punkt przecięcia (intercept) wskazuje wartość wagi, gdy liczba dni wynosi zero (czyli na początku pomiarów).
        slope, intercept = np.polyfit(df['Days'], df['Waga (kg)'], 1)

        # Obliczamy liczbę dni potrzebną do osiągnięcia docelowej wagi (target_weight) na podstawie równania linii regresji, gdzie target_weight jest wartością Y, a Days jest wartością X. Obliczamy to, przekształcając równanie linii regresji do postaci Days = (target_weight - intercept) / slope, co pozwala nam na przewidzenie, ile dni zajmie osiągnięcie docelowej wagi na podstawie trendu z danych historycznych.
        current_weight = df['Waga (kg)'].iloc[-1]


        # Jeżeli jesteśmy już bardzo blisko celu - obsługa przypadku, gdy aktualna waga jest równa lub mniejsza niż docelowa waga, co oznacza, że cel wagowy został już osiągnięty lub przekroczony, więc nie ma potrzeby przewidywania daty osiągnięcia celu, ponieważ jest on już osiągnięty
        if abs(current_weight - target_weight) <= 0.5 : 

            # Jeżeli aktualna waga jest równa lub mniejsza niż docelowa waga, zwracamy gratulacje, ponieważ cel wagowy został już osiągnięty, co oznacza, że użytkownik osiągnął swój cel i nie ma potrzeby dalszych przewidywań
            return "Gratulacje! Twój cel wagowy został już osiągnięty!"
        

        # Sprawdzamy czy idziemy w dobrym kierunku 

        # Jeżeli chcemy schudnąć (target_weight < current_weight) i nachylenie jest dodatnie, to oznacza, że waga rośnie, co jest sprzeczne z celem, więc zwracamy komunikat o potrzebie zmiany podejścia, ponieważ obecny trend wskazuje na wzrost wagi, co jest sprzeczne z celem schudnięcia
        if (slope > 0 and target_weight < current_weight) or (slope < 0 and target_weight > current_weight) :

            # Jeżeli chcemy schudnąć, a nachylenie jest dodatnie, lub jeżeli chcemy przytyć, a nachylenie jest ujemne, zwracamy komunikat o oddalaniu się od celu, co oznacza, że obecny trend wagi wskazuje na kierunek przeciwny do celu, więc zalecamy skorygowanie diety lub podejścia do osiągnięcia celu wagowego
            return "Twój obecny trend wagi oddala Cię od celu. Skoryguj dietę!"
        
        # Jeżeli nachylenie jest równe zero, to oznacza, że waga się nie zmienia, co jest sprzeczne z celem, więc zwracamy komunikat o braku postępów, ponieważ obecny trend wskazuje na brak zmian w wadze, co jest sprzeczne z celem osiągnięcia określonej wagi
        if slope == 0 :