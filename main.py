from src.calculator import calculate_bmi      # Importujemy funkcję calculate_bmi z modułu calculator
from src.analyzer import analyze_bmi          # Importujemy funkcję analyze_bmi z modułu analyzer

# Główna funkcja programu, która będzie wywoływana podczas uruchamiania skryptu
def main():

    """
    Punkt wejścia programu Kalkulatora BMI

    Oczekiwane dane wejściowe:
    - Dane wprwadzone przez użytkownika (waga i wzrost) są typu float - z klawiatury
    - Oczekiwane są liczby dodatnie dla wagi i wzrostu

    Zachowanie funkcji:
    - Wyświetla interfejs powitalny dla użytkownika w konsoli
    - Pobiera dane wejściowe od użytkownika (waga i wzrost) - w tym przypadku używamy przykładowych danych
    - Wywołuje funkcje obliczające i analizujące BMI, a następnie wyświetla wyniki w konsoli
    - Wyświetla pełne podsumowanie wyników

    Ograniczenia:
    - Funkcja przeznaczoa jest do działania w środowisku konsolowym
    
    Podnoszenie wyjątków:
    - Obsługuje potencjalne wyjątki typu ValueError, które mogą być podniesione przez funkcję calculate_bmi
    - Wyświetla komunikat o błędzie, jeśli dane wejściowe są nieprawidłowe (np. waga lub wzrost mniejsze lub równe 0)

    """

    # Nagłówek powitalny dla użytkownika, informujący o autorze programu i jego funkcjonalności
    print("=" * 30)                                                             
    print("Witaj w Kalkulatorze BMI!")
    print("Autor programu: Piotr Bacior - 15 722 - 2026")
    print("Oblicz swoje BMI, podając wagę w kilogramach i wzrost w metrach.")
    print("=" * 30)


    # Wywołujemy funkcję calculate_bmi i obsługujemy potencjalne wyjątki, które mogą wystąpić podczas obliczeń
    try:

        # Pobieramy wpis od użytkownika i podmieniamy ewentualny przecinek na kropkę - aby umożliwić poprawne przetwarzanie danych typu float
        waga_input = input("Podaj swoją wagę w kilogramach (np. 70.5): ").replace(",", ".")

        # Konwertujemy tekst na liczbę typu float, aby można było przeprowadzić obliczenia BMI
        waga = float(waga_input)

        # Wywołujemy funkcję calculate_bmi z przykładowymi danymi
        moje_bmi = calculate_bmi(waga, wzrost)   

        print(f"Twoje BMI wynosi: {moje_bmi}")                          # Wyświetlamy wynik obliczeń BMI
        print(f"Podany wzrost: {wzrost} m, podana waga: {waga} kg")     # Wyświetlamy podane dane wejściowe
    

    # Obsługujemy wyjątki typu ValueError, które mogą być podniesione przez funkcję calculate_bmi
    except ValueError as e:     
        print(f"Błąd: {e}")     # Wyświetlamy komunikat o błędzie, jeśli dane wejściowe są nieprawidłowe


# Uruchamiamy główną funkcję programu
if __name__ == "__main__":
    main()          