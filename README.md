***
***

# Cyfrowa Technika Foniczna 2023Z

### **LABORATORIUM 1-2** | Percepcja słuchowa i pomiary podstawowych parametrów dźwięku.

#### Niezbędne oprogramowanie i sprzęt.
Ćwiczenie wymaga posiadania urządzenia mobilnego z systemem Android (zadanie 2), a w częściach ćwiczenia związanych z percepcją słuchową (zadanie 1) wskazane jest, aby odsłuchiwanie próbek dźwiękowych odbywało się za pomocą **słuchawek nausznych lub dousznych** (niezalecany jest odsłuch za pomocą wbudowanych lub zewnętrznych głośników komputerowych). Przed przystąpieniem do wykonania zadania 2 ćwiczenia laboratoryjnego należy **pobrać i zainstalować** darmowe [oprogramowanie do analizy widmowej](https://play.google.com/store/apps/details?id=org.intoorbit.spectrum) oraz [oprogramowanie do pomiarów dźwięku](https://github.com/MarcinEL/WIT-LAB1/tree/main/installs). Instalacja oprogramowania do pomiarów dźwięku może wymagać włączenia opcji programisty w systemie Android. Aplikacja dBMeter w nowszych systemach Android może wymagać ręcznego nadania uprawnień dostępu do pamięci urządzenia i dostępu do mikrofonu (inaczej może się nie uruchomić, sama z siebie nie prosi o uprawnienia).

### Sprawozdania

Plik lub pliki ze sprawozdaniem (w dowolnym formacie: *.rtf, *.doc, *.docx, *.pdf, Markdown, LaTex) należy umieszczać w repozytorium [GitHub](https://github.com/). Po zalogowaniu się do systemu każdy powinien utworzyć nowe repozytorium o nazwie <CTF2023Z_SPR> i tam umieścić plik/pliki ze sprawozdaniem.

***
***

### `Zadanie 1. Percepcja słuchowa`

#### Polecenia

>Między kolejnymi testami słuchowymi proszę robić ok. 5 minut przerwy.
***
- [x] Test 1

1. Proszę wykonać test słuchowy online przygotowany przez firmę [Phonak zgodnie z poleceniami na stronie](https://hearing-screener.beyondhearing.org/phonak/lMePtS/welcome).
2. W **sprawozdaniu** proszę zapisać własne spostrzeżenia i dołączyć raport z wykonanego testu.
***
- [x] Test 2

1. Proszę wykonać test słuchowy online przygotowany przez firmę [Blamey Saunders hears zgodnie z poleceniami na stronie](https://blameysaunders.com.au/discover/test-your-hearing/). Jeżeli nie chcą Państwo podawać własnych adresów e-mail to jest możliwość skorzystania z [adresu tymczasowego TempMail](https://temp-mail.org/en/).
2. W **sprawozdaniu** proszę zapisać własne spostrzeżenia i dołączyć raport z wykonanego testu (opcja Print w przesłanym na adres e-mail raport - może być plik *.pdf).
***
- [x] Test 3

1. Proszę wykonać test słuchowy online [zgodnie z poleceniami na stronie](https://hearingtest.online/). Po wykonaniu wstępnego testu proszę zwiększyć rozdzielczość testu dla niskich częstotliwości (opcja `Alt Low [250-1500Hz]` w sekcji 3). Następnie proszę wykonać test jeszcze raz, ale ze zwiększoną rozdzielczością dla wyższych częstotliwości (opcja `Alt High [1500-8000Hz]` w sekcji 3).
2. W **sprawozdaniu** proszę zapisać własne spostrzeżenia i dołączyć raport z wykonanych testów (opcja `Print - Save - Bookmark` poniżej wykresu audiogramu):
  - testu oryginalnego
  - testu ze zwiększoną rozdzielczością dla niskich częstotliwości
  - testu ze zwiększoną rozdzielczością dla wysokich częstotliwości
***
### `Zadanie 2. Pomiary podstawowych parametrów dźwięku`
***
- [x] Test 1

1. Proszę znaleźć w najbliższym otoczeniu ścianę (o powierzchni dużo większej względem rozmiarów urządzenia mobilnego), stanąć w pewnej odległości od ściany i uruchomić dowolny utwór muzyczny. Następnie ([rysunek pomocniczy](https://github.com/MarcinEL/WIT-LAB1/blob/main/images/Zad2_img1.png)):
  - zbliżyć źródło dźwięku do ściany na pewnej wysokości od podłogi (jedna powierzchnia odbijająca) i posłuchać kilka sekund
  - umieścić źródło dźwięku blisko ściany i na podłodze (dwie powierzchnie odbijające) i posłuchać kilka sekund
  - umieścić źródło dźwięku na podłodze w rogu między dwoma ścianami (trzy powierzchnie odbijające) i posłuchać kilka sekund
2. W **sprawozdaniu** proszę zapisać własne spostrzeżenia dotyczące zmian, które zachodzą przy każdorazowej zmianie położenie źródła dźwięku. Istotne jest, aby materiał dźwiękowy w trakcie przemieszczania źródła dźwięku nie zmieniał swojego charakteru. Jakie zjawiska mogą mieć wpływ na zmiany odbieranego materiału dźwiękowego?
***
- [x] Test 2

1. Proszę uruchomić aplikację [dBMeter](https://github.com/MarcinEL/WIT-LAB1/tree/main/installs) w urządzeniu mobilnym i ustawić parametry aplikacji zgodnie z [podanymi](https://github.com/MarcinEL/WIT-LAB1/blob/main/images/Zad2_img2.jpg) ustawieniami.
2. Proszę umieścić urządzenie mobilne w pewnej odległości od ściany i uruchomić [plik dźwiękowy](https://github.com/MarcinEL/WIT-LAB1/blob/main/samples/rain_noise.wav), włączyć opcję logowania danych do pliku w aplikacji dBMeter -> [opcja `Save`](https://github.com/MarcinEL/WIT-LAB1/blob/main/images/Zad2_img3.jpg) oraz odczekać co najmniej 30 sekund, aby wykonać przynajmniej 30 pomiarów (logowanie do pliku odbywa się co 1 sekundę). Wyłączyć logowanie do pliku przyciskiem `Stop`.
3. Następnie umieścić urządzenie mobilne na podłodze w rogu między dwoma ścianami i wykonać identyczne pomiary jak w punkcie wyżej zapisując dane pomiarowe do kolejnego pliku (włączenie logowania do pliku przyciskiem `Save`).
4. Pliki z zapisanymi danymi opisującymi zmierzony poziom głośności w całym paśmie (kolumna dB(A)) oraz w podpasmach oktawowych (od 16Hz do 20kHz) z rozdzielczością co 1 sekundę można udostępnić bezpośrednio z [poziomu aplikacji](https://github.com/MarcinEL/WIT-LAB1/blob/main/images/Zad2_img4.jpg).
5. W **sprawozdaniu** proszę zamieścić wykresy przedstawiające zobrazowanie: średnich wartości mocy sygnału w każdym paśmie oraz poziomu głośności dla pomiaru z punktu 2 i punktu 3. W celach porównawnczych najlpiej, aby wykresy średniej mocy sygnału i poziomu głośności były nałożone na siebie. Proszę skorzystać z [szablonu](https://github.com/MarcinEL/WIT-LAB1/blob/main/dBMeter_visualize.py) oraz opisać swoje spostrzeżenia po wykonaniu tego testu.

***
- [x] Test 3

1. Proszę przygotować pustą butelkę (najlepiej szklaną) i zapisać/odczytać parametry:
  - odczytać i zapisać objętość butelki **V** (jednostka ml == cm^3)
  - zmierzyć i zapisać pole powierzchni **A** otworu w [szyjce butelki](https://github.com/MarcinEL/WIT-LAB1/blob/main/images/Zad2_img10.jpg)
  - zmierzyć i zapisać [długość szyjki](https://github.com/MarcinEL/WIT-LAB1/blob/main/images/Zad2_img9.jpg) **L**
2. Proszę obliczyć przybliżoną częstotliwość rezonansową takiego układu ([rezonator Helmholtz'a](http://hyperphysics.phy-astr.gsu.edu/hbase/Waves/cavity.html#c1)) za pomocą [kalkulatora online](http://hyperphysics.phy-astr.gsu.edu/hbase/Waves/cavity.html#c4). Należy zwrócić uwagę, aby dobrze obliczyć wszystkie parametry i zachować odpowiednie jednostki każdego z wymiarów (po wpisaniu wszystkich parametrów należy kliknąć w czerwony napis "frequency", który uruchamia skrypt wykonujący obliczenia).
3. Proszę uruchomić [aplikację](https://play.google.com/store/apps/details?id=org.intoorbit.spectrum) i ustawić parametry [dźwięku](https://github.com/MarcinEL/WIT-LAB1/blob/main/images/Zad2_img5.jpg), [zobrazowania](https://github.com/MarcinEL/WIT-LAB1/blob/main/images/Zad2_img6.jpg) oraz [inne](https://github.com/MarcinEL/WIT-LAB1/blob/main/images/Zad2_img7.jpg).
4. Proszę umieścić urządzenie mobilne blisko butelki z włączoną aplikacją do pomiaru widma i pobudzić układ do drgań przez wdmuchiwanie pod pewnym kątem powietrza w otwór szyjki butelki aż do uzyskania słyszalnego tonu oraz zapisać częstotliwość wykrytą i zmierzoną przez aplikację. Przydatną opcją w aplikacji może być resetowanie widoku [zobrazowania widma](https://github.com/MarcinEL/WIT-LAB1/blob/main/images/Zad2_img8.jpg).
5. Proszę dolać 100ml wody do pustej butelki i powtórzyć czynności z punktów 1, 2 i 4 (w punkcie 1. zmianie ulega tylko efektywna objętość butelki - zostaje pomniejszona o 100ml). Następnie proszę dolewać kolejne 100ml wody i powtarzać obliczenia i pomiar dopóki butelka się nie wypełni lub do momentu otrzymania 4 par obliczenia-pomiar.
6. W **sprawozdaniu** proszę zamieścić wyniki obliczeń zestawione z wynikami pomiarów w formie tabeli.
