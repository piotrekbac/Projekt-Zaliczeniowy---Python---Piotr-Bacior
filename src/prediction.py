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
        return "Brak danych do analizy. Nie można przewidzieć daty osiągnięcia celu wagowego."    
    
    # Jeśli plik istnieje, wczytujemy dane z pliku CSV do DataFrame'a za pomocą biblioteki pandas, co pozwala nam na łatwą manipulację danymi i przygotowanie ich do analizy
    try : 

        # Wczytujemy dane z pliku CSV, zakładając, że wartości są oddzielone średnikami
        df = pd.read_csv(csv_filename, sep=';') 

        # Jeżeli DataFrame jest pusty, zwracamy komunikat o braku danych historycznych, co oznacza, że nie możemy przewidzieć daty osiągnięcia celu wagowego
        return _calculate_trend(df, target_weight, 'Data i czas', 'Waga (kg)')

    # Obsługa wszelkich nieoczekiwanych błędów, które mogą wystąpić podczas wczytywania danych, przetwarzania danych lub obliczeń regresji liniowej. Jeśli wystąpi jakikolwiek błąd, zwracamy komunikat o błędzie, co pozwala użytkownikowi na zrozumienie, że coś poszło nie tak i może potrzebować sprawdzić dane wejściowe lub skonsultować się z pomocą techniczną.
    except Exception as e :

        # Zwracamy komunikat o błędzie wraz z informacją o tym, co poszło nie tak, co pozwala użytkownikowi na zrozumienie, że coś poszło nie tak i może potrzebować sprawdzić dane wejściowe lub skonsultować się z pomocą techniczną
        return f"Błąd algorytmu: {e}"
    

# Funkcja pomocnicza do obliczania trendu i przewidywania daty osiągnięcia celu wagowego na podstawie danych historycznych
def predict_goal_from_sql(csv_filename: str, target_weight: float) -> str :

    """ Algorytm podpięty pod bazę danych SQL (używany w aplikacji Webowej) """

    # Sprawdzamy, czy DataFrame jest pusty, co oznacza brak danych historycznych. Jeśli jest pusty, zwracamy komunikat o braku danych historycznych, co oznacza, że nie możemy przewidzieć daty osiągnięcia celu wagowego
    if df.empty :

        # Jeśli DataFrame jest pusty, zwracamy komunikat o braku danych historycznych, co oznacza, że nie możemy przewidzieć daty osiągnięcia celu wagowego
        return "Brak historii w bazie SQL."
        
    # Jeśli DataFrame nie jest pusty, obliczamy trend i przewidujemy datę osiągnięcia celu wagowego, korzystając z funkcji _calculate_trend, która wykonuje regresję liniową na podstawie danych historycznych
    try :

        # Obliczamy trend i przewidujemy datę osiągnięcia celu wagowego, korzystając z funkcji _calculate_trend, która wykonuje regresję liniową na podstawie danych historycznych
        df = pd.read_csv(csv_filename, sep=';')  

        # Obliczamy trend i przewidujemy datę osiągnięcia celu wagowego, korzystając z funkcji _calculate_trend, która wykonuje regresję liniową na podstawie danych historycznych
        return _calculate_trend(df, target_weight, 'Data i czas', 'Waga (kg)')
        
    # Obsługa wszelkich nieoczekiwanych błędów, które mogą wystąpić podczas wczytywania danych, przetwarzania danych lub obliczeń regresji liniowej. Jeśli wystąpi jakikolwiek błąd, zwracamy komunikat o błędzie, co pozwala użytkownikowi na zrozumienie, że coś poszło nie tak i może potrzebować sprawdzić dane wejściowe lub skonsultować się z pomocą techniczną.
    except Exception as e :

        # Zwracamy komunikat o błędzie wraz z informacją o tym, co poszło nie tak, co pozwala użytkownikowi na zrozumienie, że coś poszło nie tak i może potrzebować sprawdzić dane wejściowe lub skonsultować się z pomocą techniczną
        return f"Błąd algorytmu: {e}"
        

# Funkcja pomocnicza do obliczania trendu i przewidywania daty osiągnięcia celu wagowego na podstawie danych historycznych, która wykonuje regresję liniową na podstawie danych historycznych i zwraca przewidywaną datę osiągnięcia celu wagowego w formacie string
def _calculate_trend(df: pd.DataFrame, target_weight: float, date_col: str, weight_col: str) -> str :

    """ Oblicza trend i przewiduje datę osiągnięcia celu wagowego na podstawie danych historycznych. """

    # Sprawdzamy, czy DataFrame zawiera wystarczającą ilość danych do przeprowadzenia analizy. Jeśli jest mniej niż 2 wiersze, zwracamy komunikat o braku wystarczających danych historycznych, co oznacza, że nie możemy przewidzieć daty osiągnięcia celu wagowego
    if len(df) < 2 :

        # Jeśli jest mniej niż 2 wiersze, zwracamy komunikat o braku wystarczających danych historycznych, co oznacza, że nie możemy przewidzieć daty osiągnięcia celu wagowego
        return "Potrzebujesz minimum 2 pomiarów w historii, aby wyliczyć trend"
        
    # Konwertujemy kolumnę z datami na format datetime, co pozwala nam na łatwe obliczenia związane z czasem
    df[date_col] = pd.to_datetime(df[date_col])  

    # Sortujemy dane według daty, co jest ważne dla analizy trendu    
    df = df.sort_values(by=date_col)

    # Wybieramy pierwszą datę z danych, co jest potrzebne do obliczenia różnic czasowych w regresji liniowej
    first_date = df[date_col].min()

    # Obliczamy liczbę dni od pierwszej daty dla każdego pomiaru, co jest potrzebne do regresji liniowej
    df['Days'] = (df[date_col] - first_date).dt.days  


    # Sprawdzamy, czy mamy wystarczającą ilość unikalnych dni do przeprowadzenia regresji liniowej. Jeśli jest mniej niż 2 unikalne dni, zwracamy komunikat o braku wystarczających danych historycznych, co oznacza, że nie możemy przewidzieć daty osiągnięcia celu wagowego
    if df['Days'].nunique() < 2 :

        # Jeśli jest mniej niż 2 unikalne dni, zwracamy komunikat o braku wystarczających danych historycznych, co oznacza, że nie możemy przewidzieć daty osiągnięcia celu wagowego
        return "Potrzebujesz minimum 2 pomiarów w historii, aby wyliczyć trend"
        
        
    # Obliczamy współczynnik kierunkowy (slope) i punkt przecięcia (intercept) dla regresji liniowej
    slope, intercept = np.polyfit(df['Days'], df[weight_col], 1)  

    # Pobieramy aktualną wagę z ostatniego pomiaru
    current_weight = df[weight_col].iloc[-1]  


    # Jeżeli aktualna waga jest już bliska docelowej wadze (różnica mniejsza niż 0.5 kg), zwracamy komunikat, że cel jest już blisko osiągnięty, co oznacza, że użytkownik jest już blisko osiągnięcia swojego celu wagowego i może nie potrzebować dalszych przewidywań
    if abs(current_weight - target_weight) < 0.5 :

        # Zwracamy komunikat, że cel jest już blisko osiągnięty, co oznacza, że użytkownik jest już blisko osiągnięcia swojego celu wagowego i może nie potrzebować dalszych przewidywań
        return "Twój cel jest już blisko osiągnięcia!"


    # Sprawdzamy, czy trend jest zgodny z kierunkiem osiągnięcia celu wagowego. Jeśli trend jest pozytywny (slope > 0) i docelowa waga jest mniejsza niż aktualna waga, lub jeśli trend jest negatywny (slope < 0) i docelowa waga jest większa niż aktualna waga, oznacza to, że użytkownik zmierza w kierunku osiągnięcia celu wagowego. W takim przypadku obliczamy przewidywaną datę osiągnięcia celu wagowego na podstawie regresji liniowej i zwracamy tę datę w formacie string.
    if (slope > 0 and target_weight < current_weight) or (slope < 0 and target_weight > current_weight) :

        # Zwracamy odpowiedni komunikat 
        return "Twój obecny trend wagi oddala Cie od celu. Skortyguj dietę!"
        

    # Jeśli trend jest zgodny z kierunkiem osiągnięcia celu wagowego, obliczamy przewidywaną datę osiągnięcia celu wagowego na podstawie regresji liniowej i zwracamy tę datę w formacie string.
    if slope == 0 :

        # Jeśli trend jest płaski (slope == 0), oznacza to, że waga stoi w miejscu i nie zmienia się w kierunku osiągnięcia celu wagowego. W takim przypadku zwracamy komunikat, że waga od dłuższego czasu stoi w miejscu, co oznacza, że użytkownik nie robi postępów w kierunku osiągnięcia swojego celu wagowego i może potrzebować zmienić swoją strategię, aby zacząć robić postępy.
        return "Twoja waga od dłuższego czasu stoi w miejscu"
        
    # Obliczamy liczbę dni potrzebną do osiągnięcia celu wagowego na podstawie regresji liniowej
    target_days = (target_weight - intercept) / slope  

    # Obliczamy liczbę dni pozostałych do osiągnięcia celu wagowego, odejmując aktualną liczbę dni od liczby dni potrzebnych do osiągnięcia celu wagowego
    days_reaming = int(target_days - df['Days'].iloc[-1])  


    # Sprawdzamy, czy liczba dni pozostałych do osiągnięcia celu wagowego jest ujemna, co oznacza, że według trendu użytkownik powinien już osiągnąć swój cel wagowy. Jeśli jest ujemna, zwracamy komunikat, że według trendu użytkownik powinien już osiągnąć swój cel wagowy, co oznacza, że użytkownik jest już za późno na osiągnięcie swojego celu wagowego i może potrzebować zmienić swoją strategię, aby zacząć robić postępy.
    if days_reaming < 0 :

        # Jeśli liczba dni pozostałych do osiągnięcia celu wagowego jest ujemna, zwracamy komunikat, że według trendu użytkownik powinien już osiągnąć swój cel wagowy, co oznacza, że użytkownik jest już za późno na osiągnięcie swojego celu wagowego i może potrzebować zmienić swoją strategię, aby zacząć robić postępy.
        return "Cel powinieneś osiągnąć już lada chwila!"
        

    # Obliczamy przewidywaną datę osiągnięcia celu wagowego, dodając liczbę dni pozostałych do osiągnięcia celu wagowego do ostatniej daty pomiaru w danych historycznych
    goal_date = df[date_col].iloc[-1] + timedelta(days=days_reaming)


    # Zwracamy komunikat z przewidywaną datą osiągnięcia celu wagowego w formacie string, co oznacza, że użytkownik może oczekiwać osiągnięcia swojego celu wagowego około tej daty, jeśli będzie utrzymywał obecny trend wagi.
    return f"Utrzymując obecne tempo, osiągniesz cel za {days_reaming} dni ({goal_date.strftime('%Y-%m-%d')})."