import unittest                                                     # Importujemy moduł unittest, który służy do tworzenia i uruchamiania testów jednostkowych
from src.calculator import calculate_bmi, calculate_ideal_weight    # Importujemy funkcje calculate_bmi i calculate_ideal_weight z modułu calculator

# Piotr Bacior - 15 722 - 2026 - Python - MH

# Tworzymy klasę TestCalculator, która dziedziczy po unittest.TestCase, co pozwala nam definiować metody testowe 
class TestCalculator(unittest.TestCase): 
    """ Klasa zawierająca testy jednostkowe dla funkcji calculate_bmi i calculate_ideal_weight z modułu calculator """


    # Definiujemy metodę testową, która sprawdza poprawność obliczeń BMI dla różnych zestawów danych wejściowych
    def test_calculate_bmi_correct_values(self):

        """ Sprawdza, czy funkcja prawidłowo oblicza BMI dla poprawnych wartości wagi i wzrostu """

        # Wzór: self.assertEqual(A, B) - sprawdza, czy A jest równe B

        # Sprawdzimy: waga 75 kg i wzrost 1.80m. Oczekiwany wynik BMI: 23.15
        self.assertEqual(calculate_bmi(75, 1.80), 23.15)

        # Sprawdzimy: waga 50 kg i wzrost 1.60m. Oczekiwany wynik BMI: 19.53
        self.assertEqual(calculate_bmi(50, 1.60), 19.53)

        # Sprawdzimy: waga 90 kg i wzrost 1.75m. Oczekiwany wynik BMI: 29.39
        self.assertEqual(calculate_bmi(90, 1.75), 29.39)


    # Definiujemy metodę testową, która sprawdza, czy funkcja calculate_bmi podnosi odpowiednie wyjątki, gdy waga lub wzrost są równe lub mniejsze od zera
    def test_calculate_bmi_zero_or_negative(self):

        """ Sprawdza, czy funkcja wyrzuca błąd ValueError przy błędnych danych wejściowych (waga lub wzrost <= 0) """

        # self.assertRaises(ValueError) sprawdza, czy kod poniżej wyrzuci ten konkretny wyjątek (ValueError)

        with self.assertRaises(ValueError):
            calculate_bmi(-10.0, 1.80)          # Waga ujemna - powinno wyrzucić ValueError

        with self.assertRaises(ValueError):
            calculate_bmi(75.0, 0.0)            # Wzrost zerowy - powinno wyrzucić ValueError


    # Definiujemy metodę testową, która sprawdza poprawność obliczeń idealnej wagi dla różnych wartości wzrostu
    def test_calculate_ideal_weight(self):

        """ Sprawdza, czy funkcja poprawnie oblicza idealną wagę dla różnych wartości wzrostu """

        # Wywołujemy fumkcję dla wzrostu 1.80m. Oczekiwany wynik: (59.94, 80.68)

        min_weight, max_weight = calculate_ideal_weight(1.80)

        # Wiemy, że idealna waga dla wzrostu 1.80m powinna być w zakresie 59.94 kg - 80.68 kg, więc sprawdzamy, czy obliczone wartości mieszczą się w tym zakresie
        
        self.assertEqual(min_weight, 59.94)    # Sprawdzamy, czy minimalna idealna waga jest równa 59.94 kg
        self.assertEqual(max_weight, 80.68)    # Sprawdzamy, czy maksymalna idealna waga jest równa 80.68 kg