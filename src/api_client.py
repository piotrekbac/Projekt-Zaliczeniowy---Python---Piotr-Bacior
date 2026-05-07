import requests                                                 # import modułu requests do obsługi zapytań HTTP
import random                                                   # import modułu random do generowania losowych danych (symulacja)

# Piotr Bacior - 15 722 - 2026 - Python - MH

# Tutaj podaję swoje darmowe klucze z serwisu Edamam.com (zakładka Recipe Search API).
# Jeśli zostawiamy je puste, program automatycznie użyje wbudowanego trybu "Fallback" (Zabezpieczającego).

API_ID = ""     # Nasz API ID z Edamam.com#
API_KEY = ""    # Nasz API Key z Edamam.com#


# Funkcja do pobierania sugestii posiłków na podstawie docelowej kaloryczności (target_kcal).
def get_meal_suggestions(taget_kcal: float) -> list : 

    """
    Łączy się z internetową bazą Edamam API, aby pobrać przepisy kulinarne.
    Szuka posiłków, które mają około 1/3 Twojego dziennego zapotrzebowania.
    
    """