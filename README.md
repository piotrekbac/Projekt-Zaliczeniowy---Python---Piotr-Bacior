# Osobisty Asystent Zdrowia i Kalkulator BMI

Zaawansowana aplikacja dietetyczno-analityczna, zrealizowana jako projekt zaliczeniowy z języka Python. Projekt udowadnia płynne przejście od skryptu konsolowego do nowoczesnej, wielomodułowej aplikacji webowej z wykorzystaniem baz danych, zewnętrznych API oraz uczenia maszynowego.

**Autor:** Piotr Bacior (15 722) | **Rok:** 2026 | **Język:** Python 3

--- 

## Zastosowane moduły i technologie 

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?logo=streamlit&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightblue?logo=sqlite&logoColor=white)
![Machine Learning](https://img.shields.io/badge/AI-Linear_Regression-green)

---

## Architektura i Funkcjonalności

Projekt oparty jest na wzorcu inżynieryjnym **Separation of Concerns**. Logika matematyczna została całkowicie odseparowana od interfejsów, co pozwoliło na podpięcie jej pod dwa niezależne środowiska: klasyczne CLI (`main.py`) oraz nowoczesne WebUI (`web_app.py`).

### 1. 🌐 Aplikacja Webowa (Streamlit)
* W pełni responsywny i reaktywny interfejs użytkownika w przeglądarce.
* Parametry zdrowotne i wykresy odświeżają się w czasie rzeczywistym przy użyciu suwaków.

### 2. 🗄️ Relacyjna Baza Danych (SQLite)
* Dane pacjenta zapisywane są trwale na lokalnym serwerze przy użyciu języka zapytań **SQL** (moduł `sqlite3`).
* Możliwość odczytu i analizy historycznych rekordów z tabeli.

### 3. 🤖 Machine Learning (AI Prediction)
* Algorytm regresji liniowej (biblioteka `numpy`) wyznacza trend zmian wagi pacjenta.
* System automatycznie przewiduje i formatuje dokładną datę kalendarzową osiągnięcia idealnego środka normy BMI.

### 4. 🌍 REST API (Zewnętrzne integracje)
* Łączność z zewnętrzną bazą kulinarną w celu serwowania przepisów dietetycznych na podstawie docelowych makroskładników (biblioteka `requests`).
* **Wzorzec Fallback (Graceful Degradation):** W przypadku braku klucza API lub awarii sieci, program płynnie ładuje wbudowaną lokalną bazę przepisów.

---

## Instrukcja uruchomienia

### 1. Inicjalizacja projektu

Aby móc w pełni korzystać z programu (w tym z interaktywnych wykresów), wymagane jest zainstalowanie zewnętrznych bibliotek do analizy danych.
Sklonuj repozytorium na swój dysk:

```bash
git clone https://github.com/piotrekbac/Projekt-Zaliczeniowy---Python---Piotr-Bacior.git
```

### 2a. (Opcjonalnie) Uruchom wirtualne środowisko (venv).

### 2b. Zainstaluj wymagane biblioteki:

```bash
pip install pandas matplotlib numpy
```

---

## Uruchomienie Programu

Aby odpalić Asystenta Zdrowia, uruchom główny plik w swoim terminalu:

```bash
python main.py
```

---

## Testy Jednostkowe (Unit Tests)

Projekt może pochwalić się 100% pokryciem kodu testami jednostkowymi. Napisano łącznie 10 niezależnych testów, które sprawdzają zarówno poprawne wyniki matematyczne, zachowanie przyjmowania ujemnych wartości, jak i mockowanie zapisu do plików tymczasowych.
Aby uruchomić pakiet testów, wpisz w terminalu:

```bash
python -m unittest discover -s tests
```

---

## Architektura i Struktura Projektu

Projekt został napisany z zachowaniem dobrych praktyk inżynierii oprogramowania (Separation of Concerns). Kod podzielono na logiczne moduły:


```text
 Projekt-Zaliczeniowy
 ┣  src                                     # Folder src (w nim analyzer.py, calculator.py, charts.py, file_handler.py)
 ┃ ┣  analyzer.py                           # Logika kategoryzacji BMI i rysowania paska ASCII
 ┃ ┣  calculator.py                         # Algorytmy matematyczne (BMI, BMR, TDEE, waga idealna)
 ┃ ┣  charts.py                             # Generowanie wykresów z użyciem Matplotlib i Pandas
 ┃ ┗  file_handler.py                       # Odczyt i zapis danych (TXT oraz CSV)
 ┣  tests                                   # Folder z testami (w nim test_analyzer.py, test_calculator.py, test_file_handler.py)
 ┃ ┣  test_analyzer.py                      # Testy analizatora
 ┃ ┣  test_calculator.py                    # Testy funkcji matematycznych
 ┃ ┗  test_file_handler.py                  # Testy I/O (z użyciem wirtualnych plików tempfile)
 ┣  main.py                                 # Główna pętla programu i interfejs CLI
 ┗  README.md                               # Dokumentacja projektu
 ```