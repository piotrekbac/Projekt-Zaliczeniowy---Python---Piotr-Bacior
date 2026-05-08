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