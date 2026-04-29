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

# Tworzymy klasę PDF, która dziedziczy po FPDF, co pozwala nam na tworzenie niestandardowych funkcji do generowania raportów PDF z analizą BMI i zaleceniami dietetycznymi
class PDF(FPDF) : 

    # Definiujemy metodę header, która jest wywoływana automatycznie przez FPDF podczas generowania każdej strony PDF, co pozwala nam na dodanie niestandardowego nagłówka do naszego raportu PDF
    def header(self):

        # Kolorowe tło nagłówka (Niebieski)
        self.set_fill_color(41, 128, 185) 

        # Rysujemy prostokąt jako tło nagłówka, który zajmuje całą szerokość strony (210 mm) i ma wysokość 30 mm, wypełniony kolorem ustawionym wcześniej
        self.rect(0, 0, 210, 30, 'F')

        # Tytuł dokumentu

        # Ustawiamy pozycję kursora na współrzędnych y=10, co pozwala nam na umieszczenie tytułu w odpowiednim miejscu na stronie
        self.set_y(10)

        # Ustawiamy czcionkę Arial Bold o rozmiarze 20 dla tytułu, co pozwala na wyróżnienie tytułu raportu PDF i nadanie mu profesjonalnego wyglądu
        self.set_font('Arial', 'B', 20)

        # Ustawiamy kolor tekstu na biały, co zapewnia dobry kontrast z niebieskim tłem nagłówka i poprawia czytelność tytułu raportu PDF
        self.set_text_color(255, 255, 255) 

        # Dodajemy tytuł dokumentu, usuwając polskie znaki, aby zapewnić poprawne wyświetlanie w PDF, i ustawiając go na środku strony (align='C')
        self.cell(0, 10, remove_polish_accents('KARTA PACJENTA - ASYSTENT ZDROWIA'), 0, 1, 'C')

        # Dodajemy odstęp między nagłówkiem a treścią raportu, co poprawia czytelność i estetykę układu strony w raporcie PDF
        self.ln(15)


    # Definiujemy metodę footer, która jest wywoływana automatycznie przez FPDF podczas generowania każdej strony PDF, co pozwala nam na dodanie niestandardowej stopki do naszego raportu PDF
    def footer(self) :

        # Ustawiamy pozycję kursora na 15 mm od dołu strony, co pozwala nam na umieszczenie stopki w odpowiednim miejscu na stronie
        self.set_y(-15)
        
        # Ustawiamy czcionkę Arial Italic o rozmiarze 8 dla stopki, co pozwala na wyróżnienie informacji w stopce i nadanie jej profesjonalnego wyglądu
        self.set_font('Arial', 'I', 8)

        # Ustawiamy kolor tekstu na szary, co zapewnia subtelny wygląd stopki i nie odciąga uwagi od głównej treści raportu PDF
        self.set_text_color(128, 128, 128) 

        # Dodajemy tekst stopki, usuwając polskie znaki, aby zapewnić poprawne wyświetlanie w PDF, i ustawiając go na środku strony (align='C'), co informuje użytkownika o autorze raportu i numerze strony
        self.cell(0, 10, remove_polish_accents(f'Wygenerowano przez: Piotr Bacior (15 722) | Strona {self.page_no()}'), 0, 0, 'C')


# Definiuję funkcję do generowania pliku PDF z analizą BMI - dane wejściowe są typu str, oczekujemy wyniku typu None (funkcja nie zwraca wartości)
def generate_pdf_report(waga: float, wzrost: float, bmi: float, kategoria: str, tdee: float, bialko: int, tluszcze: int, wegle: int, cel: str, filename: str = "Raport_Dietetyczny.pdf") -> None :

    """
    Generuje profesjonalny raport PDF z wynikami i wykresem.

    """

    # Sprawdzamy, czy plik o podanej nazwie już istnieje, aby uniknąć nadpisania istniejącego raportu
    pdf = FPDF()

    # Dodajemy nową stronę do dokumentu PDF
    pdf.add_page()  


    # --- Funkcje pomocnicze do rysowania sekcji ---

    # Definiujemy funkcję section_title, która przyjmuje tytuł sekcji jako argument i dodaje go do raportu PDF z odpowiednim formatowaniem, co pozwala na łatwe tworzenie sekcji w raporcie PDF z analizą BMI i zaleceniami dietetycznymi
    def section_title(title) : 

        # Ustawiamy czcionkę Arial Bold o rozmiarze 14 dla tytułu sekcji, co pozwala na wyróżnienie tytułu sekcji i nadanie mu profesjonalnego wyglądu
        pdf.set_font('Arial', 'B', 14)

        # Ustawiamy jasnoniebieski kolor tła podtekstu sekcji, co poprawia czytelność i estetykę układu strony w raporcie PDF
        pdf.set_fill_color(230, 240, 255)

        # Dodajemy granatowy kolor tekstu dla tytułu sekcji, co zapewnia dobry kontrast z jasnoniebieskim tłem i poprawia czytelność tytułu sekcji w raporcie PDF
        pdf.set_text_color(41, 128, 185)

        # Dodajemy tytuł sekcji, usuwając polskie znaki, aby zapewnić poprawne wyświetlanie w PDF, i ustawiając go na lewej stronie (align='L'), z wypełnieniem tła (fill=1)
        pdf.cell(0, 10, remove_polish_accents(title), 0, 1, 'L', 1)

        # Dodajemy odstęp między tytułem sekcji a treścią sekcji, co poprawia czytelność i estetykę układu strony w raporcie PDF
        pdf.ln(2)

    # Definiujemy funkcję normal_text, która przyjmuje tekst i opcjonalny argument bold, który określa, czy tekst ma być pogrubiony, i dodaje go do raportu PDF z odpowiednim formatowaniem, co pozwala na łatwe dodawanie treści do sekcji w raporcie PDF z analizą BMI i zaleceniami dietetycznymi
    def normal_text(text, bold=False) : 

        # Ustawiamy czcionkę Arial o rozmiarze 12, z opcją pogrubienia, jeśli argument bold jest ustawiony na True, co pozwala na wyróżnienie ważnych informacji w treści sekcji raportu PDF z analizą BMI i zaleceniami dietetycznymi
        pdf.set_font('Arial', 'B' if bold else '', 12)

        # Ustawiamy ciemnoszary kolor tekstu dla treści sekcji, co zapewnia dobry kontrast z białym tłem i poprawia czytelność treści sekcji w raporcie PDF
        pdf.set_text_color(40, 40, 40)

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

    # Dodajemy szczegółowe informacje o zapotrzebowaniu kalorycznym i celach diety, usuwając polskie znaki, aby zapewnić poprawne wyświetlanie w PDF
    pdf.cell(200, 8, txt=remove_polish_accents(f"Cel diety: {cel.upper()}"), ln=True)

    # Dodajemy szczegółowe informacje o zapotrzebowaniu kalorycznym i makroskładnikach, usuwając polskie znaki, aby zapewnić poprawne wyświetlanie w PDF
    pdf.cell(200, 8, txt=remove_polish_accents(f"Zalecane kalorie: {tdee} kcal"), ln=True)

    # Dodajemy szczegółowe informacje o białku, usuwając polskie znaki, aby zapewnić poprawne wyświetlanie w PDF
    pdf.cell(200, 8, txt=remove_polish_accents(f"-> Bialko: {bialko} g"), ln=True)

    # Dodajemy szczegółowe informacje o zapotrzebowaniu na tłuszcze, usuwając polskie znaki, aby zapewnić poprawne wyświetlanie w PDF
    pdf.cell(200, 8, txt=remove_polish_accents(f"-> Tluszcze: {tluszcze} g"), ln=True)

    # Dodajemy szczegółowe informacje o zapotrzebowaniu węglowodanów, usuwając polskie znaki, aby zapewnić poprawne wyświetlanie w PDF
    pdf.cell(200, 8, txt=remove_polish_accents(f"-> Weglowodany: {wegle} g"), ln=True)

    # Dodajemy odstęp między sekcją z wynikami a kolejną sekcją raportu
    pdf.ln(10)


    # Sekcja Wykresu (jeśli istnieje obrazek) - dodajemy wykres BMI do raportu, jeśli plik z wykresem istnieje

    # Ustawiamy czcionkę Arial Bold o rozmiarze 12 dla nagłówka sekcji z wykresem
    pdf.set_font("Arial", 'B', 12)

    # Dodajemy nagłówek dla sekcji z wykresem, usuwając polskie znaki, aby zapewnić poprawne wyświetlanie w PDF
    pdf.cell(200, 10, txt=remove_polish_accents("3. Historia Twojej wagi:"), ln=True)

    # Sprawdzamy, czy plik z wykresem istnieje, aby uniknąć błędów podczas dodawania obrazu do PDF
    if os.path.exists("wykres_trendu.png") :

        # Wstawienie obrazka na współrzędnych x=10, w=190 (na szerokość strony)
        pdf.image("wykres_trendu.png", x=10, w=190)

    # Jeśli plik z wykresem nie istnieje, dodajemy informację o braku danych do raportu, usuwając polskie znaki, aby zapewnić poprawne wyświetlanie w PDF
    else :

        # Ustawiamy czcionkę Arial Italic o rozmiarze 10 dla informacji o braku danych
        pdf.set_font("Arial", 'I', 10)

        # Dodajemy informację o braku danych do raportu, usuwając polskie znaki, aby zapewnić poprawne wyświetlanie w PDF
        pdf.cell(200, 10, txt=remove_polish_accents("(Brak wygenerowanego wykresu. Uruchom podglad wykresu w aplikacji, aby go dodac!)"), ln=True)


    # Sekcja Podsumowania - dodajemy podsumowanie i zalecenia końcowe do raportu - zapis
    try :

        # Zapisujemy wygenerowany raport PDF do pliku o podanej nazwie
        pdf.output(filename)

        # Jeśli zapis się powiedzie, wyświetlamy komunikat o sukcesie, informując użytkownika o wygenerowaniu raportu PDF
        print(f"\n[SUKCES] Wygenerowano raport PDF: {filename}")

    # Jeśli podczas zapisywania raportu PDF wystąpi błąd, przechwytujemy wyjątek i wyświetlamy komunikat o błędzie, informując użytkownika o problemie z generowaniem raportu PDF
    except Exception as e :

        # Wyświetlamy komunikat o błędzie, informując użytkownika o problemie z generowaniem raportu PDF, wraz z treścią wyjątku, która może pomóc w diagnozie problemu
        print(f"\n[BLAD] Nie udalo sie zapisac PDF: {e}")