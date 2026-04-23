# Zaawansowany Asystent Zdrowia i Kalkulator BMI

Wielomodułowa aplikacja konsolowa napisana w języku Python. Projekt wykracza poza standardowe obliczanie wskaźnika BMI, oferując pełne statystyki dietetyczne, analizę danych (Data Science) oraz interaktywne wykresy graficzne.

**Autor:** Piotr Bacior (15 722) | **Rok:** 2026 | **Język:** Python 3

---

## Główne Funkcjonalności

*   **Obliczanie BMI i Idealnej Wagi:** Precyzyjne wyliczanie wskaźnika masy ciała oraz sugerowanie optymalnego zakresu wagowego dla danego wzrostu.
*   **Asystent Kaloryczny (BMR i TDEE):** Wykorzystanie wzoru *Mifflin-St Jeor* do obliczania Podstawowej Przemiany Materii oraz Całkowitego Dziennego Zapotrzebowania Energetycznego na podstawie wieku, płci i aktywności fizycznej.
*   **Wizualizacja ASCII:** Generowanie tekstowego, estetycznego paska w konsoli obrazującego umiejscowienie wskaźnika na skali (Niedowaga - Otyłość).
*   **Trwały zapis danych (I/O):**
    *   Zapis logów do czytelnego pliku tekstowego `bmi_results.txt`.
    *   Równoległy zapis danych ustrukturyzowanych do bazy `historia_bmi.csv` (kompatybilnej z programem Excel).
*   **Interaktywne Wykresy (Data Science):** Integracja z bibliotekami `Pandas` i `Matplotlib`. Program potrafi odczytać historię z pliku CSV i wygenerować w nowym oknie profesjonalny wykres trendu zmiany wagi oraz BMI w czasie.
*   **Idiotoodporność (Error Handling):** Zaawansowana obsługa wyjątków wyłapująca litery, zera, wartości ujemne oraz inteligentnie konwertująca wzrost podany w centymetrach na metry.

---

## Instrukcja uruchomienia

### 1. Inicjalizacja projektu

Aby móc w pełni korzystać z programu (w tym z interaktywnych wykresów), wymagane jest zainstalowanie zewnętrznych bibliotek do analizy danych.
Sklonuj repozytorium na swój dysk:

```bash
git clone https://github.com/piotrekbac/Projekt-Zaliczeniowy---Python---Piotr-Bacior.git
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