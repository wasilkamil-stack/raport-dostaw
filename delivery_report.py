#dostawy.csv ──wczytaj_dane──> dostawy (słownik: dostawca → ilość)
                                   #│
                              #raport_dostaw
                                   #▼
                     #wynik (słownik: opis → wartość)
                                   #│
                              #zapisz_csv
                                   #▼
                              #raport.csv

# Sekcja 1 - Funkcja wczytania danych

# wczytaj_dane(sciezka)
# sciezka = to napis z adresem pliku, jaki dokładnie plik chcę wczytać
# krok 1: utworz pusty słownik
# krok 2: otworz plik do odczytu (tryb "r")
# krok 3: pomin pierwsza linie, bo nagłówek
# krok 4: dla kazdej linii:
#           rozdziel linie po przecinku na nazwe i ilosc
#           zamien ilosc z tekstu na liczbę (int)
#           dodaj do slownika: klucz = dostawca, wartosc = ilosc
# funkcja zwraca: słownik

def wczytaj_dane(sciezka):    # Ta funkcja stworzy słownik w którym nazwa dostawcy jest kluczem a ilość palet jest wartościa
    dane = {}
    with open(sciezka, "r", encoding="utf-8") as plik:
        plik.readline()       # Pomija pierwszą linię bo to nagłówek 
        for linia in plik:
            czesci = linia.split(",")   # Tnę kazdą linię po przecinku na dwie części
            if len(czesci) !=2:         # Jeżleli po cięciu nie mam dwóch elementów wtedy pomijam tą linię
                continue                # Ta komenda pomija linię
            nazwa = czesci[0]           # Utwórz zmienną nazwa, Nazwa to pierwszy element z pociętej lini - jest na pozycji [0]
            try:                        # Python spróbuj coś dla mnie zrobić
                ilosc = int(czesci[1])  # Zamień drugi element z tekstu na liczbę
            except ValueError:          # Jeżeli napotkasz błąd ValueError przy zmianie
                continue                # Wtedy pomiń tą linię
            dane[nazwa] = ilosc         # Zapisz to w słowniku dane jako np. {"DHL": 200}
    return dane


# Sekcja 2 - Funkcja obliczająca statystyki dostaw

def raport_dostaw(dostawy, prog):      # Utwóz funkcję raport dostaw ( dostawy to słonik a próg jest liczbą)
    suma = 0                           # Utwórz zmienną suma
    najwieksza = None                  # Utwórz zmienna najwieksza - (Największa dostawa)
    najwiekszy_dostawca = None         # Utwóz zmienną najwiekszy_dostawca
    licznik_prog = 0                   # Utwóz zmienną licznik_prog - (Ile jest dostaw powyżej progu)
    suma_prog = 0                      # Utwórz zmienną suma_prog - (Suma palet powyżej progu)

    for dostawca in dostawy:           # Utwórz pętle która przechodzi po każdym kluczu
        ilosc = dostawy[dostawca]      # Utwórz zmienną ilość - (Jaka wartość znajduje się pod kluczem dostawca w słowniku dostawy)
        suma = suma + ilosc            # Suma = dodaj każdą kolejną ilość po przechodzeniu przez kolejne klucze w pętli do sumy która na
                                       # początku wynosi zero
        if najwieksza is None:         # Jeżeli największa dostawa nie jest jeszcze znana
            najwieksza = ilosc         # Wtedy największa dostawa równa się ilości którą znajdziesz jako pierwszą w pętli
            najwiekszy_dostawca = dostawca # A największy dostawca równa sie dostawcy w tym właśnie obiegu pętli
        elif ilosc > najwieksza:       # Jeżeli po kolejnym obiegu ilość będzie większa od dotychczasowej najwiekszej którą znalazłeś
            najwieksza = ilosc         # wtedy nadpisz zmienną największa o nową największą wartość
            najwiekszy_dostawca = dostawca  # Oraz nadpisz dostawcę dla największej wartości

        if ilosc > prog:                     # Jeśli ilość palet jest większa od ustalonego progu (Nie chcemy aby równała się progowi)
            licznik_prog = licznik_prog + 1  # Wtedy odnotuj to w zmiennej licznik_prog zliczając. Dodaj +1 przy każdeym obrocie spełniajacym warunek
            suma_prog = suma_prog + ilosc    # Oraz policz sumę palet które znalazły się powyżej progu

    if licznik_prog == 0:                    # Kiedy porównasz licznik_próg do 0 i okaże się że wynosi 0
        srednia_prog = None                  # Wtedy srednia_prog = None, Nie pokazuj błedu. Zwróc None(Dzielenie przez zero zatrzymalo by program)
    else:                                          # W innym przypadku
        srednia_prog = suma_prog / licznik_prog     # Policz ile będzie wynosić średnia

    return {                                     # Zwróć mi wyniki
        "suma": suma,
        "najwieksza dostawa": najwieksza,
        "najwiekszy dostawca": najwiekszy_dostawca,
        "powyzej progu": licznik_prog,
        "srednia powyzej progu": srednia_prog
    }

# Sekcja 3 - Funkcja zapisu do pliku
# 
# zapisz_csv(wynik, sciezka)
# wynik  = słownik z wynikami raportu, czyli suma, 
#           największa dostawa, licznik i średnia.
# sciezka = napis z adresem pliku, do którego zapisuję, np. “raport.csv“
# krok 1: otwórz plik w trybie do zapisu "write"
# krok 2: zapisz w nim w pierwszej lini, opis, wartosc(zapisz nagłówek)
# krok 3: dla kazdego klucza w wynik:
#           jesli wartosc jest None - 
#       > zapisz Brak Dostaw powyzej progu
#               w przeciwnym raize  -
#       > zapisz pare (klucz, wartosc)
# funkcja zwraca: nic

def zapisz_csv(wynik, sciezka): # Wynik to słownik z funkcji raport_dostaw a sciezka to adres do pliku do którego zapisuje
    with open(sciezka, "w", encoding="utf-8") as plik: # Otwiera adres pliku jako plik, tryb w = zapis, nadpisuje stary plik
        plik.write("opis,wartosc\n") # Zapisz na samym początku nagłówek "opis,wartosc"
        for klucz in wynik:  # Przejdz pętlę dla każdego klucza w słowniku wynik
            wartosc = wynik[klucz] # Stwórz zmienną wartość - Weź dane ze słownika wynik które stoją pod kluczem
            if wartosc is None:    # Jeśli wartość jest None
                plik.write(klucz + "," + "Brak dostaw powyzej progu" + "\n") # Zapisz klucz, Brak dostaw powyżej progu
            else: # W innym przypadku zapisz
                plik.write(klucz + "," + str(wartosc) + "\n") # Zapisz klucz oraz wartość "str" zamień liczbę na tekst
                
# Sekcja 4 Główna - Dane wejściowe - dostawy palet

def main():

    dostawy = wczytaj_dane("dane/dostawy_ok.csv")

    if len(dostawy) < 1:
        print("Brak dostaw")
    else:

        # Sekcja 5 - Automatyczne obliczenie raportu

        wynik = raport_dostaw(dostawy, 200)

        # Sekcja 6 - Zapisanie raportu do pliku CSV

        zapisz_csv(wynik, "raport.csv")

        # Sekcja 7 - Odczytanie zapisanego pliku

        with open("raport.csv", "r", encoding="utf-8") as plik:
            print(plik.read())

def testy():
    # Sekcja 8 - Testy

    # Test A: wszyscy ponizej 200
    # dane: {"DHL": 120, "INPOST": 100, "UPS": 111}
    # oczekuje: powyzej progu = 0, srednia powyzej progu = None

    test_a = {"DHL": 120, "INPOST": 100, "UPS": 111}
    wynik_a = raport_dostaw(test_a, 200)
    print(wynik_a)

    # Test B: jeden dostawca ma dokladnie 200
    # dane: {"DHL": 200, "INPOST": 100, "UPS": 111}
    # oczekuje: powyzej progu = 0, srednia powyzej progu = None
    test_b = {"DHL": 200, "INPOST": 100, "UPS": 111}
    wynik_b = raport_dostaw(test_b, 200)
    print(wynik_b)

main()
testy()
