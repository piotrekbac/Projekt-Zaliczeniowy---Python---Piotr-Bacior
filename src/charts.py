import os                                      # importujemy moduł os, aby móc pracować z plikami i ścieżkami
import pandas as pd                            # importujemy pandas, aby móc pracować z danymi w formacie DataFrame
import matplotlib.pyplot as plt                # importujemy matplotlib, aby móc tworzyć wykresy

# Piotr Bacior - 15 722 - 2026 - Python - MH

# Funkcja show_bmi_trend_chart przyjmuje nazwę pliku CSV jako argument i wyświetla wykres trendu BMI na podstawie danych z tego pliku.
def show_bmi_trend_chart(csv_filename: str = "historia_bmi.csv") -> None:

    """
    Generuje i wyświetla wykres trendu BMI na podstawie danych z pliku CSV z historią pomiarów BMI
    Wykorzystuje biblioteki Pandas (do analizy danych) i Matplotlib (do tworzenia wykresów)

    Oczekiwane dane wejściowe:
    - csv_filename: nazwa pliku CSV zawierającego historię pomiarów BMI (domyślnie "historia_bmi.csv")

    Zachowanie funkcji:
    - Sprawdza, czy plik CSV istnieje i jest dostępny do odczytu
    - Odczytuje dane z pliku CSV do obiektu DataFrame
    - Generuje wykres liniowy przedstawiający trend wartości BMI w czasie
    
    Ograniczenia:
    - Funkcja przeznaczona jest do działania w środowisku, gdzie możliwe jest wyświetlanie wykresów (np. Jupyter Notebook, środowisko graficzne)
    
    Podnoszenie wyjątków:
    - Obsługuje potencjalne błędy przy generowaniu wykresu

    """


    # Sprawdzamy, czy plik CSV istnieje na dysku
    if not os.path.exists(csv_filename):        

        # Informujemy użytkownika, że plik nie istnieje
        print(f"Plik {csv_filename} nie istnieje. Nie można wygenerować wykresu trendu BMI.")   

        # Kończymy działanie funkcji, ponieważ nie można wygenerować wykresu bez danych
        return                                                                                  
    

    # Jeżeli plik istnieje, próbujemy go odczytać i wygenerować wykres, obsługując potencjalne błędy przy generowaniu wykresu
    try: 

        # Pandas - odczytuje całego excela dzięki DataFrame - średnik jako separator, ponieważ w pliku CSV używamy średnika do oddzielania wartości
        df = pd.read_csv(csv_filename, sep=";")


        # Sprawdzamy, czy DataFrame jest pusty (brak danych do wyświetlenia)
        if df.empty:           

            # Informujemy użytkownika, że plik jest pusty
            print(f"Plik {csv_filename} jest pusty. Nie można wygenerować wykresu trendu BMI.")         

            # Kończymy działanie funkcji, ponieważ nie można wygenerować wykresu bez danych
            return                 


        # Konwertujemy kolumnę 'Data i czas' na format daty i czasu                                                                
        df['Data i czas'] = pd.to_datetime(df['Data i czas'])  


        # Tworzymy wykres - matplotlib - wykres liniowy z datą na osi X i wartością BMI na osi Y
        # Zaczynamy od obszaru roboczego - z dwoma wykresami jeden pod drugim

        # Tworzymy obszar roboczy z dwoma wykresami (2 wiersze, 1 kolumna) o rozmiarze 10x8 cali
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))   

        # Dodajemy tytuł główny dla całego obszaru roboczego
        fig.suptitle('Historia Twoich pomiarów kalkulatora BMI', fontsize=16, fontweight='bold')   


        # Wykres 1 - Zmiana wagi w czasie 
        # 'o' oznacza, że chcemy kropki w punktach pomiarowych połączonych linią
        ax1.plot(df['Data i czas'], df['Waga (kg)'], marker='o', color='blue', linewidth=2)
        
        # Tytuł dla pierwszego wykresu
        ax1.set_title('Trend wagi w czasie', fontsize=12)                   

        # Etykieta osi Y dla pierwszego wykresu
        ax1.set_ylabel('Waga (kg)')            

        # Dodajemy siatkę do pierwszego wykresu                        
        ax1.grid(True, linestyle='--', alpha=0.7)     


        # Wykres 2 - Zmiana BMI w czasie    
        ax2.plot(df['Data i Czas'], df['BMI'], 'o-', color='green', linewidth=2)

        # Tytuł dla drugiego wykresu
        ax2.set_title('Trend BMI w czasie', fontsize=12)

        # Etykieta osi X dla drugiego wykresu
        ax2.set_xlabel('Data pomiaru')              

        # Etykieta osi Y dla drugiego wykresu
        ax2.set_ylabel('Wartość BMI')

        # Dodajemy siatkę do drugiego wykresu
        ax2.grid(True, linestyle='--', alpha=0.7)   


        # Rysujemy czerwoną przerywaną linię oznaczającą górną granicę prawidłwoego BMI (25.0)
        ax2.axhline(y=25.0, color='red', linestyle='--', label='Górna granica prawidłowego BMI (25.0)')