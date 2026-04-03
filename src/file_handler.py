from datetime import datetime       # importujemy datetime, aby móc pracować z datami i czasem

# Funkcja save_result_to_file zapisuje wynik obliczeń BMI do pliku tekstowego, wraz z datą i czasem, oraz informacjami o wadze, wzroście, wartości BMI i kategorii zdrowotnej.
def save_result_to_file(weight_kg: float, height_m: float, bmi_value: float, category: str, filename: str = "bmi_results.txt") -> None:

    """
    Zapisuje wynik obliczeń BMI do pliku tekstowego wraz z obecną datą i godziną 

    Oczekiwane dane wejściowe:
    - weight_kg: waga w kilogramach (float)
    - height_m: wzrost w metrach (float)
    - bmi_value: obliczone BMI (float)
    - category: kategoria zdrowotna (str)
    - filename: nazwa pliku, do którego zostanie zapisany wynik (domyślnie "bmi_results.txt")

    Zachowanie funkcji:
    - Pobiera aktualną datę i czas systemowy 
    - Otwiera plik w trybie dopisywania ("a" - append), aby nie nadpisywać starych wyników
    - Zapisuje sformatowaną linijkę z wynikiem

    Ograniczenia:
    - Funkcja przeznaczona jest do działania w środowisku konsolowym, gdzie użytkownik może mieć dostęp do plików tekstowych

    """
