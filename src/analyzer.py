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

    # Definiujemy zakres skali BMI i długość paska
    min_scale = 15.0
    max_scale = 40.0
    bar_length = 40

    # Upewniamy się, że wskaźnik nie wyjdzie fizycznie poza narysowany pasek 
    clamped_bmi = max(min_scale, min(bmi_value, max_scale))

    # Obliczamy pozycję na pasku 
    position = int((clamped_bmi - min_scale) / (max_scale - min_scale) * bar_length)

    # Zapewniamy, że pozycja nie przekroczy długości paska
    if position >= bar_length:
        position = bar_length - 1                           # Zapewniamy, że pozycja nie przekroczy długości paska


    # Tworzymy części paska: lewą stronę, nasz znacznik i prawą stronę 
    left_part = '-' * position
    marker = 'O'                                            # Znacznik reprezentujący aktualną wartość BMI
    right_part = '-' * (bar_length - position - 1)

    # Składamy cały pasek i zwracamy go jako string
    return f"15.0[{left_part}{marker}{right_part}]40.0+"


# Definiuję funkcję do obliczania różnicy w kilogramach między aktualną a idealną wagą - dane wejściowe są typu float, oczekujemy wyniku typu str
def calculate_weight_difference(current_weight: float, min_ideal: float, max_ideal: float) -> str :

    """ 
    Oblicza i zwraca różnicę w kilogramach pomiędzy obecną a idealną wagą.

    Oczekiwane dane wejściowe:
    - current_weight: aktualna waga użytkownika (float)
    - min_ideal: minimalna idealna waga (float)
    - max_ideal: maksymalna idealna waga (float)
    
    Zachowanie funkcji:
    - Oblicza różnicę między aktualną wagą a minimalną idealną wagą
    - Oblicza różnicę między aktualną wagą a maksymalną idealną wagą
    - Zwraca sformatowany string z informacją o tym, ile kilogramów użytkownik musi schudnąć lub przytyć, aby osiągnąć idealną wagę

    """

    # Obliczamy różnicę między aktualną wagą a minimalną idealną wagą
    if current_weight < min_ideal :