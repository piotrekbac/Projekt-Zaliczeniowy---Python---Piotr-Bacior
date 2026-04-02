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
    
    Podnoszenie wyjątków:
    - Obsługuje potencjalne wyjątki typu ValueError, które mogą być podniesione przez funkcję calculate_bmi
    - Wyświetla komunikat o błędzie, jeśli dane wejściowe są nieprawidłowe (np. waga lub wzrost mniejsze lub równe 0)

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

        # Wywołujemy funkcję calculate_bmi z przykładowymi danymi
        moje_bmi = calculate_bmi(waga, wzrost)   

        print(f"Twoje BMI wynosi: {moje_bmi}")                          # Wyświetlamy wynik obliczeń BMI
        print(f"Podany wzrost: {wzrost} m, podana waga: {waga} kg")     # Wyświetlamy podane dane wejściowe
    

    # Obsługujemy wyjątki typu ValueError, które mogą być podniesione przez funkcję calculate_bmi
    except ValueError as e:     
        print(f"Błąd: {e}")     # Wyświetlamy komunikat o błędzie, jeśli dane wejściowe są nieprawidłowe

