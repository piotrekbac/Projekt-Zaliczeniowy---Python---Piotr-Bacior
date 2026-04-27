from fpdf import FPDF               # Importujemy klasę FPDF z biblioteki fpdf, która służy do generowania plików PDF
import os                           # Importujemy moduł os, który pozwala na interakcję z systemem plików (np. sprawdzanie istnienia pliku, usuwanie pliku)
from datetime import datetime       # Importujemy klasę datetime z modułu datetime, która pozwala na pracę z datami i czasem

# Piotr Bacior - 15 722 - 2026 - Python - MH

# 
def remove_polish_accents(text: str) -> str : 

     """ Funkcja pomocnicza usuwająca polskie znaki dla standardowych czcionek PDF. """