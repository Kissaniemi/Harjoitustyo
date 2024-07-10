# Määrittelydokumentti

## Algoritmit ja Tekoäly Harjoitustyö

Tietojenkäsittelytieteen kandiohjelma (TKT)

Harjoitustyön toteutus: Python
Koodissa käytetty kieli: Englanti
Dokumentoinnin kieli: Suomi

Vertaisarviointi mahdollista muille Python-projekteille joissa käytetty kieli joko Suomi/Englanti


## Harjoitustyön aihe ja vaatimusmäärittely

Harjoiustyön aihe on kurssin valmiista aihe-ehdotuksista valittu MiniMax-algoritmi Connect4/Neljän suora-pelille.
Vaatimusmäärittely perustuu täysin valmiiksi annettuun määrittelyyn.

Ohjelman ydin on minimax-algoritmi joka generoi/laskee mahdollisimman hyvän siirron tietyn ajan puitteissa (ei vielä määritelty). Algoritmia tehostetaan alpha-beta-karsinnalla ja iteratiivisella syvenemisellä.

Vähimmäisvaatimuksena koodin pitää toimia komentoriviltä, graafinen käyttöliittymä ei oleellista työn ytimen kannalta.

Tarkoitus on pystyä antamaan ohjelmalle pelilaudan tilanne ja kumman pelaajan vuoro jonka perusteella se generoi seuraavan siirron.

## Connect4:sta

Kahden pelaajan peli, joka pelataan 7x6 kokoisella pelilaudalla. Pelaajat "tiputtavat" laudalle vuoron perään kiekkoja (kummallakin pelaajalla oma värinsä)
Esimerkiksi ristinollasta poiketen, kiekkoa ei voi pistää mihin kohtaan peliruutua tahansa, vaan sillä on aina maksimissaan 7 mahdollista kohtaa mihin se voi tulla. Joko pelilaudan alareunaan jos sarakkeessa ei ole jo toista kiekkoa tai toisen kiekon päälle.
 
Connect4 on ratkaistu peli, eli jos aloittaja pelaa täydellisesti tämä voittaa aina.

## Lähteet:
- 
