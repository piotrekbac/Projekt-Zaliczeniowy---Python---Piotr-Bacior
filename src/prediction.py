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

        # Jeżeli DataFrame jest pusty, zwracamy komunikat o braku danych historycznych, co oznacza, że nie możemy przewidzieć daty osiągnięcia celu wagowego
        return _calculate_trend(df, target_weight, 'Data i czas', 'Waga (kg)')

    # Obsługa wszelkich nieoczekiwanych błędów, które mogą wystąpić podczas wczytywania danych, przetwarzania danych lub obliczeń regresji liniowej. Jeśli wystąpi jakikolwiek błąd, zwracamy komunikat o błędzie, co pozwala użytkownikowi na zrozumienie, że coś poszło nie tak i może potrzebować sprawdzić dane wejściowe lub skonsultować się z pomocą techniczną.
    except Exception as e :

        # Zwracamy komunikat o błędzie wraz z informacją o tym, co poszło nie tak, co pozwala użytkownikowi na zrozumienie, że coś poszło nie tak i może potrzebować sprawdzić dane wejściowe lub skonsultować się z pomocą techniczną
        return f"Błąd algorytmu: {e}"
    

    # Funkcja pomocnicza do obliczania trendu i przewidywania daty osiągnięcia celu wagowego na podstawie danych historycznych
    def predict_goal_from_sql(df: pd.DataFrame, target_weight: float) -> str :

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

