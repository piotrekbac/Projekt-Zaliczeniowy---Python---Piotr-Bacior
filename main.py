from src.calculator import calculate_bmi    # Importujemy funkcję calculate_bmi z modułu calculator

# Główna funkcja programu, która będzie wywoływana podczas uruchamiania skryptu
def main():

    """
    Punkt wejścia programu Kalkulatora BMI

    Oczekiwane dane wejściowe:
    - Brak bezpośrednich argumentów funkcji (na razie dane wpisywane będą na sztywno
      w kodzie - docelowo będziemy je pobierać z klawiatury)

    Zachowanie funkcji:
    - Wyświetla interfejs powitalny dla użytkownika w konsoli
    - Wywołuje funkcję obliczającą BMI z podanymi parametrami
    - Formatuje i wyświetla wynik obliczeń BMI w czytelny sposób na ekranie

    Ograniczenia:
    - Funkcja przeznaczoa jest do działania w środowisku konsolowym
    
    """

    print("=" * 30)                                                             
    print("Witaj w Kalkulatorze BMI!")
    print("Autor programu: Piotr Bacior - 15 722 - 2026")
    print("Oblicz swoje BMI, podając wagę w kilogramach i wzrost w metrach.")
    print("=" * 30)

    waga = 70.0               # Przykładowa waga w kilogramach (float)
    wzrost = 1.75             # Przykładowy wzrost w metrach (float)


    # Wywołujemy funkcję calculate_bmi i obsługujemy potencjalne wyjątki, które mogą wystąpić podczas obliczeń
    try:
        moje_bmi = calculate_bmi(waga, wzrost)   # Wywołujemy funkcję calculate_bmi z przykładowymi danymi

    


