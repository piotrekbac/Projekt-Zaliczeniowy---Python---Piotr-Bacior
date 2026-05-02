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