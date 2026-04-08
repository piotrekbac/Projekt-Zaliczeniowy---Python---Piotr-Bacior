# Piotr Bacior - 15 722 - 2026 - Python - MH

# Definiuję funkcję do obliczania BMI (Body Mass Index) - dane wejściowe są typu float, oczekujemy wyniku typu float 
def calculate_bmi(weight_kg: float, height_m: float) -> float: 

    """
    Oblicza BMI na podstawie wagi (w kilogramach) i wzrostu (w metrach)
    
    Oczekiwane dane wejściowe:
    - weight_kg: waga w kilogramach (float)
    - height_m: wzrost w metrach (float)

    Zachowanie funkcji:
    - Oblicza stosunek wagi do kwadratu wzrostu (BMI = waga / (wzrost^2))
    - Zwraca wskaźnik BMI jako wartość zmiennoprzecinkową (float)

    Ograniczenia: 
    - Oczekiwane wartosci 'weight_kg' i 'height_m' muszą być dodatnie (> 0)

    Podnoszenie wyjątków:
    - ValueError: jeśli 'weight_kg' lub 'height_m' jest mniejsze lub równe 0

    """

    # Sprawdzamy, czy waga i wzrost są większe niż 0, aby uniknąć błędów dzielenia przez zero lub negatywnych wartości
    if weight_kg <= 0:
        raise ValueError("Waga musi być większa niż 0.")
    if height_m <= 0:
        raise ValueError("Wzrost musi być większy niż 0.")
    

    bmi = weight_kg / (height_m ** 2)           # Obliczamy BMI jako wagę podzieloną przez kwadrat wzrostu
    return round(bmi, 2)                        # Zaokrąglamy wynik do dwóch miejsc po przecinku  


# Definiuję funkcję do obliczania idealnej wagi na podstawie wzrostu - dane wejściowe są typu float, oczekujemy wyniku typu tuple[float, float]
def calculate_ideal_weight(height_m: float) -> tuple[float, float]:
    
    """
    Oblicza zakres idealnej wagi dla danego wzrostu w metrach

    Oczekiwane dane wejściowe:
    - height_m: wzrost w metrach (float)

    Zachowanie funkcji:
    - Wykorzystuje minimalne (18.5) i maksymalne (24.9) wartości BMI, aby obliczyć dolną i górną granicę idealnej wagi
    - Zwraca dwuelementową krotkę (tuple) zawierającą dolną i górną granicę idealnej wagi w kilogramach (float)

    Ograniczenia:
    - Oczekiwana wartość 'height_m' musi być dodatnia (> 0)

    Podnoszenie wyjątków:
    - ValueError: jeśli 'height_m' jest mniejsze lub równe 0

    """

    # Sprawdzamy, czy wzrost jest większy niż 0, aby uniknąć błędów dzielenia przez zero lub negatywnych wartości
    if height_m <= 0:
        raise ValueError("Wzrost musi być większy niż 0.")
    

    # Wzór: Waga = BMI * (wzrost^2), gdzie BMI minimalne to 18.5, a maksymalne to 24.9

    min_weight = 18.5 * (height_m ** 2)   # Obliczamy dolną granicę idealnej wagi
    max_weight = 24.9 * (height_m ** 2)   # Obliczamy górną granicę idealnej wagi


    # Zwracamy krotkę z zaokrąglonymi wartościami idealnej wagi
    return round(min_weight, 2), round(max_weight, 2)   


# Definiuję funkcję do obliczania BMR (Basal Metabolic Rate) - dane wejściowe są typu float, oczekujemy wyniku typu float
def calculate_bmr(weight_kg: float, height_m: float, age: int, gender: str) -> float:

    """
    Oblicza BMR (Basal Metabolic Rate) na podstawie wagi, wzrostu, wieku i płci - wzorem Mifflin-St Jeor
    
    Oczekiwane dane wejściowe:
    - weight_kg: waga w kilogramach (float)
    - height_m: wzrost w metrach (float)
    - age: wiek w latach (int)
    - gender: płeć (str), oczekiwane wartości to "mężczyzna" lub "kobieta"

    Zachowanie funkcji:
    - Oblicza BMR na podstawie wzoru Mifflin-St Jeor:
      - Dla mężczyzn: BMR = 10 * waga + 6.25 * wzrost_cm - 5 * wiek + 5
      - Dla kobiet: BMR = 10 * waga + 6.25 * wzrost_cm - 5 * wiek - 161
    - Zwraca wartość BMR jako zmiennoprzecinkową (float)

    Ograniczenia:
    - Oczekiwane wartości 'weight_kg', 'height_m' i 'age' muszą być dodatnie (> 0)

    Podnoszenie wyjątków:
    - ValueError: jeśli 'weight_kg', 'height_m' lub 'age' jest mniejsze lub równe 0

    """

    # Sprawdzamy, czy waga, wzrost i wiek są większe niż 0, aby uniknąć błędów dzielenia przez zero lub negatywnych wartości
    if weight_kg <= 0 or height_m <= 0 or age <= 0:

        # Informujemy użytkownika, że waga, wzrost i wiek muszą być większe niż 0
        raise ValueError("Waga, wzrost i wiek muszą być większe niż 0.")
    
    # Sprawdzamy poprawność wartości płci, aby uniknąć błędów przy obliczaniu BMR - 'm' dla mężczyzn, 'k' dla kobiet
    if gender not in ["m", "k"]:

        # Informujemy użytkownika, że płeć musi być 'm' lub 'k'
        raise ValueError("Płeć musi być 'm' lub 'k'.")