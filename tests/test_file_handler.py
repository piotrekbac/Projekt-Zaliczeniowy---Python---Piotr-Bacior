import unittest             # importuję moduł unittest do tworzenia testów jednostkowych
import os                   # importuję moduł os do operacji na plikach
import tempfile             # importuję moduł tempfile do tworzenia tymczasowych plików
import csv                  # importuję moduł csv do obsługi plików CSV

# Importuję funkcje save_result_to_file, read_history_from_file i save_to_csv z modułu file_handler
from src.file_handler import save_result_to_file, read_history_from_file, save_to_csv   

# Piotr Bacior - 15 722 - 2026 - Python - MH


# Tworzę klasę TestFileHandler, która dziedziczy po unittest.TestCase, co pozwala mi definiować metody testowe dla funkcji save_result_to_file, read_history_from_file i save_to_csv
class TestFileHandler(unittest.TestCase) : 

    """ Klasa testująca zapis i odczyt z systemu plików (TXT oraz CSV). """


    def test_txt_read_write(self) :