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