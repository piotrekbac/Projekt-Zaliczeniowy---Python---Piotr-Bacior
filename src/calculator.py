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

    """