import requests                                                 # import modułu requests do obsługi zapytań HTTP
import random                                                   # import modułu random do generowania losowych danych (symulacja)

# Piotr Bacior - 15 722 - 2026 - Python - MH

# Tutaj podaję swoje darmowe klucze z serwisu Edamam.com (zakładka Recipe Search API).
# Jeśli zostawiamy je puste, program automatycznie użyje wbudowanego trybu "Fallback" (Zabezpieczającego).

API_ID = ""     # Nasz API ID z Edamam.com#
API_KEY = ""    # Nasz API Key z Edamam.com#


# Funkcja do pobierania sugestii posiłków na podstawie docelowej kaloryczności (target_kcal).
def get_meal_suggestions(target_kcal: float) -> list : 

    """
    Łączy się z internetową bazą Edamam API, aby pobrać przepisy kulinarne.
    Szuka posiłków, które mają około 1/3 Twojego dziennego zapotrzebowania.

    """

    # Celujemy w posiłki o kaloryczności około 1/3 dziennego zapotrzebowania
    meal_kcal = int(target_kcal / 3)  



    # 1. Tryb internetowy (jeżeli mamy klucze API)

    # Sprawdzamy, czy mamy klucze API (nie są puste)
    if API_ID and API_KEY :

        # Zakres kaloryczności dla wyszukiwania (± 100 kcal od celu)
        kcal_range = f"{meal_kcal - 100}-{meal_kcal + 100}"

        # Budujemy URL do zapytania do Edamam API, włączając nasze klucze i zakres kaloryczności - Pobieramy maksymalnie 5 przepisów
        url = f"https://api.edamam.com/api/recipes/v2?type=public&q=healthy&app_id={API_ID}&app_key={API_KEY}&calories={kcal_range}&random=true"  


        # Próbujemy wykonać zapytanie do API
        try :

            # Wysyłamy zapytanie GET do API z limitem czasu 5 sekund
            response = requests.get(url, timeout=5)   

            # Sprawdzamy, czy odpowiedź jest poprawna (status code 200)
            if response.status_code == 200 :   

                # Parsujemy odpowiedź JSON na słownik Pythona
                data = response.json()   

                # Pobieramy listę przepisów (hits) z odpowiedzi
                hits = data.get("hits", [])   

                # Lista do przechowywania przepisów
                recipes = []   

                # Iterujemy przez każdy przepis (hit) i wyciągamy potrzebne informacje
                for hit in hits :

                    # Pobieramy dane przepisu
                    recipe = hit['recipe']   

                    # Dodajemy przepis do listy, wyciągając nazwę, kaloryczność i składniki
                    recipes.append({

                        # Nazwa przepisu
                        "name": recipe["label"],

                        # Kaloryczność przepisu (zaokrąglona do int)
                        "calories": int(recipe["calories"]),  

                        # Składniki przepisu (lista)
                        "image": recipe["image"],

                        # URL do przepisu
                        "url": recipe["url"],
                    })

                # Jeżeli API znalazło przynajmniej 3 przepisy, zwracamy je
                if len(recipes) == 3 :

                    # Zwracamy listę 3 przepisów
                    return recipes
                
        # Jeżeli wystąpił błąd podczas zapytania do API, przechodzimy do trybu "Fallback"
        except Exception as e :