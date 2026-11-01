#dostawy.csv ──wczytaj_dane──> dostawy (słownik: dostawca → ilość)
                                   #│
                              #raport_dostaw
                                   #▼
                     #wynik (słownik: opis → wartość)
                                   #│
                              #zapisz_csv
                                   #▼
                              #raport.csv




# 1. Funkcja obliczająca statystyki dostaw

def raport_dostaw(dostawy, prog):
    suma = 0
    najwieksza = None
    najwiekszy_dostawca = None
    licznik_prog = 0
    suma_prog = 0

    for dostawca in dostawy:
        ilosc = dostawy[dostawca]
        suma = suma + ilosc

        if najwieksza is None:
            najwieksza = ilosc
            najwiekszy_dostawca = dostawca
        elif ilosc > najwieksza:
            najwieksza = ilosc
            najwiekszy_dostawca = dostawca

        if ilosc > prog:
            licznik_prog = licznik_prog + 1
            suma_prog = suma_prog + ilosc

    if licznik_prog == 0:
        srednia_prog = None
    else:
        srednia_prog = suma_prog / licznik_prog

    return {
        "suma": suma,
        "najwieksza dostawa": najwieksza,
        "najwiekszy dostawca": najwiekszy_dostawca,
        "powyzej progu": licznik_prog,
        "srednia powyzej progu": srednia_prog
    }

# Sekcja 1b - Funkcja zapisu do pliku
# 
# zapisz_csv(wynik, sciezka)
# wynik  = słownik z wynikami raportu, czyli suma, 
#           największa dostawa, licznik i średnia.
# sciezka = raport.csv
# krok 1: otwórz plik w trybie do zapisu "write"
# krok 2: zapisz w nim w pierwszej lini, opis, wartosc(zapisz nagłówek)
# krok 3: dla kazdego klucza w wynik:
#           jesli wartosc jest None - 
#       > zapisz Brak Dostaw powyzej progu
#               w przeciwnym raize  -
#       > zapisz pare (klucz, wartosc)
# funkcja zwraca: nic

def zapisz_csv(wynik, sciezka):
    with open(sciezka, "w", encoding="utf-8") as plik:
        plik.write("opis,wartosc\n")
        for klucz in wynik:
            wartosc = wynik[klucz]
            if wartosc is None:
                plik.write(klucz + "," + "Brak dostaw powyzej progu" + "\n")
            else:
                plik.write(klucz + "," + str(wartosc) + "\n")
                
# Sekcja 1c - Funkcja wczytania danych

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

# 2. Dane wejściowe - dostawy palet

dostawy = wczytaj_dane("dane/dostawy_ok.csv")

if len(dostawy) < 1:
    print("Brak dostaw")
else:

    # 3. Automatyczne obliczenie raportu

    wynik = raport_dostaw(dostawy, 200)

    # 4. Zapisanie raportu do pliku CSV

    zapisz_csv(wynik, "raport.csv")

    # 5. Odczytanie zapisanego pliku

    with open("raport.csv", "r", encoding="utf-8") as plik:
        print(plik.read())

# 6. Testy

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




















# 4. Zapisanie raportu do pliku CSV - Stara Metoda

# zapisz_csv(raport_dostaw, "raport.csv")

# plik = open("raport.csv", "w", encoding="utf-8")

# plik.write("opis,wartosc\n")

# for klucz in wynik:
    # jeśli wartość jest None, to do pliku zapisz: Brak dostaw powyzej progu
    # wartosc = wynik[klucz]
    # if wartosc is None:
        # plik.write(klucz + "," + "Brak dostaw powyzej progu" + "\n")
    # else:    
    # w przeciwnym razie do pliku zapisz: wartość
        # plik.write(klucz + "," + str(wartosc) + "\n")







