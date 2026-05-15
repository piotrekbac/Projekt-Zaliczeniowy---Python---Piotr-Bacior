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

        """ Kod, który wynukuje się ZANIM uruchomi się każdy test (przygotowanie środowsiska) """

        # Tworzę tymczasowy katalog, który będzie służył jako miejsce przechowywania tymczasowej bazy danych podczas testów
        self.temp_dir = tempfile.TemporaryDirectory()

        # Ustawiam ścieżkę do tymczasowej bazy danych, która będzie używana podczas testów, aby nie wpływać na rzeczywistą bazę danych aplikacji
        self.test_db_path = os.path.join(self.temp_dir.name, "testowa_baza.db")

        # Podmieniamy ścieżkę bazy z modułu na naszą tymczasową!
        db.DB_NAME = self.test_db_path

        # Inicjalizujemy bazę danych, tworząc w niej niezbędne tabele i struktury, aby była gotowa do użycia podczas testów
        db.init_db()


    # Definiuję metodę tearDown, która jest wywoływana po każdym teście, aby posprzątać środowisko testowe - w tym przypadku usuwa tymczasową bazę danych i zwalnia zasoby
    def tearDown(self) : 