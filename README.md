***

***

# Cyfrowa Technika Foniczna 2020Z

### **LABORATORIUM 1** | Pomiary podstawowych parametrów dźwięku za pomocą urządzeń mobilnych

#### Niezbędne oprogramowanie i sprzęt.
Przed przystąpieniem do wykonania ćwiczenia laboratoryjnego należy **pobrać i zainstalować** darmowe [oprogramowanie do wizualizcji, analizy i edycji plików dźwiękowych](https://www.sonicvisualiser.org/) w sekcji "Download" i dalej zgodnie z używanym system operacyjnym. Zalecane jest, aby odsłuchiwanie próbek dźwiękowych odbywało się za pomocą **słuchawek nausznych lub dousznych** (niezalecany jest odsłuch za pomocą wbudowanych lub zewnętrznych głośników komputerowych).

### Sprawozdania

Plik lub pliki ze sprawozdaniem (w dowolnym formacie: *.rtf, *.doc, *.docx, *.pdf, Markdown, LaTex) należy umieszczać w repozytorium [GitHub](https://github.com/). Po zalogowaniu się do systemu każdy powinien utworzyć nowe repozytorium o nazwie <CTF2020Z_SPR> i tam umieścić plik/pliki ze sprawozdaniem.

### Pliki dźwiękowe

Wszystkie niezbędne do wykonania ćwiczenia pliki dźwiękowe znajdują się w folderze `./Samples` w repozytorium.

***

***

### `Zadanie 1. Próbkowanie`

#### Teoria
> **Sygnał analogowy** jest sygnałem ciągłym w dziedzinie czasu i amplitudy. W celu przetworzenia takiego sygnału na **sygnał cyfrowy** najpierw należy dokonać próbkowania, czyli zamiany sygnału na sygnał dyskretny w czasie, a następnie kwantyzacji i kodowania tak, aby amplituda sygnału również była zmienną dyskretną.
> 
> Sygnał analogowy dźwiękowy jest zawsze próbkowany w stałych odstępach czasu (ze stałą częstotliwością próbkowania), co z matematycznego punktu widzenia oznacza mnożenie sygnału analogowego z ciągiem impulsów o określonym czasie trwania. Jest to tożsame ze splotem widm sygnałów w dziedzinie częstotliwości.
> 
> **Teoria o próbkowaniu** zakłada, że aby poprawnie zrekonstruować sygnał cyfrowy to sygnał analogowy musi być próbkowany przynajmniej z podwójną maksymalną częstotliwością występującą w sygnale. Można to wyjaśnić w dziedzinie czasu i częstotliwości:
> 
> - **W dziedzinie czasu** sygnał sinusoidalny może być w pełni określony cyfrowo za pomocą tylko dwóch punktów, co oznacza, że występuje tylko jeden sygnał sinusoidalny o częstotliwości mniejszej od połowy częstotliwości próbkowania, którego jeden okres przechodzi dokładnie przez te dwa punkty. Jest to oczywiście prawdą tylko wtedy, kiedy sygnałem próbkowanym jest sygnał sinusoidalny bez składowych harmonicznych, co oznacza, że pełna rekonstrukcja sygnału cyfrowego jest możliwa, gdy pasmo sygnału jest ograniczone do takiej częstotliwości, która określa jeden jego okres w dwóch punktach (sygnał sinusoidalny, którego jeden okres jest określony w dwóch punktach ma częstotliwość połowy częstotliwości próbkowania).
> - **W dziedzinie częstotliwości** w procesie próbkowania widmo sygnału próbkowanego jest powielane symetrycznie wokół wielokrotności częstotliwości próbkowania. Takie mnożenie ciągu impulsów próbkujących z sygnałem próbkowanym jest znane również jako modulacja PAM (*Pulse Amplitude Modulation*). W trakcie procesu próbkowania widmo ciągu impulsów próbkujących charakteryzującego się podstawową częstotliwością równą częstotliwości próbkowania i czasem trwania impulsu na tyle małym żeby zminimalizować błędy apertury jest splatane z widmem sygnału wejściowego. Oznacza to, że widmo sygnału wejściowego jest powielane na wielokrotnościach częstotliwości próbkowania. W celu rekonstrukcji takiego sygnału w przetworniku c/a należy odseparować od siebie część widma w paśmie podstawowym oraz powieleń tego widma. Jako, że pierwsze powielenie widma jest przesuniętym i lustrzanym odbiciem widma z pasma podstawowego na częstotliwości próbkowania to próbkowanie powinno odbywać się właśnie przynajmniej z podwójną częstotliwością pasma sygnału próbkowanego. 
> 
> Jeżeli sygnał analogowy nie jest próbkowany przynajmniej dwa razy szybciej niż wynika to z pasma sygnału próbkowanego lub odwrotnie - jeżeli sygnał wejściowy ma składowe częstotliwościowe większe niż wartość połowy częstotliwości próbkowania to widmo sygnału w paśmie podstawowym i przesunięte oraz lustrzane odbicia widma zachodzą na siebie. Po konwersji takiego sygnału z powrotem do sygnału analogowego będą słyszalne dodatkowe komponenty częstotliwościowe, które nie występowały w sygnale oryginalnym. Zjawisko to jest nazywane **aliasingiem**. W celu uniknięcia problemu aliasingu na wejściu przetwornika a/c stosuje się analogowy filtr antyaliasingowy, który ogranicza pasmo sygnału wejściowego do połowy częstotliwości próbkowania. Na wyjściu przetwornika c/a natomiast stosuje się filtr antylustrzany (rekonstruujący), który ma za zadanie stłumić zniekształcenia wynikające z działania praktycznego (nie idealnego) układu próbkująco-pamiętającego (wprowadzającego zniekształcenia typu sin(x)/x).

#### Polecenia
1. Uruchom oprogramowanie Sonic Visualiser i wczytaj plik [Oscillator_2_4_8_16kHz_PitchUp_and_PitchDown_Fs44100Hz.wav](/Samples/Oscillator_2_4_8_16kHz_PitchUp_and_PitchDown_Fs44100Hz.wav)*. Kółkiem myszy można zbliżać i oddalać widok w czasie, a przytrzymując lewy klawisz myszy i przesuwając w lewo i prawo można nawigować widokiem wczytanego sygnału. W panelu po prawej stronie można zmienić kolor zobrazowania próbek sygnału (karta nr 3 - `Waveform`).
2. Zobrazowanie widma sygnału proszę uruchomić dodając kolejny panel za pomocą polecenia `Pane -> Add Spectrum`. W panelu po prawej stronie w karcie nr 2 można zmienić parametry analizy widmowej (`Colour` - kolor, `Bins` - skala częstotliwościowa i sposób prezentacji wykresu, `Scale` - skala amplitudowa, `Window` - szerokość okna analizy, nakładanie się okien, nadpróbkowanie). Polecane ustawienia, jeśli są inne: skala logarytmiczna w częstotliwości i amplitudzie, okno analizy 4096, nakładanie 50%, zmiana kształtu okna -> `File -> Preferences... -> Analysis -> Spectral analysis window shape: Nutall`.
3. Dodatkowo zobrazowanie widma w czasie (spektrogram) proszę uruchomić w kolejnym panelu za pomocą polecenia `Pane -> Add Spectrogram`. W panelu po prawej stronie w karcie nr 3 proszę zmienić, jeśli ustawienia są inne, skala mocy dBV^2, szerokość okna analizy 2048 i nakładanie 50%.
4. Proszę odsłuchać plik dźwiękowy od początku do końca analizując zobrazowanie widma i korelując wrażenia słuchowe z tym, co można zauważyć na widmie.
5. W **sprawozdaniu** proszę zapisać wnioski i opisać zaobserwowane zjawisko.

    **plik dźwiękowy to suma sygnałów sinusoidalnych o częstotliwościach początkowych 2kHz, 4kHz, 8kHz i 16kHz o zmiennej liniowo wysokości dla wszystkich tonów w czasie (o 4 oktawy do góry - częstotliwości x2 dla każdej oktawy i później 4 oktawy w dół), częstotliwość próbkowania sygnału 44100Hz, rozdzielczość bitowa 32b (float).*
    
6. W oprogramowaniu Sonic Visualiser proszę utworzyć nową sesję (`File -> New Session`), otworzyć plik [Original_piano.wav](/Samples/Original_piano.wav), a następnie wczytać dwa kolejne pliki (`File -> Import More Audio...`), a mianowicie [Original_piano_sampled_at8kHz_sample1.wav](/Samples/Original_piano_sampled_at8kHz_sample1.wav) oraz [Original_piano_sampled_at8kHz_sample2.wav](/Samples/Original_piano_sampled_at8kHz_sample2.wav). W trakcie odsłuchiwania można zmieniać aktualnie odwtarzany plik włączając opcję `Playback -> Solo Current Pane` i klikając na panel z plikiem, który w danym momencie chcemy odsłuchiwać.
7. W **sprawozdaniu** proszę opisać czym różnią się pliki [Original_piano_sampled_at8kHz_sample1.wav](/Samples/Original_piano_sampled_at8kHz_sample1.wav) oraz [Original_piano_sampled_at8kHz_sample2.wav](/Samples/Original_piano_sampled_at8kHz_sample2.wav) i z czego może wynikać różnica brzmienia w porównaniu z oryginalną ścieżką [Original_piano.wav](/Samples/Original_piano.wav). Do analizy można wykorzystać zobrazowanie widma (jak w poprzednich punktach), jako oddzielne panele ALBO można nałożyć na siebie kilka wizualizacji za pomocą polecenia `Layer -> Add Spectrum` / `Layer -> Add Spectrogram`.

***
