# Piotr Bacior - 15 722 - 2026 - Python - MH

# Definiuję funkcję do analizy wartości BMI i zwracania odpowiedniego komunikatu - dane wejściowe są typu float, oczekujemy wyniku typu str
def analyze_bmi(bmi_value: float) -> str:

    """
    Analizuje wskaźnik BMI i zwraca odpowiednią kategorię zdrowotną na podstawie wartości BMI

    Oczekiwane dane wejściowe:
    - bmi_value: wartość wskaźnika BMI (float)

    Zachowanie funkcji:
    - Porównuje wartosci BMI z przyjętymi normami światowej organizacji zdrowia (WHO) 
    - Zwraca łańcuch znaków (str) z nazwą odpowiedniej kategorii zdrowotnej 

    Ograniczenia:
    - Wartość 'bmi_value' powinna być dodatnia (> 0)

    Podnoszenie wyjątków:
    - ValueError: jeśli 'bmi_value' jest mniejsze lub równe 0

    """

    # Sprawdzamy, czy wartość BMI jest większa niż 0, aby uniknąć nieprawidłowych analiz
    if bmi_value <= 0:
        raise ValueError("Wartość BMI musi być większa niż 0.")

    # Analizujemy wartość BMI i zwracamy odpowiednią kategorię zdrowotną na podstawie norm WHO
    if bmi_value < 18.5:
        return "Niedowaga"
    elif bmi_value < 25.0:
        return "Waga prawidłowa"
    elif bmi_value < 30.0:
        return "Nadwaga"
    else:
        return "Otyłość"

# Definiuję funkcję do generowania wizualnej reprezentacji BMI w formie paska - dane wejściowe są typu float, oczekujemy wyniku typu str
def generate_bmi_bar(bmi_value: float) -> str:

    """ 
        Generuje tekstowy pasek wizualizujący wskaźnik BMI na skali

        Oczekiwane dane wejściowe:
        - bmi_value: wartość wskaźnika BMI (float)

        Zachowanie funkcji:
        - Rysuje 40-znakowy pasek (skala od 15.0 do 40.0)
        - Oblicza proporcjonalną pozycję dla podanego BMI 
        - Wstawia znacznik 'O' w odpowiednim miejscu na osi
        
    """