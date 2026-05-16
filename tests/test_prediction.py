import unittest                                            # importuję moduł unittest do tworzenia testów jednostkowych 
import pandas as pd                                        # importuję moduł pandas do manipulacji danymi w formie DataFrame
from datetime import datetime, timedelta                   # importuję moduły datetime i timedelta do operacji na datach i czasie
from src.prediction import predict_goal_from_sql           # importuję funkcję predict_goal_from_sql z modułu prediction, która przewiduje cel na podstawie danych z bazy danych


class TestPrediction(unittest.TestCase) :                  # definiuję klasę TestPrediction, która dziedziczy po unittest.TestCase, co pozwala na tworzenie testów jednostkowych