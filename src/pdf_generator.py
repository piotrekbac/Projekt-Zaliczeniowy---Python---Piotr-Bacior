from fpdf import FPDF               # Importujemy klasę FPDF z biblioteki fpdf, która służy do generowania plików PDF
import os                           # Importujemy moduł os, który pozwala na interakcję z systemem plików (np. sprawdzanie istnienia pliku, usuwanie pliku)
from datetime import datetime       # Importujemy klasę datetime z modułu datetime, która pozwala na pracę z datami i czasem

# Piotr Bacior - 15 722 - 2026 - Python - MH


# Definiuję funkcję do generowania pliku PDF z analizą BMI - dane wejściowe są typu str, oczekujemy wyniku typu None (funkcja nie zwraca wartości)
def remove_polish_accents(text: str) -> str : 

    """ Funkcja pomocnicza usuwająca polskie znaki dla standardowych czcionek PDF. """

    # Tworzymy nowy łańcuch znaków, zastępując polskie znaki ich odpowiednikami bez akcentów
    accents = {'ą':'a', 'ć':'c', 'ę':'e', 'ł':'l', 'ń':'n', 'ó':'o', 'ś':'s', 'ź':'z', 'ż':'z',
            'Ą':'A', 'Ć':'C', 'Ę':'E', 'Ł':'L', 'Ń':'N', 'Ó':'O', 'Ś':'S', 'Ź':'Z', 'Ż':'Z'}
    

    for k, v in accents.items() :
        text = text.replace(k, v)