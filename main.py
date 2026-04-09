from src.calculator import calculate_bmi, calculate_ideal_weight, calculate_bmr, calculate_tdee         # Importujemy funkcję calculate_bmi z modułu calculator
from src.analyzer import analyze_bmi, generate_bmi_bar                                                  # Importujemy funkcję analyze_bmi z modułu analyzer
from src.file_handler import save_result_to_file, read_history_from_file, save_to_csv                   # Importujemy funkcję save_result_to_file z modułu file_handler
from src.charts import show_bmi_trend_chart                                                             # Importujemy funkcję show_bmi_trend_chart z modułu charts

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
    print("\n" + "=" * 70 + "")   

    # Przesuwamy tekst do środka, aby był bardziej estetyczny i czytelny dla użytkownika w konsoli
    print(f"{'Witaj w Kalkulatorze BMI!':^70}")
    print(f"{'Autor programu: Piotr Bacior - 15 722 - 2026':^70}")
    print(f"{'Oblicz swoje BMI, podając wagę w kilogramach i wzrost w metrach.':^70}")

    print("" + "=" * 70 + "\n")


    # Pytamy użytkownika, czy chce zobaczyć historię swoich pomiarów BMI, i przechowujemy jego odpowiedź w zmiennej 'czy_historia'

    czy_historia = input("Czy chcesz zobaczyć historię swoich pomiarów BMI? (T/N): ").strip().lower()    
            
    if czy_historia == 't':                                 # Sprawdzamy, czy użytkownik wpisał 'T' (tak)
        historia = read_history_from_file()                 # Wywołujemy funkcję read_history_from_file, aby odczytać historię pomiarów z pliku tekstowego                                                   

        print("\n" + "-" * 60)
        print(f"{'Historia Twoich pomiarów BMI:':^60}")     # Wyświetlamy nagłówek dla historii pomiarów BMI
        print("-" * 60 + "\n")

        # Sprawdzamy, czy historia pomiarów jest pusta (brak zapisanych pomiarów) i wyświetlamy odpowiedni komunikat
        if not historia:
            
            print("Brak zapisanych pomiarów BMI. Zacznij obliczać swoje BMI, aby zobaczyć historię pomiarów!")

        # Jeżeli historia pomiarów nie jest pusta, wyświetlamy każdy zapisany pomiar BMI, usuwając ewentualne białe znaki z początku i końca linii
        else:
            for linia in historia:
                print(linia.strip())


        # Pytamy użytkownika, czy chce zobaczyć wykres trendu swoich pomiarów BMI, i przechowujemy jego odpowiedź w zmiennej 'czy_wykres'
        czy_wykres = input("\nCzy chcesz zobaczyć wykres trendu swoich pomiarów BMI? (T/N): ").strip().lower()    

        if czy_wykres == 't':                                           # Sprawdzamy, czy użytkownik wpisał 'T' (tak)
            print("\nGeneruję wykres trendu Twoich pomiarów BMI...")    # Informujemy użytkownika, że generujemy wykres trendu BMI
            show_bmi_trend_chart()                                      # Wywołujemy funkcję show_bmi_trend_chart, aby wygenerować i wyświetlić wykres trendu BMI

            # Po wygenerowaniu wykresu, informujemy użytkownika, że wykres został wygenerowany i można go zobaczyć w nowym oknie
            print("\nWykres trendu BMI został wygenerowany. Możesz go zobaczyć w nowym oknie.")   


        # Dodajemy odstęp i linię oddzielającą historię pomiarów od reszty interfejsu
        print("\n" + "-" * 60 + "\n")    


    # Pętla nieskończona, która pozwala użytkownikowi na wielokrotne obliczanie BMI, dopóki nie zdecyduje o zakończeniu programu
    while True:    

        # Wypisujemy w konsoli komunikat o podaniu danych wejściowych (waga i wzrost) przez użytkownika, które będą używane do obliczenia BMI
        print("\n" + "=" * 60 + "\n")                                       # Dodajemy odstęp i linię oddzielającą wyniki od reszty interfejsu
        print("Podaj swoje dane, aby obliczyć BMI:")                        # Wyświetlamy komunikat o podaniu danych wejściowych 
        print("\n" + "=" * 60 + "\n")                                       # Dodajemy odstęp i linię oddzielającą wyniki od reszty interfejsu

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
                print(f"Informacja: Wykryto wzrost podany w centrymetrach ({wzrost} cm). Konwertuję na metry...")
                wzrost = wzrost / 100

            # Pobieramy wpis od użytkownika i podmieniamy ewentualny przecinek na kropkę - aby umożliwić poprawne przetwarzanie danych typu float
            wiek_input = input("Podaj swój wiek w latach (np. 30): ").replace(",", ".")   

            # Konwertujemy tekst na liczbę typu int, aby można było przeprowadzić obliczenia BMR i TDEE
            wiek = int(wiek_input)   

            # Pobieramy wpis od użytkownika i usuwamy ewentualne spacje oraz konwertujemy na małe litery, aby ułatwić porównanie
            plec = input("Podaj swoją płeć (M/K): ").strip().lower() 

            # Wypisujemy w konsoli odpowiednie komunikaty informujące o poziomach aktywności fizycznej, które użytkownik może wybrać, aby obliczyć swoje TDEE
            print('\n-- Poziomy aktywności fizycznej --\n')  
            print('1. Siedzący tryb życia (brak lub minimalna aktywność fizyczna)')
            print('2. Lekko aktywny (lekkie ćwiczenia/sport 1-3 dni w tygodniu)')
            print('3. Umiarkowanie aktywny (umiarkowane ćwiczenia/sport 3-5 dni w tygodniu)')
            print('4. Bardzo aktywny (intensywne ćwiczenia/sport 6-7 dni w tygodniu)')
            print('5. Ekstremalnie aktywny (bardzo intensywne ćwiczenia/sport, praca fizyczna lub trening dwa razy dziennie)\n')
            
            # Pobieramy wpis od użytkownika i usuwamy ewentualne spacje
            aktywnosc_input = input("\nWybierz poziom swojej aktywności fizycznej (1-5): ").strip()  

            # Konwertujemy tekst na liczbę typu int, aby można było przeprowadzić obliczenia TDEE
            aktywnosc = int(aktywnosc_input)

            # Wywołujemy funkcję calculate_bmi z przykładowymi danymi
            moje_bmi = calculate_bmi(waga, wzrost)   

            # Wywołujemy funkcję analyze_bmi, aby uzyskać kategorię zdrowotną na podstawie obliczonego BMI
            kategoria = analyze_bmi(moje_bmi)   

            # Wywołujemy funkcję calculate_ideal_weight, aby obliczyć zakres idealnej wagi dla podanego wzrostu
            min_waga, max_waga = calculate_ideal_weight(wzrost)   

            # Tworzymy graficzny pasek wizualizujący wartość BMI, wywołując funkcję generate_bmi_bar z modułu analyzer
            pasek_wizualny = generate_bmi_bar(moje_bmi)

            # Wywołujemy funkcję calculate_bmr, aby obliczyć podstawową przemianę materii (BMR) na podstawie wagi, wzrostu, wieku i płci
            bmr = calculate_bmr(waga, wzrost, wiek, plec)   

            # Wywołujemy funkcję calculate_tdee, aby obliczyć całkowite dzienne zapotrzebowanie kaloryczne (TDEE) na podstawie obliczonego BMR i poziomu aktywności fizycznej
            tdee = calculate_tdee(bmr, aktywnosc)

            # Wywołujemy funkcję save_result_to_file, aby zapisać wynik obliczeń do pliku tekstowego
            save_result_to_file(waga, wzrost, moje_bmi, kategoria, min_waga, max_waga)

            # Wywołujemy funkcję save_to_csv, aby zapisać wynik obliczeń do pliku CSV
            save_to_csv(waga, wzrost, moje_bmi, kategoria, min_waga, max_waga)

            # Wyświetlamy pełne podsumowanie 

            print("\n" + "=" * 60 + "\n")                                       # Dodajemy odstęp i linię oddzielającą wyniki od reszty interfejsu

            print(f"Podany wzrost: {wzrost} m, podana waga: {waga} kg")         # Wyświetlamy podane dane wejściowe
            print(f"BMI: {moje_bmi}")                                           # Wyświetlamy BMI
            print(f"Twoja kategoria zdrowotna: {kategoria}")                    # Wyświetlamy kategorię zdrowotną

            # Wyświetlamy zakres idealnej wagi dla podanego wzrostu
            print(f"Zakres idealnej wagi dla Twojego wzrostu: {min_waga} - {max_waga} kg")   

            print("\n" + "=" * 60 + "\n")                                       # Dodajemy linię oddzielającą wyniki od reszty interfejsu

            # Wyświetlamy graficzny pasek wizualizujący wartość BMI
            print("Wizualizacja Twojego BMI na skali:")
            print(pasek_wizualny)                                               # Wyświetlamy graficzny pasek wizualizujący wartość BMI
            print("      (Niedowaga | Norma | Nadwaga | Otyłość)")
            print("\n" + "=" * 60 + "\n")                                       # Dodajemy linię oddzielającą wyniki od reszty interfejsu

            # Wyświetlamy obliczone BMR i TDEE
            print("-- Twoje zapotrzebowanie kaloryczne --\n")
            print(f"Podstawowa przemiana materii (BMR): {bmr} kcal")
            print(f"Całkowite dzienne zapotrzebowanie (TDEE): {tdee} kcal")

            # Porady dietetyczne na podstawie kategorii zdrowotnej
            print("\n -- Porady dietetyczne --\n")


            # Wyświetlamy odpowiednie porady dietetyczne w zależności od kategorii zdrowotnej, do której należy użytkownik

            # Porady dla kategorii "Niedowaga"
            if kategoria == "Niedowaga":

                # Wyświetlamy porady dla osób z niedowagą, które mają na celu pomóc im przybrać na wadze w zdrowy sposób
                print(f"Aby przybrać na wadze jedz około {tdee + 500} kcal dziennie (+500 kcal).")

            # Porady dla kategorii "Nadwaga"
            elif kategoria == "Nadwaga":

                # Wyświetlamy porady dla osób z nadwagą, które mają na celu pomóc im schudnąć w zdrowy sposób
                print(f"Aby schudnąć jedz około {tdee - 500} kcal dziennie (-500 kcal).")

            # Porady dla kategorii "Otyłość"
            elif kategoria == "Otyłość":

                # Wyświetlamy porady dla osób z otyłością, które mają na celu pomóc im schudnąć w zdrowy sposób
                print(f"Aby schudnąć jedz około {tdee - 650} kcal dziennie (-650 kcal).")
                print("W tym przypadku zalecam konsultację z lekarzem lub dietetykiem, aby opracować bezpieczny i skuteczny plan odchudzania.")
                print("Pamiętaj, że zdrowe odchudzanie to proces stopniowy, a szybka utrata wagi może być niezdrowa i trudna do utrzymania.")

            # Porady dla normy wagowej - nasza waga jest w normie
            else:

                # Wyświetlamy porady dla osób z normą, które mają na celu pomóc im utrzymać zdrową wagę
                print(f"Twoje BMI jest w normie. Aby utrzymać zdrową wagę, jedz tyle kalorii, ile wynosi Twoje TDEE, czyli: {tdee} kcal dziennie.")
                print("Pamiętaj o zrównoważonej diecie i regularnej aktywności fizycznej, aby utrzymać zdrowy styl życia.")


        # Obsługujemy wyjątki typu ValueError, które mogą być podniesione przez funkcję calculate_bmi
        except ValueError as e:     
            print(f"\nBłąd: {e}")           # Wyświetlamy komunikat o błędzie, jeśli dane wejściowe są nieprawidłowe
            print("Spróbuj ponownie.\n")    # Kontynuujemy działanie programu, wracając do początku pętli while True


        # Ta pętla odpowiada za pytanie użytkownika, czy chce kontynuować działanie programu, czy zakończyć 
        while True:

            # Pytamy użytkownika, czy chce kontynuować działanie programu, czy zakończyć - usuwamy spacje oraz zmieniamy na małe litery, aby ułatwić porównanie
            wybor = input("\nCzy chcesz obliczyć BMI ponownie? (T/N): \n").strip().lower()
 
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
            print("\nDziękujemy za skorzystanie z Kalkulatora BMI. Do zobaczenia!")       # Wyświetlamy komunikat pożegnalny
            break                                                                       # Kończymy działanie programu

        # Jeżeli użytkownik wpisał 't' (tak), kontynuujemy działanie programu (wracamy do początku pętli while True)
        elif wybor == 't':     
            print("\n" + "=" * 30 + "\n")                                       # Dodajemy odstęp i linię oddzielającą wyniki od reszty interfejsu
            print("Nowe obliczenie BMI")                                        # Informujemy użytkownika, że rozpoczynamy nowe obliczenie BMI
            print("\n" + "=" * 30 + "\n")                                       # Dodajemy odstęp i linię oddzielającą wyniki od reszty interfejsu


# Uruchamiamy główną funkcję programu
if __name__ == "__main__":
    main()          