import unittest             # importuję moduł unittest do tworzenia testów jednostkowych
import os                   # importuję moduł os do operacji na plikach
import tempfile             # importuję moduł tempfile do tworzenia tymczasowych plików
import csv                  # importuję moduł csv do obsługi plików CSV

# Importuję funkcje save_result_to_file, read_history_from_file i save_to_csv z modułu file_handler
from src.file_handler import save_result_to_file, read_history_from_file, save_to_csv   

# Piotr Bacior - 15 722 - 2026 - Python - MH


# Tworzę klasę TestFileHandler, która dziedziczy po unittest.TestCase, co pozwala mi definiować metody testowe dla funkcji save_result_to_file, read_history_from_file i save_to_csv
class TestFileHandler(unittest.TestCase) : 

    """ Klasa testująca zapis i odczyt z systemu plików (TXT oraz CSV) """

    
    # Definiuję metodę testową, która sprawdza, czy funkcja save_result_to_file poprawnie zapisuje dane do pliku tekstowego, a następnie czy funkcja read_history_from_file poprawnie odczytuje te dane
    def test_txt_read_write(self) :

        """ Sprawdza cykl życia pliku tekstowego: zapisz dane i odczytaj je poprawnie """

        # Tworzymy bezpieczny, tymczasowy folder dla testu
        with tempfile.TemporaryDirectory() as tmpdir:
            test_file = os.path.join(tmpdir, "test_historia.txt")

        # Krok 1: Zapis
            save_result_to_file(70.0, 1.75, 22.8, "Waga prawidłowa", 50.0, 70.0, filename=test_file)

        # Krok 2: Odczyt
            history = read_history_from_file(filename=test_file)

        # Krok 3: Sprawdzanie
            self.assertEqual(len(history), 1)                   # Powinna być dokładnie 1 linijka
            self.assertIn("Waga: 70.0", history[0])             # Sprawdzamy czy nasza waga się zapisała
            self.assertIn("Wzrost: 1.75", history[0])           # Sprawdzamy czy nasz wzrost się zapisał

    
     def test_csv_write(self) :