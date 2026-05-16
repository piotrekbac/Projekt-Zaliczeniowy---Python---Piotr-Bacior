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