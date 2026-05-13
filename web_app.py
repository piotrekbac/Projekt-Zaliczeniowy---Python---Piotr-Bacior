import streamlit as st                                                          # importuję bibliotekę streamlit do tworzenia interfejsu webowego 
import pandas as pd                                                             # importuję bibliotekę pandas do manipulacji danymi w formie tabel
import matplotlib.pyplot as plt                                                 # importuję bibliotekę matplotlib do renderowania wykresów
import os                                                                       # importuję moduł os do operacji na plikach i ścieżkach systemowych

# Importowanie naszych autorskich funkcji z modułów w folderze src
from src.calculator import calculate_bmi, calculate_ideal_weight, calculate_bmr, calculate_tdee, calculate_macros
from src.analyzer import analyze_bmi, calculate_weight_difference                               
from src.prediction import predict_goal_date                                       
from src.api_client import fetch_recipes_from_api, get_meal_suggestions, meal_kcal               
from src.database import init_db, save_measurement_to_csv, load_history_from_csv, save_to_sql, read_from_sql         
from src.prediction import predict_goal_from_sql 
from src.pdf_generator import generate_pdf_report

# Piotr Bacior - 15 722 - 2026 - Python - MH

# Inicjalizuję bazę danych (tworzę plik CSV, jeśli jeszcze nie istnieje) - ważne, by to zrobić przed renderowaniem strony, by uniknąć błędów związanych z brakiem pliku
init_db()  

# Konfiguracja strony Streamlit - ustawiam tytuł karty w przeglądarce, ikonę jabłka (odnoszącą się do zdrowia) oraz szeroki układ strony (layout="wide"), by maksymalnie wykorzystać przestrzeń ekranu
st.set_page_config(page_title="Asystent Zdrowia AI - PB2026", page_icon="🍏", layout="wide")

# Wyświetlam główny tytuł aplikacji na stronie
st.title("🍏 Interaktywny Asystent Zdrowia i Kalkulator BMI")    

# Wyświetlam krótki opis aplikacji informujący, że aplikacja jest w pełni reaktywna i działa w czasie rzeczywistym
st.markdown("Wersja przeglądarkowa projektu oparta na silniku Python Data Science. Zmień parametry z lewej strony, a wyniki **zaktualizują się natychmiast!**")

# =====================================================================================
# SEKCJA PANELU BOCZNEGO (SIDEBAR) - DO WPROWADZANIA DANYCH W CZASIE RZECZYWISTYM
# =====================================================================================

# Nagłówek sekcji bocznej dla panelu sterowania
st.sidebar.header("📋 Wprowadź swoje dane")    

# Pole numeryczne do wprowadzania wagi, z krokiem co 0.5 kg (aby umożliwić precyzyjne wprowadzanie)
waga = st.sidebar.number_input("Waga (kg)", min_value=20.0, max_value=300.0, value=70.0, step=0.5)    

# Pole numeryczne do wprowadzania wzrostu, z krokiem co 1 cm (0.01 m)
wzrost = st.sidebar.number_input("Wzrost (m)", min_value=1.00, max_value=2.50, value=1.75, step=0.01)

# Pole numeryczne do wprowadzania wieku (w pełnych latach)
wiek = st.sidebar.number_input("Wiek (lata)", min_value=10, max_value=120, value=30, step=1)    

# Lista rozwijana (selectbox) do wyboru płci biologicznej
plec = st.sidebar.selectbox("Płeć", options=["Mężczyzna", "Kobieta"])    

# Logika skracająca płeć do formatu akceptowanego przez nasze funkcje kalkulatora ('m' lub 'k')
plec_skrot = "m" if plec == "Mężczyzna" else "k"    

# Słownik wiążący opisowe poziomy aktywności fizycznej z ich liczbowymi mnożnikami używanymi w algorytmach
aktywnosc_dict = {
    "1. Siedzący tryb (brak aktywności)": 1,                  
    "2. Lekko aktywny (lekkie ćwiczenia 1-3 dni/tyg)": 2,                  
    "3. Umiarkowanie aktywny (ćwiczenia 3-5 dni/tyg)": 3,           
    "4. Bardzo aktywny (intensywne ćwiczenia 6-7 dni/tyg)": 4,                 
    "5. Ekstremalnie aktywny (praca fizyczna / trening 2x dziennie)": 5            
}

# Wyświetlamy listę rozwijaną z kluczami słownika jako opcjami dla użytkownika
aktywnosc_wybor = st.sidebar.selectbox("Poziom aktywności fizycznej", options=list(aktywnosc_dict.keys()))    

# Mapujemy wybrany przez użytkownika klucz na odpowiednią wartość liczbową (1-5) potrzebną do obliczeń TDEE
aktywnosc = aktywnosc_dict[aktywnosc_wybor]    

# =====================================================================================
# GŁÓWNE OBLICZENIA (BACKEND) - WYKONUJĄ SIĘ AUTOMATYCZNIE PO ZMIANIE JAKIEGOKOLWIEK POLA
# =====================================================================================

# Obliczamy BMI na podstawie wprowadzonych danych z paska bocznego
bmi = calculate_bmi(waga, wzrost)

# Pobieramy słowną kategorię medyczną (np. Nadwaga) na podstawie BMI
kategoria = analyze_bmi(bmi)  

# Obliczamy optymalne granice wagi dla wzrostu użytkownika (minimalna i maksymalna waga)
min_w, max_w = calculate_ideal_weight(wzrost)  

# Pobieramy gotowe zdanie tekstowe z analizatora określające, ile kg nam brakuje lub mamy w nadmiarze
roznica = calculate_weight_difference(waga, min_w, max_w)

# Obliczamy Podstawową Przemianę Materii (BMR) wzorem Mifflin-St Jeor
bmr = calculate_bmr(waga, wzrost, wiek, plec_skrot)  

# Obliczamy Całkowite Zapotrzebowanie Energetyczne (TDEE) włączając w to aktywność
tdee = calculate_tdee(bmr, aktywnosc)  

# Ustalamy domyślny cel dietetyczny jako "utrzymanie" i zapotrzebowanie równe TDEE
cel_dietetyczny = "utrzymanie"
docelowe_kcal = tdee  

# Automatyczna modyfikacja celu dietetycznego i kalorii na podstawie zdiagnozowanej kategorii
if kategoria == "Niedowaga": 
    cel_dietetyczny = "masa"
    docelowe_kcal = round(tdee + 500, 2)  
elif kategoria in ['Nadwaga', 'Otyłość']:
    cel_dietetyczny = "redukcja"
    docelowe_kcal = round(tdee - 500, 2)   
    if kategoria == "Otyłość": 
        # Większe ucięcie kalorii w przypadku otyłości dla optymalizacji redukcji
        docelowe_kcal = round(tdee - 650, 2)

# Obliczamy proporcje makroskładników w gramach na bazie wytyczonego celu kalorii
bialko, tluszcze, wegle = calculate_macros(docelowe_kcal, cel_dietetyczny)  

# =====================================================================================
# WYŚWIETLANIE W GŁÓWNYM OKNIE (FRONTEND) - PREZENTACJA WYNIKÓW
# =====================================================================================

# Tworzymy 3 równe kolumny, w których umieścimy najważniejsze wskaźniki (Metryki)
col1, col2, col3 = st.columns(3)

# Wyświetlamy widget ze Wskaźnikiem BMI (z formaterem wyświetlającym go jako tekst bazowy) i mniejszym tekstem kategorii pod spodem
col1.metric("Wskaźnik BMI", f"{bmi}", kategoria)    

# Wyświetlamy widget z zakresem idealnej wagi 
col2.metric("Idealna waga", f"{min_w} - {max_w} kg")    

# Wyświetlamy widget z całkowitym zapotrzebowaniem na energię
col3.metric("TDEE (Zapotrzebowanie)", f"{tdee} kcal")        

# Wyświetlamy czytelną informację tekstową o tym, ile wagi musimy zgubić/przybrać, używając komponentu ostrzeżenia/informacji (st.info)
st.info(f"⚖️ **Analiza wagi:** {roznica}")

# Dodajemy estetyczną linię poziomą separującą sekcje na stronie
st.divider()    

# Wyświetlamy podtytuł dla strefy dietetycznej
st.subheader("🍽️ Twój Zindywidualizowany Plan Dietetyczny")       

# Wyświetlamy informacje podsumowujące cel i wyliczone z niego docelowe spożycie kcal
st.markdown(f"**Cel:** {cel_dietetyczny.upper()} | **Zalecane spożycie:** {docelowe_kcal} kcal / dzień")

# Tworzymy kolejne 3 kolumny do kolorowego zaprezentowania rozkładu makroskładników w gramach
c1, c2, c3 = st.columns(3)
c1.success(f"🥩 **Białko:** {bialko} g / dzień")                # Kolor zielony dla białka
c2.warning(f"🥑 **Tłuszcze:** {tluszcze} g / dzień")           # Kolor żółty dla tłuszczy
c3.error(f"🥖 **Węglowodany:** {wegle} g / dzień")             # Kolor czerwony dla węglowodanów

st.divider()    

# =====================================================================================
# SEKCJA WYKRESU I PREDYKCJI AI - ANALIZA DANYCH HISTORYCZNYCH
# =====================================================================================

st.subheader("📈 Analiza Danych i Predykcja AI")       

# Sprawdzamy, czy plik z historią istnieje, upewniając się, że używamy dokładnej nazwy ("historia_bmi.csv")
if os.path.exists("historia_bmi.csv"): 

    # Obliczamy tzw. złoty środek normy wagowej pacjenta, by wyznaczyć punkt docelowy dla algorytmu AI
    srodek_normy = round((min_w + max_w) / 2, 1)    
    
    # Przekazujemy historię i środek normy do modułu uczenia maszynowego (Regresji Liniowej), by wyliczył przewidywaną datę sukcesu
    prognoza = predict_goal_date("historia_bmi.csv", srodek_normy)    

    # Wyświetlamy wynik algorytmu AI w formie pogrubionego tekstu
    st.markdown(f"**🤖 Predykcja AI:** {prognoza}")    

    # Wczytujemy bazę danych z pliku CSV za pomocą biblioteki Pandas do obiektu typu DataFrame
    df = pd.read_csv("historia_bmi.csv", sep=";")

    # Standaryzujemy kolumnę czasu do natywnego typu datetime, co pozwoli Matplotlib poprawnie rysować oś X (chronologicznie)
    df['Data i czas'] = pd.to_datetime(df['Data i czas'])

    # Inicjalizujemy "płótno" na wykres o określonych proporcjach w calach
    fig, ax = plt.subplots(figsize=(10, 4))    

    # Rysujemy główną linię trendu łączącą punkty pomiarowe. Ustawiamy kolor niebieski i znaczniki kropkowe na każdym pomiarze.
    ax.plot(df['Data i czas'], df['Waga (kg)'], marker='o', color='royalblue', linestyle='-', linewidth=2)

    # Parametryzacja etykiet i wizualiów wykresu
    ax.set_title("Historia Twojej Wagi", fontsize=14)
    ax.set_ylabel("Waga (kg)")

    # Włączamy siatkę na wykresie, ustawiając delikatnie przezroczystą linię przerywaną, aby nie przytłaczała głównego wykresu
    ax.grid(True, linestyle='--', alpha=0.7)

    # Używamy specjalnej funkcji Streamlit, która "chwyta" wyrenderowany przed chwilą wykres Matplotlib i wrzuca go na stronę internetową jako responsywny obraz wektorowy
    st.pyplot(fig)

else: 
    # Jeśli program po przeszukaniu folderu projektu nie znajdzie bazy danych, wyświetla eleganckie, żółte ostrzeżenie dla użytkownika
    st.warning("Brak pliku CSV z historią pomiarów. Zapisz dane z poziomu konsoli, aby wygenerować tutaj interaktywny wykres i predykcje AI.")


# =====================================================================================
# SEKCJA INTEGRACJI Z API (PROPOZYCJE POSIŁKÓW)
# =====================================================================================

# Dodajemy estetyczną linię poziomą separującą sekcje na stronie
st.divider()

# Wyświetlamy podtytuł dla strefy integracji z API, sugerując, że znajdziemy tam propozycje posiłków na bazie docelowej kaloryczności
st.subheader("Propozycje Posiłków (Integracja API)")

# Wyświetlamy informację, że poniżej znajdziemy przepisy kulinarne dostosowane do naszego celu dietetycznego, pobrane z internetu
st.markdown("Poniżej pobrano z internetu przepisy dostosowane do Twojego celu dietetycznego (ok. 1/3 dziennego zapotrzebowania na posiłek).")


# Pobieramy listę przepisów kulinarnych na bazie docelowej kaloryczności
przepisy = get_meal_suggestions(docelowe_kcal)    

# Sprawdzamy, czy lista przepisów nie jest pusta, co oznacza, że API zwróciło jakieś propozycje
if przepisy :

    # Tworzymy 3 kolumny, w których umieścimy karty z przepisami kulinarnymi
    r1, r2, r3 = st.columns(3)

    # Iterujemy po pierwszych 3 przepisach (jeśli jest ich mniej, iterujemy po wszystkich) i umieszczamy je w kolejnych kolumnach
    kolumny_przepisow = [r1, r2, r3]


    # Pętla generująca karty ze zdjęciem i linkiem dla każdego przepisu
    for inx, przepis in enumerate(przepisy) :  

        # Każda karta to klikany link (st.markdown z formatowaniem Markdown), który otwiera się w nowej karcie przeglądarki (target="_blank") i zawiera zdjęcie oraz tytuł przepisu
        with kolumny_przepisow[inx] : 

            # Wyświetlam zdjęcie przepisu, rozciągając je na całą szerokość kolumny
            st.image(przepis['image'], use_container_width=True)  

            # Wyświetlam tytuł przepisu pogrubioną czcionką
            st.markdown(f"**{przepis['name']}**")  

            # Wyświetlam kaloryczność przepisu
            st.write(f" {przepis['calories']} kcal")  

            # Link do przepisu
            st.markdown(f"[Kliknij po przepis]({przepis['url']})")  


# Jeśli nie znaleziono przepisów, wyświetlamy komunikat
else :

    # Jeśli API nie zwróciło żadnych przepisów, wyświetlamy elegancki komunikat o błędzie w kolorze czerwonym, informując użytkownika o problemie z pobraniem danych
    st.error("Wystąpił problem z pobraniem przepisów z API.")


# Dodajemy estetyczną linię poziomą separującą sekcje na stronie
st.divider()

# Wyświetlam podtytuł dla sekcji analizy danych i predykcji AI, sugerując, że znajdziemy tam wykres historii wagi oraz prognozę daty osiągnięcia celu
st.subheader("Analiza danych i predykcja AI")


# =========================================================
# ODDZIELONA SEKCJA BAZY DANYCH (KLIKNIĘCIE ZAPISUJE DANE)
# =========================================================


# Dodajemy estetyczną linię poziomą separującą sekcje na stronie
st.divider()

# Wyświetlam podtytuł dla sekcji zapisu danych do bazy, sugerując, że użytkownik może tam zapisać swoje pomiary do bazy danych
st.subheader("📊 Zapisz swoje pomiary do bazy danych")



# Wciśnięcie tego przycisku uruchomi komendę INSERT w module bazy danych 
if st.button("ZAPISZ TEN POMIAR DO BAZY DANYCH", type="primary", use_container_width=True) : 

    # Funkcja z modułu bazy danych, która zapisuje pomiar do pliku CSV (symulacja bazy SQL) i aktualizuje historię
    save_to_sql(waga, wzrost, wiek, plec_skrot)  

    # Wyświetlam komunikat sukcesu, informując użytkownika, że pomiar został pomyślnie zapisany do bazy danych i sugerując odświeżenie strony, by zobaczyć zaktualizowany wykres i prognozy AI
    st.success("Pomyślnie zapisano pomiar do bazy danych! Odśwież stronę, by zobaczyć zaktualizowany wykres i prognozy AI.")

# Dodajemy estetyczną linię poziomą separującą sekcje na stronie
st.divider()


# Wyświetlam podtytuł dla sekcji integracji z API, sugerując, że znajdziemy tam propozycje posiłków na bazie docelowej kaloryczności
st.subheader("Propozycje Posiłków (Integracja API)")

# Pobieramy listę przepisów kulinarnych na bazie docelowej kaloryczności
przepisy = get_meal_suggestions(docelowe_kcal)


# Sprawdzamy, czy lista przepisów nie jest pusta, co oznacza, że API zwróciło jakieś propozycje
if przepisy :

    # Tworzymy 3 kolumny, w których umieścimy karty z przepisami kulinarnymi
    r1, r2, r3 = st.columns(3)

    # Iterujemy po pierwszych 3 przepisach (jeśli jest ich mniej, iterujemy po wszystkich) i umieszczamy je w kolejnych kolumnach
    cols = [r1, r2, r3]

    # Pętla generująca karty ze zdjęciem i linkiem dla każdego przepisu
    for inx, przepis in enumerate(przepisy) :

        # Każda karta to klikany link (st.markdown z formatowaniem Markdown), który otwiera się w nowej karcie przeglądarki (target="_blank") i zawiera zdjęcie oraz tytuł przepisu
        with cols[inx] :

            # Wyświetlam zdjęcie przepisu, rozciągając je na całą szerokość kolumny
            st.image(przepis['image'], use_container_width=True)  

            # Wyświetlam tytuł przepisu pogrubioną czcionką
            st.markdown(f"**{przepis['name']}**")

            # Wyświetlam kaloryczność przepisu
            st.write(f" {przepis['calories']} kcal")

            # Link do przepisu
            st.markdown(f"[Kliknij po przepis]({przepis['url']})")


# Oddzielamy sekcję z propozycjami posiłków od reszty strony, dodając estetyczną linię poziomą
st.divider()


# Wyświetlam podtytuł dla sekcji analizy danych i predykcji AI, sugerując, że znajdziemy tam wykres historii wagi oraz prognozę daty osiągnięcia celu
st.subheader("Analiza danych i predykcja AI")

# Wyciągamy dane komendą SELECT z bazy danych 
df_sql = read_from_sql()    


# Sprawdzamy, czy DataFrame zawiera jakieś dane (czyli czy baza danych nie jest pusta), zanim spróbujemy wykonać na niej operacje analityczne i predykcyjne
if not df_sql.empty :

    # Obliczamy tzw. złoty środek normy wagowej pacjenta, by wyznaczyć punkt docelowy dla algorytmu AI
    srodek_normy = round((min_w + max_w) / 2, 1)

    # Obliczamy prognozę daty osiągnięcia celu wagowego na bazie danych z SQL i złotego środka normy, korzystając z funkcji regresji liniowej w module prediction
    prognoza = predict_goal_from_sql(df_sql, srodek_normy)

    # Wyświetlam wynik algorytmu AI w formie pogrubionego tekstu
    st.markdown(f"**Predykcja AI (na podstawie SQL): {prognoza} **")

    # Standaryzujemy kolumnę czasu do natywnego typu datetime, co pozwoli Matplotlib poprawnie rysować oś X (chronologicznie)
    df_sql['Data i czas'] = pd.to_datetime(df_sql['Data i czas'])

    # Inicjalizujemy "płótno" na wykres o określonych proporcjach w calach
    fig, ax = plt.subplots(figsize=(10, 4))

    # Rysujemy główną linię trendu łączącą punkty pomiarowe. Ustawiamy kolor niebieski i znaczniki kropkowe na każdym pomiarze.
    ax.plot(df_sql['Data i czas'], df_sql['Waga (kg)'], marker='o', color='royalblue', linestyle='-', linewidth=2)

    # Parametryzacja etykiet i wizualiów wykresu
    ax.set_title("Historia Twojej Wagi (z SQL)", fontsize=14)

    # Ustawiamy etykietę osi Y na "Waga (kg)", by jasno komunikować, co przedstawia wykres
    ax.set_ylabel("Waga (kg)")

    # Włączamy siatkę na wykresie, ustawiając delikatnie przezroczystą linię przerywaną, aby nie przytłaczała głównego wykresu
    ax.grid(True, linestyle='--', alpha=0.7)

    # Używamy specjalnej funkcji Streamlit, która "chwyta" wyrenderowany przed chwilą wykres Matplotlib i wrzuca go na stronę internetową jako responsywny obraz wektorowy
    st.pyplot(fig)


    # Wyświetalam dodatkową informację tekstową, sugerując, że wykres i prognozy AI są oparte na danych z bazy SQL, co podkreśla wartość dodaną tej funkcjonalności
    with st.expander("Kliknij tutaj, aby zobaczyć surowe dane z SQL") : 

        # Wyświetlam surowe dane z SQL w formie interaktywnej tabeli Streamlit, umożliwiając użytkownikowi eksplorację danych, na których bazują wykresy i prognozy AI
        st.dataframe(df_sql)  

# Obsługa przypadku, gdy baza danych jest pusta (nie zawiera żadnych pomiarów), co może się zdarzyć przy pierwszym uruchomieniu aplikacji lub jeśli użytkownik jeszcze nie zapisał żadnych danych
else :

    # Wyświetlam eleganckie, żółte ostrzeżenie dla użytkownika, informując go, że baza danych jest pusta i zachęcając do zapisania pomiarów, by zobaczyć wykres historii wagi i prognozy AI oparte na danych z SQL
    st.warning("Baza danych jest pusta. Zapisz swoje pomiary, by zobaczyć wykres historii wagi i prognozy AI oparte na danych z SQL.")


# =========================================================
# SEKCJA GENEROWANIA RAPORTU PDF W PRZEGLĄDARCE
# =========================================================

# Dodanie podtytułu dla sekcji generowania raportu PDF, sugerując, że użytkownik może tam pobrać raport PDF z danymi pomiaru
st.subheader("📄 Pobierz Raport PDF z Twoimi Danymi")

# Wyświetlam informację, że kliknięcie przycisku poniżej wygeneruje i pobierze raport PDF zawierający aktualne dane pomiaru oraz analizę BMI, w tym wykres historii wagi, prognozę daty osiągnięcia celu oraz zalecenia dietetyczne
st.markdown("Kliknij przycisk poniżej, aby wygenerować i pobrać raport PDF zawierający Twoje aktualne dane pomiaru oraz analizę BMI. Raport będzie zawierał wykres historii wagi, prognozę daty osiągnięcia celu oraz zalecenia dietetyczne.")

# Obsługa logiki generowania raportu PDF po kliknięciu przycisku. Funkcja generate_pdf_report z modułu pdf_generator zajmie się stworzeniem pliku PDF na bazie aktualnych danych i analizy, a następnie udostępni go do pobrania w przeglądarce.
if st.button("Wygeneruj raport PDF", use_container_width=True) : 

    # Generujemy plik na dysku serwera
    generate_pdf_report(waga, wzrost, wiek, plec_skrot, bmi, kategoria, min_w, max_w, roznica, bmr, tdee, cel_dietetyczny, docelowe_kcal, bialko, tluszcze, wegle)

    # Odczytujemy go i tworzymy specjalny przycisk pobierania streamlit
    with open("raport_pomiaru.pdf", "rb") as pdf_file :

        # Tworzymy przycisk pobierania, który pozwala użytkownikowi pobrać wygenerowany raport PDF. Ustawiamy etykietę przycisku, nazwę pliku do pobrania oraz typ MIME dla plików PDF.
        st.download_button(

        )