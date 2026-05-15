import unittest                                                # importuję moduł unittest do tworzenia testów jednostkowych 
import os                                                      # importuję moduł os do operacji na systemie plików
import tempfile                                                # importuję moduł tempfile do tworzenia tymczasowych plików
import src.database as db                                      # importuję moduł database z katalogu src, który zawiera funkcje do zarządzania bazą danych

# Piotr Bacior - 15 722 - 2026 - Python - MH


# Tworzę klasę TestDatabase, która dziedziczy po unittest.TestCase, co pozwala mi definiować metody testowe dla funkcji zarządzających bazą danych
class TestDatabase(unittest.TestCase) : 

    """ Klasa testująca funkcje zarządzające bazą danych. """

    # Definiuję metodę setUp, która jest wywoływana przed każdym testem, aby przygotować środowisko testowe - w tym przypadku tworzy tymczasową bazę danych i ustawia jej ścieżkę w module database
    def setUp(self) : 