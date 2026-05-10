import sqlite3                                          # Import modułu sqlite3 do obsługi bazy danych SQLite
import pandas as pd                                     # Import modułu pandas do manipulacji danymi
from datetime import datetime                           # Import modułu datetime do obsługi dat i czasu

# Piotr Bacior - 15 722 - 2026 - Python - MH

# Nazwa pliku bazy danych
DB_NAME = "baza_pacjentow.db"  

# Definicja funkcji do inicjalizacji bazy danych
def init_db() :

    """
    Inizjalicja relacyjnej bazy danych SQLite, jeżeli tabela nie istnieje - tworzy ją 
    """

    # Nawiązanie połączenia z bazą danych (jeśli plik bazy danych nie istnieje, zostanie utworzony)
    conn = sqlite3.connect(DB_NAME)

    # Utworzenie kursora do wykonywania operacji na bazie danych
    cursor = conn.cursor()  

    # Tworzymy tabelę z użyciem języka zapytań SQL, jeśli tabela o nazwie 'pacjenci' nie istnieje
    cursor.execute('''
                   
        # Tworzenie tabeli 'pacjenci' z kolumnami: id, imie, nazwisko, wiek, plec
        CREATE TABLE IF NOT EXISTS pomiary (
                   
                   # Kolumna 'id' jest kluczem głównym i automatycznie inkrementuje się przy dodawaniu nowych rekordów
                   id INTEGER PRIMARY KEY AUTOINCREMENT,

                   # Kolumna 'data_pomiaru' przechowuje tekstową reprezentację daty pomiaru
                   data_pomiaru TEXT,

                   # Kolumna 'waga' przechowuje wartość wagi jako liczbę zmiennoprzecinkową
                   waga REAL,  

                   # Kolumna 'bmi' przechowuje wartość BMI jako liczbę zmiennoprzecinkową
                   bmi REAL, 

                    # Kolumna 'kategoria' przechowuje tekstową reprezentację kategorii BMI
                    kategoria TEXT,
                   
                    # Kolumna 'min_waga' przechowuje wartość minimalnej wagi jako liczbę zmiennoprzecinkową
                    min_waga REAL,
                   
                    # Kolumna 'max_waga' przechowuje wartość maksymalnej wagi jako liczbę zmiennoprzecinkową
                    max_waga REAL
        )
                   
    ''') 

    # Zatwierdzenie zmian w bazie danych
    conn.commit()  

    # Zamknięcie połączenia z bazą danych
    conn.close()  


    # Funkcja save_to_sql - do zapisywania danych pomiaru do bazy danych
    def save_to_sql(waga: float, wzrost: float, bmi: float, kategoria: str, min_waga: float, max_waga: float) :

        """ Dodaje nowy rekord do bazy danych używając instrukcji SQL INSERT. """

        # Nawiązanie połączenia z bazą danych
        conn = sqlite3.connect(DB_NAME)

        # Utworzenie kursora do wykonywania operacji na bazie danych
        cursor = conn.cursor()

        # Pobranie aktualnej daty i czasu w formacie "YYYY-MM-DD HH:MM:SS"
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Wykonanie zapytania SQL INSERT, aby dodać nowy rekord do tabeli 'pomiary' z wartościami przekazanymi jako argumenty funkcji
        cursor.execute('''
                       
            # Instrukcja SQL do wstawiania danych do tabeli 'pomiary' z kolumnami: data_pomiaru, waga, wzrost, bmi, kategoria, min_waga, max_waga
            INSERT INTO pomiary (data_pomiaru, waga, wzrost, bmi, kategoria, min_waga, max_waga)
                       
            # Sekcja VALUES określa wartości, które mają zostać wstawione do tabeli, odpowiadające kolumnom wymienionym wcześniej. Znaki zapytania (?) są używane jako miejsca na wartości, które zostaną przekazane jako argumenty funkcji.
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (now, waga, wzrost, bmi, kategoria, min_waga, max_waga))

        # Zatwierdzenie zmian w bazie danych
        conn.commit()

        # Zamknięcie połączenia z bazą danych
        conn.close()