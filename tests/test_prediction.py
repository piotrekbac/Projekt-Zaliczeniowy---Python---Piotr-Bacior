import unittest                                            # importuję moduł unittest do tworzenia testów jednostkowych 
import pandas as pd                                        # importuję moduł pandas do manipulacji danymi w formie DataFrame
from datetime import datetime, timedelta                   # importuję moduły datetime i timedelta do operacji na datach i czasie
from src.prediction import predict_goal_from_sql           # importuję funkcję predict_goal_from_sql z modułu prediction, która przewiduje cel na podstawie danych z bazy danych


class TestPrediction(unittest.TestCase) :                  # definiuję klasę TestPrediction, która dziedziczy po unittest.TestCase, co pozwala na tworzenie testów jednostkowych

    """ Klasa testowa dla algorytmów uczenia maszynoweg (regresji liniowej) """

    # Metoda testowa - test_empty_dataframe - sprawdza, czy funkcja predict_goal_from_sql poprawnie obsługuje pusty DataFrame. Oczekuje się, że funkcja zwróci None lub odpowiednią wartość wskazującą, że nie można dokonać predykcji na podstawie pustych danych
    def test_empty_dataframe(self) : 

        """ Sprawdza odpowiedź, gdy baza SQL jest pusta """

        # Tworzy pusty DataFrame
        df_empty = pd.DataFrame() 

        # Sprawdza, czy funkcja predict_goal_from_sql zwraca odpowiednią wartość (np. None lub komunikat o braku danych) dla pustego DataFrame
        self.assertEqual(predict_goal_from_sql(df_empty, 70.0), "Brak historii w bazie SQL.")


    # Metoda testowa - test_trend_calculation_success - sprawdza, czy funkcja predict_goal_from_sql poprawnie oblicza trend i przewiduje cel na podstawie danych z DataFrame. Oczekuje się, że funkcja zwróci przewidywaną wartość celu na podstawie dostarczonych danych
    def test_trend_calculation_success(self) : 
        
        """ Sprawdza obliczenia dni do osiągnięcia celu (pozytywny trend) """

        # Tworzymy symulowaną bazę z 3-ma pomiarami: pacjent traci 1kg dziennie 

        # Tworzymy listę dat dla trzech pomiarów, gdzie każdy pomiar jest oddalony o jeden dzień od poprzedniego
        dates = [datetime.now() - timedelta(days=2), datetime.now() - timedelta(days=1), datetime.now()]
