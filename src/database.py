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

        CREATE TABLE IF NOT EXISTS pomiary (
                   
                   id INTEGER PRIMARY KEY AUTOINCREMENT,

                   data_pomiaru TEXT,

                   waga REAL,  

                   bmi REAL, 

                    kategoria TEXT,
                   
                    min_waga REAL,
                   
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
                       
            INSERT INTO pomiary (data_pomiaru, waga, wzrost, bmi, kategoria, min_waga, max_waga)
                       
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (now, waga, wzrost, bmi, kategoria, min_waga, max_waga))

        # Zatwierdzenie zmian w bazie danych
        conn.commit()

        # Zamknięcie połączenia z bazą danych
        conn.close()


    # Funkcja read_from_sql - do odczytywania danych z bazy danych i zwracania ich jako DataFrame
    def read_from_sql() -> pd.DataFrame :

        """ Pobiera wszystkie dane z bazy (SQL SELECT) i zwraca gotową tabelę Pandas DataFrame. """

        # Nawiązanie połączenia z bazą danych
        conn = sqlite3.connect(DB_NAME)

        # Pandas potrafi bezpośrednio wykonać zapytanie SQL i ułożyć dane w piękną tabelę!
        df = pd.read_sql_query("SELECT * FROM pomiary", conn)

        # Zamknięcie połączenia z bazą danych
        conn.close()

        # Zwrócenie DataFrame zawierającego dane z tabeli 'pomiary'
        return df