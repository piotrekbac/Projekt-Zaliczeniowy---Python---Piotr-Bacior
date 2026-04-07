import os                                      # importujemy moduł os, aby móc pracować z plikami i ścieżkami
import pandas as pd                            # importujemy pandas, aby móc pracować z danymi w formacie DataFrame
import matplotlib.pyplot as plt                # importujemy matplotlib, aby móc tworzyć wykresy

# Piotr Bacior - 15 722 - 2026 - Python - MH

# Funkcja show_bmi_trend_chart przyjmuje nazwę pliku CSV jako argument i wyświetla wykres trendu BMI na podstawie danych z tego pliku.
def show_bmi_trend_chart(csv_filename: str = "historia_bmi.csv") -> None:

    """
    Generuje i wyświetla wykres trendu BMI na podstawie danych z pliku CSV z historią pomiarów BMI
    Wykorzystuje biblioteki Pandas (do analizy danych) i Matplotlib (do tworzenia wykresów)

    Oczekiwane dane wejściowe:
    - csv_filename: nazwa pliku CSV zawierającego historię pomiarów BMI (domyślnie "historia_bmi.csv")

    Zachowanie funkcji:
    - Sprawdza, czy plik CSV istnieje i jest dostępny do odczytu
    - Odczytuje dane z pliku CSV do obiektu DataFrame
    - Generuje wykres liniowy przedstawiający trend wartości BMI w czasie
    
    Ograniczenia:
    - Funkcja przeznaczona jest do działania w środowisku, gdzie możliwe jest wyświetlanie wykresów (np. Jupyter Notebook, środowisko graficzne)
    
    Podnoszenie wyjątków:
    - Obsługuje potencjalne błędy przy generowaniu wykresu

    """


    # Sprawdzamy, czy plik CSV istnieje na dysku
    if not os.path.exists(csv_filename):        

        # Informujemy użytkownika, że plik nie istnieje
        print(f"Plik {csv_filename} nie istnieje. Nie można wygenerować wykresu trendu BMI.")   

        # Kończymy działanie funkcji, ponieważ nie można wygenerować wykresu bez danych
        return                                                                                  