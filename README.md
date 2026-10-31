# Raport dostaw

## Problem
Obecnie pracownicy muszą często ręcznie liczyć dostawy w excelu, napotykają przy tym błedy związane z brudnymi danymi
które mogą fałszować statystyki. Często zajmuje to sporo czasu pisania skomplikowanych formuł dla każdego
podsumowania osobno. Jeżeli pracownik przeoczy jakiś błąd manager może dostać zafałszowany wynik,
co może się przekładać na błedne decyzje które podejmuje na podstawie raportu
## Dane
W pliku .CSV mamy dwie kolumny. dostawca - Nazwę dostawcy, oraz ilosć - ile palet zostało dostarczonych.
W folderze "dane" dane mamy pliki dostawy.csv - dostawy dobre z błędnymi liniami(tak jak zazwyczaj zachowują się pliki),
mają różnego rodzaju błędy.
dostawy_ok.csv - idealny plik bez błędów.
dostawy_pisty.csv. - Sprawdzić możemy przypadek graniczny kiedy z jakiegoś powodu plik jest pusty
## Co robi program
Program przygotowuje gotowy raport z nieuporządkowanych plików .csv które są odczytywane, automatycznie zliczane,
możemy ustawić próg dostaw aby widzieć poziom który będzie dla nas odpowiedni. Dodatkowo program ma zabezpieczenia przed
brudnymi danymi aby przy pustych liniach lub błednych wartościach nadal pracował.
Plik automatycznie zlicza ile palet zostało dostarczonych łącznie.
Na podstawie wszystkich palet pokazuje który dostawca dostarczył najwięcej palet.
Następnie wypisuje który dokładnie dostawca dostarczył najwięcej palet.
Możemy też ustawić próg aby monitorować czy któryś dostawca nie dostarcza zbyt dużo palet. Jeżeli nikt nie przekracza
tego poziomu wtedy otrzymamy 0
## Wnioski
W analizowanym okresie dostarczono łącznie 590 palet.
Najwięcej dostarczył DHL (200 palet), czyli ok. 34% wszystkich dostaw.
Żaden dostawca nie przekroczył progu 200 palet, więc nikt nie przeciąża magazynu, 
ale DHL jest dokładnie na granicy i warto go obserwować