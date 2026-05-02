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

        # Dodajemy tekst do raportu PDF, usuwając polskie znaki, aby zapewnić poprawne wyświetlanie w PDF, i ustawiając go na lewej stronie (align='L'), z możliwością zawijania tekstu (multi_cell)
        pdf.multi_cell(0, 8, remove_polish_accents(text))

    # Data na prawo

    # Ustawiamy czcionkę Arial Italic o rozmiarze 11 dla daty, co pozwala na wyróżnienie daty i nadanie jej profesjonalnego wyglądu
    pdf.set_font('Arial', 'I', 11)

    # Ustawiamy szary kolor tekstu dla daty, co zapewnia subtelny wygląd daty i nie odciąga uwagi od głównej treści raportu PDF
    pdf.set_text_color(100)

    # Dodajemy datę wygenerowania raportu, usuwając polskie znaki, aby zapewnić poprawne wyświetlanie w PDF, i ustawiając ją na prawej stronie (align='R'), co informuje użytkownika o czasie wygenerowania raportu PDF
    pdf.cell(0, 10, remove_polish_accents(f"Data wygenerowania raportu: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"), 0, 1, 'R')

    # Dodajemy odstęp między datą a nagłówkiem raportu, co poprawia czytelność i estetykę układu strony w raporcie PDF
    pdf.ln(5)

    # -- Sekcja 1 dokumentu - Diagnoza -- 

    # Dodajemy tytuł dla sekcji z diagnozą, usuwając polskie znaki, aby zapewnić poprawne wyświetlanie w PDF, co pozwala na wyróżnienie tej sekcji w raporcie PDF z analizą BMI i zaleceniami dietetycznymi
    section_title("1. Pomiary i Diagnoza:")

    # Dodajemy szczegółowe informacje o pomiarach i diagnozie, usuwając polskie znaki, aby zapewnić poprawne wyświetlanie w PDF, co pozwala na przekazanie użytkownikowi ważnych informacji o jego stanie zdrowia w raporcie PDF z analizą BMI i zaleceniami dietetycznymi
    normal_text(f"Wzrost: {wzrost} m\nObecna waga: {waga} kg\nZalecana waga: {min_ideal} - {max_ideal} kg")


    # Koloryzujemy napis BMI (zielony dla prawidłowej wagi, czerwony dla nadwagi)

    # Ustawiamy czcionkę Arial Bold o rozmiarze 12 dla napisu BMI, co pozwala na wyróżnienie tej informacji w raporcie PDF z analizą BMI i zaleceniami dietetycznymi
    pdf.set_font('Arial', 'B', 12)

    # Sprawdzamy kategorię BMI, aby ustawić odpowiedni kolor tekstu dla napisu BMI, co pozwala na szybkie zidentyfikowanie stanu zdrowia użytkownika w raporcie PDF z analizą BMI i zaleceniami dietetycznymi
    if kategoria in ["Niedowaga", "Otyłość", "Niedowaga"] :

        # Ustawiamy kolor czerwony dla napisu BMI, co wskazuje na niezdrowy stan wagi i przyciąga uwagę użytkownika do tej informacji w raporcie PDF z analizą BMI i zaleceniami dietetycznymi
        pdf.set_text_color(200, 50, 50)     

    # Jeśli kategoria BMI wskazuje na prawidłową wagę, ustawiamy kolor zielony dla napisu BMI, co wskazuje na zdrowy stan wagi i pozytywnie wyróżnia tę informację w raporcie PDF z analizą BMI i zaleceniami dietetycznymi
    else : 

        # Ustawiamy kolor zielony dla napisu BMI, co wskazuje na zdrowy stan wagi i pozytywnie wyróżnia tę informację w raporcie PDF z analizą BMI i zaleceniami dietetycznymi
        pdf.set_text_color(30, 150, 30)

    # Dodajemy napis z wartością BMI i kategorią, usuwając polskie znaki, aby zapewnić poprawne wyświetlanie w PDF, i ustawiając go na lewej stronie (align='L'), co informuje użytkownika o jego wskaźniku BMI i kategorii w raporcie PDF z analizą BMI i zaleceniami dietetycznymi
    pdf.cell(0, 10, remove_polish_accents(f"Wskaznik BMI: {bmi} ({kategoria})"), 0, 1)

    # Wklejamy ASCII pasek - musimy użyć czcionki Courier, aby zapewnić poprawne wyrównanie znaków, co pozwala na wizualne przedstawienie poziomu BMI w raporcie PDF z analizą BMI i zaleceniami dietetycznymi

    # Ustawiamy czcionkę Courier o rozmiarze 11 dla ASCII paska, co pozwala na poprawne wyrównanie znaków i estetyczne przedstawienie poziomu BMI w raporcie PDF z analizą BMI i zaleceniami dietetycznymi
    pdf.set_font('Courier', 'B', 11)

    # Czarny kolor tekstu dla ASCII paska
    pdf.set_text_color(0, 0, 0)  

    # Tworzymy pasek ASCII, który wizualnie przedstawia poziom BMI, gdzie '|' reprezentuje aktualny poziom BMI, a '-' reprezentuje pozostałą część skali, co pozwala na szybkie zrozumienie poziomu BMI w raporcie PDF z analizą BMI i zaleceniami dietetycznymi
    pdf.cell(0, 8, remove_polish_accents(pasek), 0, 1, 'C')

    # Dodajemy odstęp między sekcją z diagnozą a kolejną sekcją raportu, co poprawia czytelność i estetykę układu strony w raporcie PDF z analizą BMI i zaleceniami dietetycznymi
    pdf.ln(5)


    # -- Sekcja 2 - Dieta --

    # Dodajemy tytuł dla sekcji z zaleceniami dietetycznymi, usuwając polskie znaki, aby zapewnić poprawne wyświetlanie w PDF, co pozwala na wyróżnienie tej sekcji w raporcie PDF z analizą BMI i zaleceniami dietetycznymi
    section_title("2. Zapotrzebowanie i Dieta:")

    # Dodajemy szczegółowe informacje o zapotrzebowaniu kalorycznym i celach diety, usuwając polskie znaki, aby zapewnić poprawne wyświetlanie w PDF, co pozwala na przekazanie użytkownikowi ważnych informacji o jego zapotrzebowaniu kalorycznym i celach diety w raporcie PDF z analizą BMI i zaleceniami dietetycznymi
    normal_text(f"Cel dietetyczny: {cel.upper()}, bold=True)")

    # Dodajemy szczegółowe informacje o zapotrzebowaniu kalorycznym, usuwając polskie znaki, aby zapewnić poprawne wyświetlanie w PDF, co pozwala na przekazanie użytkownikowi ważnych informacji o jego zapotrzebowaniu kalorycznym w raporcie PDF z analizą BMI i zaleceniami dietetycznymi
    normal_text(f"Podstawowa przemiana materii (BMR): {bmr} kcal\nCalkowite zapotrzebowanie (TDEE): {tdee} kcal")

    # Dodanie odstępu między informacjami o zapotrzebowaniu kalorycznym a makroskładnikami, co poprawia czytelność i estetykę układu strony w raporcie PDF z analizą BMI i zaleceniami dietetycznymi
    pdf.ln(3)

    # Ustawiamy czcionkę Arial Bold o rozmiarze 12 dla nagłówków makroskładników, co pozwala na wyróżnienie tych informacji w raporcie PDF z analizą BMI i zaleceniami dietetycznymi
    pdf.set_font('Arial', 'B', 12)

    # Niebieski kolor tekstu dla nagłówków zalecanego spożycia dziennego kalorii
    pdf.set_text_color(41, 128, 185)  

    # Dodajemy szczegółowe informacje o zalecanym spożyciu dziennym kalorii, usuwając polskie znaki, aby zapewnić poprawne wyświetlanie w PDF, i ustawiając go na lewej stronie (align='L'), co informuje użytkownika o zalecanym spożyciu dziennym kalorii w raporcie PDF z analizą BMI i zaleceniami dietetycznymi
    pdf.cell(0, 8, remove_polish_accents(f"Zalecane spozycie dzienne: {docelowe_kcal} kcal"), 0, 1)

    # Ustawiamy czcionkę Arial o rozmiarze 12 dla treści makroskładników, co pozwala na przekazanie użytkownikowi ważnych informacji o zalecanym spożyciu makroskładników w raporcie PDF z analizą BMI i zaleceniami dietetycznymi
    pdf.set_font('Arial', '', 12)

    # Ustawiamy ciemnoszary kolor tekstu dla treści makroskładników, co zapewnia dobry kontrast z białym tłem i poprawia czytelność tych informacji w raporcie PDF z analizą BMI i zaleceniami dietetycznymi
    pdf.set_text_color(40, 40, 40)

    # Dodajemy szczegółowe informacje o zalecanym spożyciu białka, usuwając polskie znaki, aby zapewnić poprawne wyświetlanie w PDF, i ustawiając go na lewej stronie (align='L'), co informuje użytkownika o zalecanym spożyciu białka w raporcie PDF z analizą BMI i zaleceniami dietetycznymi
    pdf.cell(0, 8, remove_polish_accents(f"-> Bialko: {bialko} g"), 0, 1)

    # Dodajemy szczegółowe informacje o zalecanym spożyciu tłuszczów, usuwając polskie znaki, aby zapewnić poprawne wyświetlanie w PDF, i ustawiając go na lewej stronie (align='L'), co informuje użytkownika o zalecanym spożyciu tłuszczów w raporcie PDF z analizą BMI i zaleceniami dietetycznymi
    pdf.cell(0, 8, remove_polish_accents(f"-> Tluszcze: {tluszcze} g"), 0, 1)

    # Dodajemy szczegółowe informacje o zalecanym spożyciu węglowodanów, usuwając polskie znaki, aby zapewnić poprawne wyświetlanie w PDF, i ustawiając go na lewej stronie (align='L'), co informuje użytkownika o zalecanym spożyciu węglowodanów w raporcie PDF z analizą BMI i zaleceniami dietetycznymi
    pdf.cell(0, 8, remove_polish_accents(f"-> Weglowodany: {wegle} g"), 0, 1)

    # Dodajemy odstęp między sekcją z zaleceniami dietetycznymi a kolejną sekcją raportu, co poprawia czytelność i estetykę układu strony w raporcie PDF z analizą BMI i zaleceniami dietetycznymi
    pdf.ln(5)


    # -- Sekcja 3 - Wykres -- 

    # Dodajemy tytuł dla sekcji z wykresem historii wagi, usuwając polskie znaki, aby zapewnić poprawne wyświetlanie w PDF, co pozwala na wyróżnienie tej sekcji w raporcie PDF z analizą BMI i zaleceniami dietetycznymi
    section_title("3. Historia wagi (Wykres trendu): ")

    # Sprawdzamy, czy plik z wykresem trendu wagi istnieje, aby uniknąć błędów podczas próby dodania nieistniejącego pliku do raportu PDF, co pozwala na bezproblemowe generowanie raportu PDF z analizą BMI i zaleceniami dietetycznymi, nawet jeśli wykres trendu wagi nie został wygenerowany
    if os.path.exists("wykres_trendu.png") :

        # Dodajemy wykres trendu wagi do raportu PDF, umieszczając go na środku strony (x=10) i ustawiając szerokość na 190 mm, co pozwala na wizualne przedstawienie historii wagi użytkownika w raporcie PDF z analizą BMI i zaleceniami dietetycznymi
        pdf.image("wykres_trendu.png", x=10, w=190)  


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