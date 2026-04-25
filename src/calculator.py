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
    

    # Konwertujemy wzrost z metrów na centymetry, ponieważ wzór Mifflin-St Jeor używa centymetrów
    height_cm = height_m * 100   


    # Wzór dla mężczyzn 
    if gender == 'm':
         
        # Obliczamy BMR dla mężczyzn według wzoru Mifflin-St Jeor
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5    

    # Wzór dla kobiet
    else:

        # Obliczamy BMR dla kobiet według wzoru Mifflin-St Jeor
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) - 161


    # Zaokrąglamy wynik do dwóch miejsc po przecinku
    return round(bmr, 2)    


# Definiuję funkcję do obliczania TDEE (Total Daily Energy Expenditure) na podstawie BMR i poziomu aktywności fizycznej - zapotrzebowanie kaloryczne
def calculate_tdee(bmr: float, activity_level: str) -> float:

    """
    Oblicza całkowite dzienne zapotrzebowanie kaloryczne (TDEE) na podstawie BMR i poziomu aktywności fizycznej

    Oczekiwane dane wejściowe:
    - bmr: BMR (Basal Metabolic Rate) w kaloriach (float)
    - activity_level: poziom aktywności fizycznej (str), oczekiwane wartości to "siedzący", "lekko aktywny", "umiarkowanie aktywny", "bardzo aktywny"
    
    Zachowanie funkcji:
    - Oblicza TDEE, mnożąc BMR przez odpowiedni współczynnik aktywności fizycznej:
      - 1. Siedzący (brak aktywności): TDEE = BMR * 1.2
      - 2. Lekko aktywny (trening 1-3 razy w tygodniu): TDEE = BMR * 1.375
      - 3. Umiarkowanie aktywny (trening 3-5 razy w tygodniu): TDEE = BMR * 1.55
      - 4. Bardzo aktywny (trening 6-7 razy w tygodniu): TDEE = BMR * 1.725
      - 5. Ekstremalnie aktywny (bardzo ciężka praca fizyczna lub trening dwa razy dziennie): TDEE = BMR * 1.9


    Ograniczenia:
    - Oczekiwana wartość 'bmr' musi być dodatnia (> 0)
    - Oczekiwana wartość 'activity_level' musi być jedną z określonych wartości

    Podnoszenie wyjątków:
    - ValueError: jeśli 'bmr' jest mniejsze lub równe 0, lub jeśli 'activity_level' nie jest jedną z określonych wartości

    """

    # Sprawdzamy, czy BMR jest większe niż 0, aby uniknąć błędów przy obliczaniu TDEE
    if bmr <= 0:
        raise ValueError("BMR musi być większe od zera.")


    # Tworzymy słownik z poziomami aktywności i odpowiadającymi im współczynnikami

    multipliers = {
        1: 1.2,         # Brak aktywności (praca siedząca)
        2: 1.375,       # Lekka aktywność (trening 1-3 razy w tyg.)
        3: 1.55,        # Średnia aktywność (trening 3-5 razy w tyg.)
        4: 1.725,       # Wysoka aktywność (trening 6-7 razy w tyg.)
        5: 1.9          # Bardzo wysoka aktywność (praca fizyczna)
    }    


    # Sprawdzamy czy poziom aktywności jest poprawny, aby uniknąć błędów przy obliczaniu TDEE
    if activity_level not in multipliers:

        # Informujemy użytkownika, że poziom aktywności musi być jednym z określonych wartości
        raise ValueError("Poziom aktywności musi być jednym z następujących: 1, 2, 3, 4, 5.")
    
    # Obliczamy TDEE, mnożąc BMR przez odpowiedni współczynnik aktywności
    tdee = bmr * multipliers[activity_level]   

    # Zaokrąglamy wynik do dwóch miejsc po przecinku
    return round(tdee, 2)


# Definiuję funkcję do obliczania zapotrzebowania na makroskładniki (Białko, Tłuszcze, Węglowodany) w gramach - dane wejściowe są typu float i str, oczekujemy wyniku typu tuple[int, int, int]
def calculate_macros(target_kcal: float, goal: str) -> tuple[int, int, int] :

    """
    Oblicza zapotrzebowanie na makroskładniki (Białko, Tłuszcze, Węglowodany) w gramach.

    Oczekiwane dane wejściowe:
    - target_kcal: docelowa ilość kalorii (float)
    - goal: cel dietetyczny ("redukcja", "masa", "utrzymanie") (str)

    Zachowanie funkcji:
    - Zależnie od celu przydziela proporcje % makroskładników.
    - Dzieli kalorie przez wartość energetyczną (Białko/Węgle = 4 kcal/g, Tłuszcz = 9 kcal/g).
    - Zwraca krotkę (Białko, Tłuszcze, Węglowodany) w pełnych gramach (int).

    Ograniczenia:
    - target_kcal musi być większe niż 0.
    - goal musi być jednym z: "redukcja", "masa", "utrzymanie".

    Podnoszenie wyjątków:
    - ValueError: jeśli target_kcal jest mniejsze lub równe 0, lub jeśli goal nie jest jednym z określonych wartości.

    """

    # Sprawdzamy, czy docelowe kalorie są większe niż 0, aby uniknąć błędów przy obliczaniu makroskładników
    if target_kcal <= 0:
        raise ValueError("Docelowe kalorie muszą być większe od zera.")   