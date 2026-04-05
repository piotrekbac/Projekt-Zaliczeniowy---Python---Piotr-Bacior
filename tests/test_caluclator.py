import unittest                                                     # Importujemy moduł unittest, który służy do tworzenia i uruchamiania testów jednostkowych
from src.calculator import calculate_bmi, calculate_ideal_weight    # Importujemy funkcje calculate_bmi i calculate_ideal_weight z modułu calculator

# Piotr Bacior - 15 722 - 2026 - Python - MH

# Tworzymy klasę TestCalculator, która dziedziczy po unittest.TestCase, co pozwala nam definiować metody testowe 
class TestCalculator(unittest.TestCase): 
    """ Klasa zawierająca testy jednostkowe dla funkcji calculate_bmi i calculate_ideal_weight z modułu calculator """


    def test_calculate_bmi_correct_values(self):
        """ Sprawdza, czy funkcja prawidłowo oblicza BMI dla poprawnych wartości wagi i wzrostu """

        # Wzór: self.assertEqual(A, B) - sprawdza, czy A jest równe B
        # Sprawdzimy: waga 75 kg i wzrost 1.80m. Oczekiwany wynik BMI: 23.15
        self.assertEqual(calculate_bmi(75, 1.80), 23.15)