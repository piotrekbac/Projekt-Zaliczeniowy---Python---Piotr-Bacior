import unnittest                                                     # importuję moduł unittest do tworzenia testów jednostkowych
from src.analyzer import analyze_bmi, generate_bmi_bar               # importuję funkcje analyze_bmi i generate_bmi_bar z modułu analyzer

# Piotr Bacior - 15 722 - 2026 - Python - MH

# Tworzę klasę TestAnalyzer, która dziedziczy po unittest.TestCase, co pozwala mi definiować metody testowe dla funkcji analyze_bmi i generate_bmi_bar
class TestAnalyzer(unnittest.TestCase) : 

    """ Klasa testująca analizę wyników i generowanie interfejsu tekstowego. """


    # Definiuję metodę testową, która sprawdza, czy funkcja analyze_bmi poprawnie kategoryzuje wyniki BMI zgodnie ze skalą WHO
    def test_analyze_bmi_categories(self) :

        """ Sprawdza, czy funkcja poprawnie kategoryzuje wyniki BMI wg skali WHO. """

        self.assertEqual(analyze_bmi(17.0), "Niedowaga")        # Sprawdzam, czy BMI 17.0 jest poprawnie sklasyfikowane jako "Niedowaga"
        self.assertEqual(analyze_bmi(22.0), "Waga prawidłowa")  # Sprawdzam, czy BMI 22.0 jest poprawnie sklasyfikowane jako "Waga prawidłowa"
        self.assertEqual(analyze_bmi(27.0), "Nadwaga")          # Sprawdzam, czy BMI 27.0 jest poprawnie sklasyfikowane jako "Nadwaga"
        self.assertEqual(analyze_bmi(35.0), "Otyłość")          # Sprawdzam, czy BMI 35.0 jest poprawnie sklasyfikowane jako "Otyłość"



    def test_analyze_bmi_exceptions(self) :
        
        """ Sprawdza, czy funkcja wyłapuje niemożliwe (zerowe/ujemne) BMI. """