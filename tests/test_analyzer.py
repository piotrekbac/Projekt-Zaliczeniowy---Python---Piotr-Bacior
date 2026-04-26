import unittest                                                      # importuję moduł unittest do tworzenia testów jednostkowych
from src.analyzer import analyze_bmi, calculate_weight_difference, generate_bmi_bar               # importuję funkcje analyze_bmi i generate_bmi_bar z modułu analyzer

# Piotr Bacior - 15 722 - 2026 - Python - MH

# Tworzę klasę TestAnalyzer, która dziedziczy po unittest.TestCase, co pozwala mi definiować metody testowe dla funkcji analyze_bmi i generate_bmi_bar
class TestAnalyzer(unittest.TestCase) : 

    """ Klasa testująca analizę wyników i generowanie interfejsu tekstowego. """


    # Definiuję metodę testową, która sprawdza, czy funkcja analyze_bmi poprawnie kategoryzuje wyniki BMI zgodnie ze skalą WHO
    def test_analyze_bmi_categories(self) :

        """ Sprawdza, czy funkcja poprawnie kategoryzuje wyniki BMI wg skali WHO. """

        self.assertEqual(analyze_bmi(17.0), "Niedowaga")        # Sprawdzam, czy BMI 17.0 jest poprawnie sklasyfikowane jako "Niedowaga"
        self.assertEqual(analyze_bmi(22.0), "Waga prawidłowa")  # Sprawdzam, czy BMI 22.0 jest poprawnie sklasyfikowane jako "Waga prawidłowa"
        self.assertEqual(analyze_bmi(27.0), "Nadwaga")          # Sprawdzam, czy BMI 27.0 jest poprawnie sklasyfikowane jako "Nadwaga"
        self.assertEqual(analyze_bmi(35.0), "Otyłość")          # Sprawdzam, czy BMI 35.0 jest poprawnie sklasyfikowane jako "Otyłość"


    # Definiuję metodę testową, która sprawdza, czy funkcja analyze_bmi podnosi odpowiednie wyjątki, gdy BMI jest równe lub mniejsze od zera
    def test_analyze_bmi_exceptions(self) :

        """ Sprawdza, czy funkcja wyłapuje niemożliwe (zerowe/ujemne) BMI. """

        # Sprawdzam, czy funkcja analyze_bmi podnosi ValueError, gdy BMI jest równe 0.0
        with self.assertRaises(ValueError):             
            analyze_bmi(0.0)

        # Sprawdzam, czy funkcja analyze_bmi podnosi ValueError, gdy BMI jest mniejsze od 0.0
        with self.assertRaises(ValueError):
            analyze_bmi(-5.0)

        # Sprawdzam, czy funkcja analyze_bmi podnosi ValueError, gdy BMI jest równe -1.0
        with self.assertRaises(ValueError):
            analyze_bmi(-1.0)

        # Sprawdzam, czy funkcja analyze_bmi podnosi ValueError, gdy BMI jest równe -0.1
        with self.assertRaises(ValueError):
            analyze_bmi(-0.1)
   

    # Definiuję metodę testową, która sprawdza, czy funkcja generate_bmi_bar poprawnie tworzy tekstowy pasek skali (ASCII) dla różnych wartości BMI
    def test_generate_bmi_bar(self) :

        """ Sprawdza poprawne tworzenie tekstowego paska skali (ASCII). """

        # Test skrajnie niskiego BMI (znacznik 'O' powinien być na samym początku lub blisko)
        bar_low = generate_bmi_bar(10.0)        # Zostanie zablokowane na min_scale 15.0
        self.assertTrue(bar_low.startswith("15.0[O-"))

        # Test prawidłowej długości paska (40 znaków w nawiasach + napisy)
        bar_normal = generate_bmi_bar(25.0)
        self.assertIn("O", bar_normal)          # Pasek musi zawierać znacznik


    # Test dla funkcji analyze_bmi, która oblicza różnicę między aktualnym BMI a idealnym zakresem BMI (18.5-24.9) i zwraca informację o tym, ile jednostek BMI trzeba zredukować lub zwiększyć, aby znaleźć się w idealnym zakresie
    def test_calculate_weight_difference(self) :

        """ Sprawdza odliczanie kilogramów do idealnej wagi. """

        # min = 50, max = 70

        # Test dla osoby, która ma niedowagę (BMI poniżej 18.5) - powinno zwrócić informację, ile kilogramów trzeba przytyć, aby znaleźć się w idealnym zakresie
        self.assertIn("Brakuje Ci 10.0 kg", calculate_weight_difference(40.0, 50.0, 70.0))

        # Test dla osoby, która ma nadwagę (BMI powyżej 24.9) - powinno zwrócić informację, ile kilogramów trzeba zrzucić, aby znaleźć się w idealnym zakresie
        self.assertIn("Musisz zrzucić 10.0 kg", calculate_weight_difference(80.0, 50.0, 70.0))

        # Test dla osoby, która jest już w idealnym przedziale (BMI między 18.5 a 24.9) - powinno zwrócić informację, że jest w idealnym przedziale
        self.assertIn("Jesteś w idealnym przedziale", calculate_weight_difference(60.0, 50.0, 70.0))