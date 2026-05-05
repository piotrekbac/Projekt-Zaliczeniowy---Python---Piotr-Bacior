import streamlit as st                                                          # importuję bibliotekę streamlit do tworzenia interfejsu webowego 
import pandas as pd                                                             # importuję bibliotekę pandas do manipulacji danymi
import matplotlib.pyplot as plt                                                 # importuję bibliotekę matplotlib do tworzenia wykresów
import os                                                                       # importuję moduł os do operacji na plikach i ścieżkach


# Importowanie funkcji z modułów src.calculator, src.analyzer i src.prediction

# importuję funkcje z modułu calculator
from src.calculator import calculate_bmi, calculate_ideal_weight_range, calculate_weight_difference, calculate_bmr, calculate_tdee, calculate_macros  

# importuję funkcje analyze_bmi i generate_bmi_bar z modułu analyzer
from src.analyzer import analyze_bmi, generate_bmi_bar                                     

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