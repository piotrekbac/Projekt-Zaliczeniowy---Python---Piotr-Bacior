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

    
    """