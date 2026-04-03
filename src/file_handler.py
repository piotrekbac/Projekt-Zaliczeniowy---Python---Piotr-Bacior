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

    Podnoszenie wyjątków:
    - Obsługuje potencjalne wyjątki związane z operacjami na plikach (np. IOError) i wyświetla komunikat o błędzie, jeśli zapis do pliku się nie powiedzie

    """

    # Pobieramy aktualną datę i czas, formatując ją jako "YYYY-MM-DD HH:MM:SS"
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")    


    # Przygotowujemy linijkę tekstu do zapisania, zawierającą datę, wagę, wzrost, wartość BMI i kategorię zdrowotną
    line_to_save = f"{now} - Waga: {weight_kg} kg, Wzrost: {height_m} m, BMI: {bmi_value}, Kategoria: {category}\n"   


    # Próbujemy otworzyć plik i zapisać linijkę z wynikiem, obsługując potencjalne wyjątki związane z operacjami na plikach
    try: 
        # with open(...) to nasz bezpieczny sposób pracy z plikami w Pythonie
        # Tryb "a" (append) pozwala na dopisywanie nowych wyników do końca pliku, bez usuwania starych danych
        # encoding="utf-8" zapewnia, że plik będzie zapisany w formacie UTF-8, co jest ważne dla poprawnego wyświetlania polskich znaków