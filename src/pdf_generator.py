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
    
    # Iterujemy przez słownik znaków i zastępujemy je w tekście
    for k, v in accents.items() :

        # Zastępujemy wszystkie wystąpienia klucza (polskiego znaku) w tekście jego wartością (znakiem bez akcentu)
        text = text.replace(k, v)

    # Zwracamy przetworzony tekst, który nie zawiera polskich znaków, co pozwala na poprawne wyświetlanie w PDF
    return text


# Definiuję funkcję do generowania pliku PDF z analizą BMI - dane wejściowe są typu str, oczekujemy wyniku typu None (funkcja nie zwraca wartości)
def generate_pdf_report(waga: float, wzrost: float, bmi: float, kategoria: str, tdee: float, bialko: int, tluszcze: int, wegle: int, cel: str, filename: str = "Raport_Dietetyczny.pdf") -> None :

    """
    Generuje profesjonalny raport PDF z wynikami i wykresem.

    """

    # Sprawdzamy, czy plik o podanej nazwie już istnieje, aby uniknąć nadpisania istniejącego raportu
    pdf = FPDF()

    # Dodajemy nową stronę do dokumentu PDF
    pdf.add_page()  

    # Ustawiamy czcionkę Arial o rozmiarze 12 dla całego dokumentu
    pdf.set_font("Arial", size=12)  


    # Sekcja nagłówka raportu - dodajemy tytuł i datę wygenerowania raportu

    # Ustawiamy czcionkę Arial Bold o rozmiarze 16 dla tytułu
    pdf.set_font("Arial", 'B', 16)          

    # Dodajemy tytuł raportu, usuwając polskie znaki, aby zapewnić poprawne wyświetlanie w PDF
    pdf.cell(200, 10, txt=remove_polish_accents("RAPORT DIETETYCZNY - ASYSTENT ZDROWIA"), ln=True, align='C')

    # Ustawiamy czcionkę Arial Italic o rozmiarze 10 dla daty
    pdf.set_font("Arial", 'I', 10)

    # Pobieramy aktualną datę i czas, formatując ją jako string
    data_pomiaru = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  

    # Dodajemy datę pomiaru do raportu, usuwając polskie znaki, aby zapewnić poprawne wyświetlanie w PDF
    pdf.cell(200, 10, txt=remove_polish_accents(f"Data pomiaru: {data_pomiaru}"), ln=True, align='C')

    # Dodajemy odstęp między nagłówkiem a treścią raportu
    pdf.ln(10)  


    # Sekcja z wynikami - dodajemy szczegółowe informacje o pomiarach i zaleceniach

    # Ustawiamy czcionkę Arial Bold o rozmiarze 12 dla nagłówków sekcji
    pdf.set_font("Arial", "B", 12)          

    # Dodajemy nagłówek dla sekcji z wynikami, usuwając polskie znaki, aby zapewnić poprawne wyświetlanie w PDF
    pdf.cell(200, 10, txt=remove_polish_accents("2. Zapotrzebowanie i Makroskladniki:"), ln=True)

    # Ustawiamy czcionkę Arial o rozmiarze 12 dla treści sekcji
    pdf.set_font("Arial", size=12)

    # Dodajemy szczegółowe informacje o zapotrzebowaniu kalorycznym i makroskładnikach, usuwając polskie znaki, aby zapewnić poprawne wyświetlanie w PDF
    pdf.cell(200, 8, txt=remove_polish_accents(f"Cel diety: {cel.upper()}"), ln=True)

    # Dodajemy szczegółowe informacje o zapotrzebowaniu kalorycznym i makroskładnikach, usuwając polskie znaki, aby zapewnić poprawne wyświetlanie w PDF
    pdf.cell(200, 8, txt=remove_polish_accents(f"Zalecane kalorie: {tdee} kcal"), ln=True)

    # Dodajemy szczegółowe informacje o zapotrzebowaniu kalorycznym i makroskładnikach, usuwając polskie znaki, aby zapewnić poprawne wyświetlanie w PDF
    pdf.cell(200, 8, txt=remove_polish_accents(f"-> Bialko: {bialko} g"), ln=True)

    # Dodajemy szczegółowe informacje o zapotrzebowaniu kalorycznym i makroskładnikach, usuwając polskie znaki, aby zapewnić poprawne wyświetlanie w PDF
    pdf.cell(200, 8, txt=remove_polish_accents(f"-> Tluszcze: {tluszcze} g"), ln=True)