import os                                      # importujemy moduł os, aby móc pracować z plikami i ścieżkami
import pandas as pd                            # importujemy pandas, aby móc pracować z danymi w formacie DataFrame
import matplotlib.pyplot as plt                # importujemy matplotlib, aby móc tworzyć wykresy

# Piotr Bacior - 15 722 - 2026 - Python - MH

# Funkcja show_bmi_trend_chart przyjmuje nazwę pliku CSV jako argument i wyświetla wykres trendu BMI na podstawie danych z tego pliku.
def show_bmi_trend_chart(csv_filename: str = "historia_bmi.csv") -> None: