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
wage = st.sidebar.number_input("Waga (kg)", min_value=20.0, max_value=300.0, value=70.0, step=0.5)    

# Pole do wprowadzania wzrostu użytkownika w metrach
wzrost = st.sidebar.number_input("Wzrost (m)", min_value=1.0, max_value=2.5, value=1.75, step=0.01)