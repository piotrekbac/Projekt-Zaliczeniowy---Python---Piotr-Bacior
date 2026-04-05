from src.calculator import calculate_bmi, calculate_ideal_weight            # Importujemy funkcję calculate_bmi z modułu calculator
from src.analyzer import analyze_bmi                # Importujemy funkcję analyze_bmi z modułu analyzer
from src.file_handler import save_result_to_file    # Importujemy funkcję save_result_to_file z modułu file_handler

# Piotr Bacior - 15 722 - 2026 - Python - MH

# Główna funkcja programu, która będzie wywoływana podczas uruchamiania skryptu
def main():

    """
    Punkt wejścia programu Kalkulatora BMI
    Pobiera dane od użytkownika, oblicza BMI oraz idealną wagę, wyświetla wyniki i zapisuje je do pliku tekstowego

    Oczekiwane dane wejściowe:
    - Dane wprwadzone przez użytkownika (waga i wzrost) są typu float - z klawiatury
    - Oczekiwane są liczby dodatnie dla wagi i wzrostu
    - Decyzja o kontynuacji działania programu (T/N)

    Zachowanie funkcji:
    - Wyświetla interfejs powitalny dla użytkownika w konsoli
    - Pobiera dane wejściowe od użytkownika (waga i wzrost) - w tym przypadku używamy przykładowych danych
    - Wywołuje funkcje obliczające i analizujące BMI, a następnie wyświetla wyniki w konsoli
    - Wyświetla pełne podsumowanie wyników
    - Działa w nieskończonej pętli, dopóki użytkownik nie zdecyduje o zakończeniu programu (np. poprzez wpisanie 'N' lub 'n')
    - Inteligentnie konwertuje wzrost podany w centymetrach na metry

    Ograniczenia:
    - Funkcja przeznaczoa jest do działania w środowisku konsolowym
    
    Podnoszenie wyjątków:
    - Obsługuje potencjalne wyjątki typu ValueError, które mogą być podniesione przez funkcję calculate_bmi
    - Wyświetla komunikat o błędzie, jeśli dane wejściowe są nieprawidłowe (np. waga lub wzrost mniejsze lub równe 0)

    """

    # Nagłówek powitalny dla użytkownika, informujący o autorze programu i jego funkcjonalności
    print("\n" + "=" * 30 + "")                                                             
    print("Witaj w Kalkulatorze BMI!")
    print("Autor programu: Piotr Bacior - 15 722 - 2026")
    print("Oblicz swoje BMI, podając wagę w kilogramach i wzrost w metrach.")
    print("" + "=" * 30 + "\n")


    # Pętla nieskończona, która pozwala użytkownikowi na wielokrotne obliczanie BMI, dopóki nie zdecyduje o zakończeniu programu
    while True:    

        # Wywołujemy funkcję calculate_bmi i obsługujemy potencjalne wyjątki, które mogą wystąpić podczas obliczeń
        try:

            # Pobieramy wpis od użytkownika i podmieniamy ewentualny przecinek na kropkę - aby umożliwić poprawne przetwarzanie danych typu float
            waga_input = input("Podaj swoją wagę w kilogramach (np. 70.5): ").replace(",", ".")

            # Konwertujemy tekst na liczbę typu float, aby można było przeprowadzić obliczenia BMI
            waga = float(waga_input)

            # Pobieramy wpis od użytkownika i podmieniamy ewentualny przecinek na kropkę - aby umożliwić poprawne przetwarzanie danych typu float
            wzrost_input = input("Podaj swój wzrost w metrach (np. 1.75): ").replace(",", ".")

            # Konwertujemy tekst na liczbę typu float, aby można było przeprowadzić obliczenia BMI
            wzrost = float(wzrost_input)


            # Jeśli użytkownik poda wzrost w centymetrach, konwertujemy go na metry
            if wzrost >= 3.0:
                print(f"Infomracja: Wykryto wzrost podany w centrymetrach ({wzrost} cm). Konwertuję na metry...")
                wzrost = wzrost / 100


            # Wywołujemy funkcję calculate_bmi z przykładowymi danymi
            moje_bmi = calculate_bmi(waga, wzrost)   

            # Wywołujemy funkcję analyze_bmi, aby uzyskać kategorię zdrowotną na podstawie obliczonego BMI
            kategoria = analyze_bmi(moje_bmi)   

            # Wywołujemy funkcję calculate_ideal_weight, aby obliczyć zakres idealnej wagi dla podanego wzrostu
            min_waga, max_waga = calculate_ideal_weight(wzrost)   

            # Wywołujemy funkcję save_result_to_file, aby zapisać wynik obliczeń do pliku tekstowego
            save_result_to_file(waga, wzrost, moje_bmi, kategoria, min_waga, max_waga)


            # Wyświetlamy pełne podsumowanie 

            print("\n" + "=" * 30 + "\n")                                       # Dodajemy odstęp i linię oddzielającą wyniki od reszty interfejsu

            print(f"Twoje BMI wynosi: {moje_bmi}")                              # Wyświetlamy wynik obliczeń BMI
            print(f"Podany wzrost: {wzrost} m, podana waga: {waga} kg")         # Wyświetlamy podane dane wejściowe
            print(f"BMI: {moje_bmi}")                                           # Wyświetlamy BMI
            print(f"Twoja kategoria zdrowotna: {kategoria}")                    # Wyświetlamy kategorię zdrowotną

            # Wyświetlamy zakres idealnej wagi dla podanego wzrostu
            print(f"Zakres idealnej wagi dla Twojego wzrostu: {min_waga} - {max_waga} kg")   

            print("\n" + "=" * 30 + "\n")                                       # Dodajemy linię oddzielającą wyniki od reszty interfejsu


        # Obsługujemy wyjątki typu ValueError, które mogą być podniesione przez funkcję calculate_bmi
        except ValueError as e:     
            print(f"Błąd: {e}")     # Wyświetlamy komunikat o błędzie, jeśli dane wejściowe są nieprawidłowe


        # Ta pętla odpowiada za pytanie użytkownika, czy chce kontynuować działanie programu, czy zakończyć 
        while True:

            # Pytamy użytkownika, czy chce kontynuować działanie programu, czy zakończyć - usuwamy spacje oraz zmieniamy na małe litery, aby ułatwić porównanie
            wybor = input("Czy chcesz obliczyć BMI ponownie? (T/N): \n").strip().lower()
 
            # Sprawdzamy, czy użytkownik wpisał 'T' lub 'N' (po konwersji na małe litery)
            if wybor == 't' or wybor == 'n':                                                     

                # Jeżeli wpisał t lub n, wychodzimy z tej pętli 
                break                                       

            # W przeciwnym razie, jeżeli wpisał coś innego, wyświetlamy komunikat o błędzie i pytamy ponownie
            else:
                # Jeżeli wpisał coś innego, wyświetlamy komunikat o błędzie i pytamy ponownie
                print("Nieprawidłowy wybór. Proszę wpisać 'T' (tak) lub 'N' (nie).")   

        # Jeżeli użytkownik wpisał 'n' (nie), kończymy działanie programu
        if wybor == 'n':
            print("Dziękujemy za skorzystanie z Kalkulatora BMI. Do zobaczenia!")       # Wyświetlamy komunikat pożegnalny
            break                                                                       # Kończymy działanie programu

        # Jeżeli użytkownik wpisał 't' (tak), kontynuujemy działanie programu (wracamy do początku pętli while True)
        elif wybor == 't':     
            print("\n" + "=" * 30 + "\n")                                       # Dodajemy odstęp i linię oddzielającą wyniki od reszty interfejsu
            print("Nowe obliczenie BMI")                                        # Informujemy użytkownika, że rozpoczynamy nowe obliczenie BMI
            print("\n" + "=" * 30 + "\n")                                       # Dodajemy odstęp i linię oddzielającą wyniki od reszty interfejsu

# Uruchamiamy główną funkcję programu
if __name__ == "__main__":
    main()          