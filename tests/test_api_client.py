import unittest                                                 # importuję moduł unittest do tworzenia testów jednostkowych
from src.api_client import get_meal_suggestions                 # importuję funkcję get_meal_suggestions z modułu api_client

# Piotr Bacior - 15 722 - 2026 - Python - MH

# Tworzę klasę TestAPIClient, która dziedziczy po unittest.TestCase, co pozwala mi definiować metody testowe dla funkcji get_meal_suggestions
class TestAPIClient(unittest.TestCase) : 

    """ Klasa testująca połączenia sieciowe i zewnętrzne API. """

    # Definiuję metodę testową, która sprawdza, czy funkcja get_meal_suggestions zwraca listę przepisów o odpowiedniej strukturze danych (nazwa, kalorie, składniki) dla różnych wartości docelowej kaloryczności (target_kcal)
    def test_fallback_recipes(self) : 