import os                                       # importujemy moduł os, aby móc pracować z plikami i ścieżkami
import csv                                      # importujemy moduł csv, aby móc pracować z plikami CSV
from datetime import datetime                   # importujemy datetime, aby móc pracować z datami i czasem

# Piotr Bacior - 15 722 - 2026 - Python - MH

# Funkcja save_result_to_file zapisuje wynik obliczeń BMI do pliku tekstowego, wraz z datą i czasem, oraz informacjami o wadze, wzroście, wartości BMI i kategorii zdrowotnej.
def save_result_to_file(weight_kg: float, height_m: float, bmi_value: float, category: str, min_ideal: float, max_ideal: float, filename: str = "bmi_results.txt") -> None:

    """
    Zapisuje wynik obliczeń BMI do pliku tekstowego wraz z obecną datą i godziną 

    Oczekiwane dane wejściowe:
    - weight_kg: waga w kilogramach (float)
    - height_m: wzrost w metrach (float)
    - bmi_value: obliczone BMI (float)
    - category: kategoria zdrowotna (str)
    - min_ideal: minimalna idealna waga (float)
    - max_ideal: maksymalna idealna waga (float)
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
    line_to_save = f"{now} - Waga: {weight_kg} kg, Wzrost: {height_m} m, BMI: {bmi_value}, Kategoria: {category} | Idealna waga: {min_ideal} - {max_ideal} kg\n"   


    # Próbujemy otworzyć plik i zapisać linijkę z wynikiem, obsługując potencjalne wyjątki związane z operacjami na plikach
    try: 

        # with open(...) to nasz bezpieczny sposób pracy z plikami w Pythonie
        # Tryb "a" (append) pozwala na dopisywanie nowych wyników do końca pliku, bez usuwania starych danych
        # encoding="utf-8" zapewnia, że plik będzie zapisany w formacie UTF-8, co jest ważne dla poprawnego wyświetlania polskich znaków

        with open(filename, "a", encoding="utf-8") as file: 
            
            # Zapisujemy przygotowaną linijkę do pliku
            file.write(line_to_save)                
    

    # Jeśli wystąpi błąd podczas operacji na pliku, przechwytujemy wyjątek IOError i wyświetlamy komunikat o błędzie wraz z informacją o przyczynie
    except IOError as e:

        # Jeśli wystąpi błąd podczas operacji na pliku, wyświetlamy komunikat o błędzie wraz z informacją o przyczynie
        print(f"Nie można zapisać wyniku do pliku: {e}")


# Funkcja read_history_from_file odczytuje zawartość pliku z historią wyników BMI i zwraca ją jako listę linijek tekstu.
def read_history_from_file(filename: str = "bmi_results.txt") -> list:

    """ 
    Odczytuje historię pomiarów z pliku tekstowego

    Oczekiwane dane wejściowe:
    - filename: nazwa pliku, z którego zostanie odczytana historia (domyślnie "bmi_results.txt")

    Zachowanie funkcji:
    - Sprawdza, czy plik istnieje na dysku
    - Jeżeli istnieje, odczytuje wszystkie linie i zwraca je jako listę
    - Jeżeli nie istnieje, zwraca pustą listę

    Ograniczenia:
    - Funkcja przeznaczona jest do działania w środowisku konsolowym, gdzie użytkownik może mieć dostęp do plików tekstowych

    Podnoszenie wyjątków:
    - Obsługuje potencjalne wyjątki związane z operacjami na plikach (np. IOError) i wyświetla komunikat o błędzie, jeśli odczyt z pliku się nie powiedzie

    """

    # Sprawdzamy, czy plik istnieje na dysku, aby uniknąć błędów podczas próby odczytu nieistniejącego pliku

    if not os.path.exists(filename):        # Sprawdzamy, czy plik istnieje na dysku

        return []                           # Jeżeli plik nie istnieje, zwracamy pustą listę
    
    
    # Jeżeli plik istnieje, próbujemy go otworzyć i odczytać wszystkie linie, obsługując potencjalne wyjątki związane z operacjami na plikach
    try:
        # Otwieramy plik w trybie odczytu ("r" - read) i encoding="utf-8", aby poprawnie odczytać polskie znaki
        with open(filename, "r", encoding="utf-8") as file: 

            # Odczytujemy wszystkie linie z pliku i zwracamy je jako listę

            return file.readlines()          # Zwracamy listę linijek odczytanych z pliku
        

    # Jeśli wystąpi błąd podczas operacji na pliku, przechwytujemy wyjątek IOError i wyświetlamy komunikat o błędzie wraz z informacją o przyczynie
    except IOError as e:

        # Jeśli wystąpi błąd podczas operacji na pliku, wyświetlamy komunikat o błędzie wraz z informacją o przyczynie
        print(f"Nie można odczytać historii z pliku: {e}")

        return                                # W przypadku błędu zwracamy pustą listę
    

# Funkcja save_to_csv zapisuje wynik obliczeń BMI do pliku CSV, wraz z datą i czasem, oraz informacjami o wadze, wzroście, wartości BMI i kategorii zdrowotnej.
def save_to_csv(weight_kg: float, height_m: float, bmi_value: float, category: str, min_ideal: float, max_ideal: float, filename: str = "historia_bmi.csv") -> None:

    """
    Zapisuje wynik obliczeń BMI do pliku CSV

    Oczekiwane dane wejściowe:

    - weight_kg: waga w kilogramach (float)
    - height_m: wzrost w metrach (float)
    - bmi_value: obliczone BMI (float)
    - category: kategoria zdrowotna (str)
    - min_ideal: minimalna idealna waga (float)
    - max_ideal: maksymalna idealna waga (float)
    - filename: nazwa pliku CSV, do którego zostanie zapisany wynik (domyślnie "historia_bmi.csv")

    Zachowanie funkcji:
    - Sprawdza, czy plik CSV już istnieje, aby zdecydować, czy należy dodać nagłówki kolumn
    - Zapisuje dane jako czysty wiersz w tabeli, oddzielając wartosci średnikiem 
    - Używamy średnika jako separatora, ponieważ excel tak dzieli kolumny 
    
    Ograniczenia:
    - Funkcja przeznaczona jest do działania w środowisku konsolowym, gdzie użytkownik może mieć dostęp do plików CSV

    Podnoszenie wyjątków:
    - Obsługuje potencjalne wyjątki związane z operacjami na plikach (np. IOError) i wyświetla komunikat o błędzie, jeśli zapis do pliku się nie powiedzie

    """

    file_exists = os.path.isfile(filename)                   # Sprawdzamy, czy plik CSV już istnieje, aby zdecydować, czy należy dodać nagłówki kolumn
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")       # Pobieramy aktualną datę i czas, formatując ją jako "YYYY-MM-DD HH:MM:SS"

    
    try:
        
        # Otwieramy plik CSV w trybie dopisywania ("a" - append) i encoding="utf-8", aby poprawnie zapisać polskie znaki
        with open(filename, "a", newline='', encoding="utf-8") as csvfile:

            writer = csv.writer(csvfile, delimiter=';')    # Tworzymy obiekt writer z modułu csv, używając średnika jako separatora


            # Jeżeli plik nie istnieje, zapisujemy nagłówki kolumn, aby ułatwić późniejszą analizę danych w programie Excel lub innym arkuszu kalkulacyjnym

            if not file_exists:                            # Jeśli plik nie istnieje, zapisujemy nagłówki kolumn
                writer.writerow(["Data i czas", "Waga (kg)", "Wzrost (m)", "BMI", "Kategoria", "Idealna waga min (kg)", "Idealna waga max (kg)"])

            # Zapisujemy dane jako czysty wiersz w tabeli, oddzielając wartosci średnikiem
            writer.writerow([now, weight_kg, height_m, bmi_value, category, min_ideal, max_ideal])    

    except IOError as e:
        
        # Jeśli wystąpi błąd podczas operacji na pliku, wyświetlamy komunikat o błędzie wraz z informacją o przyczynie
        print(f"Nie można zapisać wyniku do pliku CSV: {e}")