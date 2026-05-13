import unittest                                                 # importuję moduł unittest do tworzenia testów jednostkowych
from src.api_client import get_meal_suggestions                 # importuję funkcję get_meal_suggestions z modułu api_client

# Piotr Bacior - 15 722 - 2026 - Python - MH

# Tworzę klasę TestAPIClient, która dziedziczy po unittest.TestCase, co pozwala mi definiować metody testowe dla funkcji get_meal_suggestions
class TestAPIClient(unittest.TestCase) : 