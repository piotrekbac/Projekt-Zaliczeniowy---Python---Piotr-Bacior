from datetime import datetime       # importujemy datetime, aby móc pracować z datami i czasem

# Funkcja save_result_to_file zapisuje wynik obliczeń BMI do pliku tekstowego, wraz z datą i czasem, oraz informacjami o wadze, wzroście, wartości BMI i kategorii zdrowotnej.
def save_result_to_file(weight_kg: float, height_m: float, bmi_value: float, category: str, filename: str = "bmi_results.txt") -> None:
