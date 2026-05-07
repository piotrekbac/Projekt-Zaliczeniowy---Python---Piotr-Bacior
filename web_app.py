import streamlit as st                                                          # importuję bibliotekę streamlit do tworzenia interfejsu webowego 
import pandas as pd                                                             # importuję bibliotekę pandas do manipulacji danymi
import matplotlib.pyplot as plt                                                 # importuję bibliotekę matplotlib do tworzenia wykresów
import os                                                                       # importuję moduł os do operacji na plikach i ścieżkach


# Importowanie funkcji z modułów src.calculator, src.analyzer i src.prediction

# importuję funkcje z modułu calculator
from src.calculator import calculate_bmi, calculate_ideal_weight_range, calculate_weight_difference, calculate_bmr, calculate_tdee, calculate_macros  

# importuję funkcje analyze_bmi i calculate_weight_difference z modułu analyzer
from src.analyzer import analyze_bmi, calculate_weight_difference                               

# importuję funkcję predict_goal_date z modułu prediction
from src.prediction import predict_goal_date                                                        


# Piotr Bacior - 15 722 - 2026 - Python - MH


# Konfiguracja strony Streamlit - ustawiam tytuł, ikonę i układ strony
st.set_page_config(page_title="Asystent zdrowia AI - PB2026", page_icon="🍏", layout="wide")

# Wyświetlam tytuł aplikacji na stronie
st.title("Interaktywny Asystent Zdrowia i Kalkulator BMI")    

# Wyświetlam krótki opis aplikacji, informując użytkownika o jej funkcjonalnościach i możliwościach
st.markdown("Wersja przeglądarkowa projektu oparta na silniku Python Data Science.")


# Sekcja panelu bocznego (sidebar) - służy do wprowadzania danych przez użytkownika, takich jak waga, wzrost, wiek, płeć i poziom aktywności fizycznej

# Nagłówek sekcji bocznej
st.sidebar.header("Wprowadź swoje dane")    

# Pole do wprowadzania wagi użytkownika w kilogramach
waga = st.sidebar.number_input("Waga (kg)", min_value=20.0, max_value=300.0, value=70.0, step=0.5)    

# Pole do wprowadzania wzrostu użytkownika w metrach
wzrost = st.sidebar.number_input("Wzrost (m)", min_value=1.0, max_value=2.5, value=1.75, step=0.01)

# Pole do wprowadzania wieku użytkownika w latach
wiek = st.sidebar.number_input("Wiek (lata)", min_value=10, max_value=120, value=30, step=1)    

# Pole do wyboru płci użytkownika (Mężczyzna lub Kobieta)
plec = st.sidebar.selectbox("Płeć", options=["Mężczyzna", "Kobieta"])    

# Skrót płci do dalszych obliczeń (m dla mężczyzny, k dla kobiety)
plec_skrot = "m" if plec == "Mężczyzna" else "k"    


# Tworzymy słownik z poziomami aktywności fizycznej i odpowiadającymi im współczynnikami, które będą używane do obliczeń TDEE

aktywnosc_dict = {
    "1. Siedzący tryb": 1,                  # 1. Siedzący tryb - brak aktywności fizycznej lub bardzo mała aktywność (np. praca biurowa, brak regularnych ćwiczeń)
    "2. Lekko aktywny": 2,                  # 2. Lekko aktywny - lekka aktywność fizyczna (np. lekkie ćwiczenia 1-3 dni w tygodniu)
    "3. Umiarkowanie aktywny": 3,           # 3. Umiarkowanie aktywny - umiarkowana aktywność fizyczna (np. umiarkowane ćwiczenia 3-5 dni w tygodniu)
    "4. Bardzo aktywny": 4,                 # 4. Bardzo aktywny - duża aktywność fizyczna (np. intensywne ćwiczenia 6-7 dni w tygodniu)
    "5. Ekstremalnie aktywny": 5            # 5. Ekstremalnie aktywny - bardzo duża aktywność fizyczna (np. bardzo intensywne ćwiczenia codziennie, praca fizyczna)
}


# Pole do wyboru poziomu aktywności fizycznej z listy opcji
aktywnosc_wybor = st.sidebar.selectbox("Poziom aktywności fizycznej", options=list(aktywnosc_dict.keys()))    

# Pobieramy współczynnik aktywności fizycznej na podstawie wyboru użytkownika
aktywnosc = aktywnosc_dict[aktywnosc_wybor]    


# -- Przycisk startowy --

# Po kliknięciu przycisku "Oblicz i analizuj" rozpoczynamy proces obliczeń i analizy danych wprowadzonych przez użytkownika
if st.sidebar.button("Oblicz i analizuj", use_container_width=True) : 

    # 1. Obliczenia (Back-end)

    # Obliczamy BMI (Body Mass Index) na podstawie wagi i wzrostu użytkownika, korzystając z funkcji calculate_bmi z modułu calculator
    bmi = calculate_bmi(waga, wzrost)

    # Analizujemy kategorię BMI (np. niedowaga, prawidłowa waga, nadwaga, otyłość) korzystając z funkcji analyze_bmi z modułu analyzer
    kategoria = analyze_bmi(bmi)  

    # Obliczamy zakres idealnej wagi na podstawie wzrostu użytkownika, korzystając z funkcji calculate_ideal_weight_range z modułu calculator
    min_w, max_w = calculate_ideal_weight_range(wzrost)  

    # Obliczamy różnicę między aktualną wagą a zakresem idealnej wagi, korzystając z funkcji calculate_weight_difference z modułu calculator
    roznica = calculate_weight_difference(waga, min_w, max_w)  

    # Obliczamy BMR (Basal Metabolic Rate) na podstawie wagi, wzrostu, wieku i płci użytkownika, korzystając z funkcji calculate_bmr z modułu calculator
    bmr = calculate_bmr(waga, wzrost, wiek, plec_skrot)  

    # Obliczamy TDEE (Total Daily Energy Expenditure) na podstawie BMR i poziomu aktywności fizycznej, korzystając z funkcji calculate_tdee z modułu calculator
    tdee = calculate_tdee(bmr, aktywnosc)  


    # Definiujemy cel dietetyczny użytkownika - w tym przypadku jest to "utrzymanie" aktualnej wagi, co oznacza, że użytkownik chce utrzymać swoją obecną wagę bez chęci jej zmiany (ani redukcji, ani zwiększenia)
    cel_dietetyczny = "utrzymanie"
    
    # Kalorie docelowe są równe TDEE, ponieważ celem jest utrzymanie wagi
    docelowe_kcal = tdee  


    # Warunek logiczny do określenia celu dietetycznego na podstawie różnicy wagi 

    # Obsługa logiki dla kategorii "Niedowaga" - jeśli kategoria BMI użytkownika to "Niedowaga", to celem dietetycznym będzie "zwiększenie masy ciała", a docelowe kalorie będą równe TDEE plus 500 kcal, co oznacza, że użytkownik powinien spożywać więcej kalorii niż wynosi jego całkowite dzienne zapotrzebowanie energetyczne, aby zwiększyć swoją masę ciała
    if kategoria == "Niedowaga" : 

        # Definiujemy cel dietetyczny jako "zwiększenie masy ciała"
        cel_dietetyczny = "masa"

        # Dodajemy 500 kcal do TDEE, aby określić docelowe kalorie dla zwiększenia masy ciała, zaokrąglając wynik do 2 miejsc po przecinku
        docelowe_kcal = round(tdee + 500, 2)  


    # Obsługa logiki dla kategorii "Nadwaga" i "Otyłość" - jeśli kategoria BMI użytkownika to "Nadwaga" lub "Otyłość", to celem dietetycznym będzie "redukcja masy ciała", a docelowe kalorie będą równe TDEE minus 500 kcal, co oznacza, że użytkownik powinien spożywać mniej kalorii niż wynosi jego całkowite dzienne zapotrzebowanie energetyczne, aby zredukować swoją masę ciała
    elif kategoria in['Nadwaga', 'Otyłość'] :

        # Definiujemy cel dietetyczny jako "redukcja masy ciała"
        cel_dietetyczny = "redukcja"

        # Odejmujemy 500 kcal od TDEE, aby określić docelowe kalorie dla redukcji masy ciała, zaokrąglając wynik do 2 miejsc po przecinku
        docelowe_kcal = round(tdee - 500, 2)   


        # Dodatkowo obsługujemy wyjątkowo kategorie "Otyłość" - jeśli kategoria BMI użytkownika to "Otyłość", to celem dietetycznym będzie "intensywna redukcja masy ciała", a docelowe kalorie będą równe TDEE minus 1000 kcal, co oznacza, że użytkownik powinien spożywać znacznie mniej kalorii niż wynosi jego całkowite dzienne zapotrzebowanie energetyczne, aby osiągnąć intensywną redukcję masy ciała
        if kategoria == "Otyłość" : 

            # Definiujemy cel dietetyczny jako "intensywna redukcja masy ciała"
            docelowe_kcal = round(tdee - 650, 2)


        # Obliczamy rozkład makroskładników (białka, tłuszcze, węglowodany) na podstawie docelowych kalorii i celu dietetycznego, korzystając z funkcji calculate_macros z modułu calculator
        bialo, tluszcze, wegle = calculate_macros(docelowe_kcal, cel_dietetyczny)  


        # 2. Wyświetlenie w głównym oknie - Front-end - prezentacja wyników obliczeń i analizy danych wprowadzonych przez użytkownika

        # Tworzymy 3 kolumny na ładne widgety z wynikami obliczeń
        col1, col2, col3 = st.columns(3)

        # Wyświetlamy wskaźnik BMI wraz z jego kategorią (np. Niedowaga, Prawidłowa waga, Nadwaga, Otyłość)
        col1.metric("Wskaźnik BMI", f"{bmi:.1f}", kategoria)    

        # Wyświetlamy zakres idealnej wagi wraz z różnicą między aktualną wagą a zakresem idealnej wagi
        col1.metric("Idealna waga (kg)", f"{min_w:.1f} - {max_w:.1f}", f"Różnica: {roznica:.1f} kg")    

        # Wyświetlamy BMR (Basal Metabolic Rate) - podstawową przemianę materii, czyli ilość kalorii, jaką organizm potrzebuje do podtrzymania podstawowych funkcji życiowych w spoczynku
        col2.metric("Idealna waga (kg)", f"{min_w:.1f} - {max_w:.1f}", f"Różnica: {roznica:.1f} kg")    

        # Wyświetlamy TDEE (Total Daily Energy Expenditure) - całkowite dzienne zapotrzebowanie energetyczne, czyli ilość kalorii, jaką organizm potrzebuje do utrzymania aktualnej wagi przy uwzględnieniu poziomu aktywności fizycznej
        col2.metric("Tdee (kcal)", f"{tdee:.0f}", f"Docelowe kcal: {docelowe_kcal:.0f}")        


        # Dodajemy poziomą linię oddzielającą sekcje
        st.divider()    


        # Wyświetlamy podtytuł dla sekcji planu dietetycznego
        st.subheader("Twój plan dietetyczny")       

        # Wyświetlamy informacje o celu dietetycznym użytkownika oraz zalecanym spożyciu kalorii na dzień, korzystając z funkcji st.info do wyróżnienia tej informacji
        st.info(f"**Cel:** {cel_dietetyczny.upper()} | **Zalecane spożycie:** {docelowe_kcal} kcal / dzień")


        # Tworzymy 3 kolumny na ładne widgety z wynikami obliczeń
        c1, c2, c3 = st.columns(3)

        c1.success(f"**Białko:** {bialo} g / dzień")                # Wyświetlamy zalecane spożycie białka w gramach na dzień
        c2.success(f"**Tłuszcze:** {tluszcze} g / dzień")           # Wyświetlamy zalecane spożycie tłuszczów w gramach na dzień
        c3.success(f"**Węglowodany:** {wegle} g / dzień")           # Wyświetlamy zalecane spożycie węglowodanów w gramach na dzień


        # Dodajemy poziomą linię oddzielającą sekcje
        st.divider()    


        # Sekcja Wykresu oraz Algorytmu ai - prezentacja graficzna danych oraz prognozowanie daty osiągnięcia celu dietetycznego

        # Wyświetlamy podtytuł dla sekcji analizy danych i AI
        st.subheader("Analiza danych i AI")       

        # Sprawdzamy czy istnieje plik "bmi_history.csv" - jeśli tak, to wczytujemy dane z tego pliku do DataFrame'a, wyświetlamy historię BMI użytkownika oraz generujemy wykres słupkowy przedstawiający zmiany BMI na przestrzeni czasu, korzystając z funkcji generate_bmi_bar z modułu analyzer
        if os.path.exists("bmi_history.csv") : 

            # Obliczamy środek normy idealnej wagi, który będzie używany do generowania wykresu słupkowego
            srodek_normy = round((min_w + max_w) / 2, 1)    
            
            # Prognozujemy datę osiągnięcia celu dietetycznego na podstawie historii BMI, aktualnego BMI i środka normy idealnej wagi, korzystając z funkcji predict_goal_date z modułu prediction
            prognoza = predict_goal_date("bmi_history.csv", bmi, srodek_normy)    

            # Wyświetlamy nagłówek dla sekcji predykcji AI
            st.markdown(f"**Predykcja AI: ** {prognoza}")    


            # Wyciągamy dane z pliku "bmi_history.csv" do DataFrame'a, konwertujemy kolumnę "date" na format daty, a kolumnę "bmi" na wartości numeryczne, aby przygotować dane do analizy i wizualizacji

            # Wczytujemy dane z pliku "bmi_history.csv" do DataFrame'a, który będzie zawierał historię BMI użytkownika wraz z datami pomiarów
            df = pd.read_csv("historia_bmi.csv", sep=";")

            # Konwertujemy kolumnę "Data i czas" na format daty i czasu, aby umożliwić analizę zmian BMI na przestrzeni czasu oraz generowanie wykresów z odpowiednią osi czasu
            df['Data i czas'] = pd.to_datetime(df['Data i czas'])


            # Tworzymy wykres o określonym rozmiarze (10 cali szerokości i 4 cali wysokości)
            fig, ax = plt.subplots(figsize=(10, 4))    

            # Rysujemy wykres liniowy przedstawiający zmiany wagi użytkownika na przestrzeni czasu, gdzie oś X reprezentuje daty pomiarów, a oś Y reprezentuje wagę w kilogramach. Dodajemy marker "o" dla każdego punktu danych, ustawiamy kolor linii na "royalblue", styl linii na "-", oraz grubość linii na 2, aby wizualnie wyróżnić zmiany wagi użytkownika na wykresie
            ax.plot(df['Data i czas'], df['Waga (kg)'], marker='o', color='royalblue', linestyle='-', linewidth=2)

            # Ustawiamy tytuł wykresu na "Historia Twojej Wagi" z czcionką o rozmiarze 14, aby jasno określić, że wykres przedstawia historię zmian wagi użytkownika na przestrzeni czasu
            ax.set_title("Historia Twojej Wagi", fontsize=14)

            # Ustawiamy etykietę osi X na "Data i czas", aby wskazać, że oś X reprezentuje daty i czasy pomiarów wagi użytkownika
            ax.set_ylabel("Waga (kg)")

            # Ustawiamy grid dla wykresu, aby ułatwić odczyt wartości z osi Y, korzystając z linii przerywanych ("--") o kolorze szarym i przezroczystości 0.7, co poprawia czytelność wykresu i umożliwia łatwiejsze porównanie zmian wagi użytkownika na przestrzeni czasu.
            ax.grid(True, linestyle='--', alpha=0.7)


            # Renderowanie wykresu z matplotlib do Streamlit


            # Wyświetlamy wykres w aplikacji Streamlit, korzystając z funkcji st.pyplot, która umożliwia renderowanie wykresów stworzonych za pomocą biblioteki matplotlib bezpośrednio w interfejsie użytkownika, co pozwala na wizualizację historii zmian wagi użytkownika na przestrzeni czasu.
            st.pyplot(fig)


        # Jeśli plik "bmi_history.csv" nie istnieje, wyświetlamy informację dla użytkownika, że historia BMI jest niedostępna, korzystając z funkcji st.warning do wyróżnienia tej informacji
        else : 

            # Wyświetlamy ostrzeżenie, że historia BMI jest niedostępna, ponieważ brak danych do analizy, co informuje użytkownika o braku możliwości przeprowadzenia analizy zmian BMI na przestrzeni czasu z powodu braku danych historycznych
            st.warning("Brak pliku CSV z historią pomiarów do wygenerowania wykresu i predykcji.")

    # Jeśli użytkownik nie kliknął przycisku "Oblicz i analizuj", wyświetlamy informację, że należy wprowadzić dane i kliknąć przycisk, aby rozpocząć proces obliczeń i analizy, korzystając z funkcji st.info do wyróżnienia tej informacji
    else : 

        # Wyświetlamy informację, że należy wprowadzić dane i kliknąć przycisk "Oblicz i analizuj", aby zobaczyć wyniki i analizę, co zachęca użytkownika do interakcji z aplikacją i rozpoczęcia procesu obliczeń oraz analizy danych wprowadzonych przez niego
        st.write("Wypełnij swoje parametry w panelu bocznym po lewej stronie i kliknij **Oblicz i Analizuj**.")