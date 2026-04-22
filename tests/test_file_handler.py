import unittest             # importuję moduł unittest do tworzenia testów jednostkowych
import os                   # importuję moduł os do operacji na plikach
import tempfile             # importuję moduł tempfile do tworzenia tymczasowych plików
import csv                  # importuję moduł csv do obsługi plików CSV

# Importuję funkcje save_result_to_file, read_history_from_file i save_to_csv z modułu file_handler
from src.file_handler import save_result_to_file, read_history_from_file, save_to_csv   