# pyQT5-harjoituksia
Graafisen käyttöliittymän suunnitteluun ja toteutukseen liittyviä harjoituksia QT Designeria ja Pythonia käyttäen. Harjoituksessa luodaan kuulokkeiden ja mikrofonien testaukseen tarkoitettu sovellus, joka tuottaa äänisignaalin väliltä 1 Hz - 20 999 Hz.

![GUI](https://github.com/Raision-seudun-koulutuskuntayhtyma/pyQT5-harjoituksia/blob/main/ui.png)

## Asiakasvaatimukset
Käyttöliittymää tulee voida käyttää sekä näppäimistön että hiiren avulla.
1. Kaikkien kontrollien kohdalla hiiren kursorin on muututtava sormikursoriksi.
2. Liukusäätimen (Duration) arvo muuttuu nuolinäppäinten avulla 1 s ja sivunvaihtonäppäimillä 10 s.
3. kHz-nupin arvo muuttuu nuolinäppäimillä 1:llä ja sivunvaihtonäppäimillä 10:llä.
4. Muiden nuppien arvot muuttuvat nuolinäppäimillä 1:llä ja sivunvaihtonäppäimillä 9:llä.
5. Kontrollien arvoja voidaan muuttaa hiirellä a) vetämällä, b) klikkaamalla sekä c) rullaa kiertämällä.
6. Kontrolliem yhteyteen sijoitetaan indikaattori, joka näyttää kontrollin arvon numeerisena.
7. Kontrollista voi siirtyä seuraavaan kontrolliin sarkainnäppäimen avulla järjestyksessä liukusäädin -> nupit -> painike
8. Punaisessa 7-segmenttinäytössä näkyy valittu taajuus
