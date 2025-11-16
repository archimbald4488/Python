# Python
### Täällä pidän kaikki python-projektini.

#### Data Structures/
Tämä kansio sisältää Data Structures & Algorithms yliopistokurssin viikkotehtäviä.
Tehtävissä mm. luodaan erilaisia algoritmeja ja tietojentallennustyyppejä.

#### MongoDB/
Tämä kansio sisältää projektin jossa harjoittelin tietokantojen käyttöä MongoDB:llä. 
Kansion projekti luo ja alustaa kolme erillistä tietokantaa, joita voi muokata yksinkertaisella terminaalisovelluksella.

#### storelocator.py<br>
Tämä tiedosto on lyhyt skripti joka tallentaa julkisesta API:sta haettuja tietoja joulukoristeita myyvistä kaupoista.
Projekti on toteutettu kaverille hänen pyynnöstään.

#### omakieli.py<br>
Tämä tiedosto on oman ohjelmointikieleni suorittaja. Se toimii seuraavalla tavalla:<br>
Suoritettava ohjelma muodostuu riveistä, joista jokainen on yksi seuraavista:

**PRINT** [arvo]: tulostaa annetun arvon<br>
**MOV** [muuttuja] [arvo]: asettaa muuttujaan annetun arvon<br>
**ADD** [muuttuja] [arvo]: lisää muuttujaan annetun arvon<br>
**SUB** [muuttuja] [arvo]: vähentää muuttujasta annetun arvon<br>
**MUL** [muuttuja] [arvo]: kertoo muuttujan annetulla arvolla<br>
[kohta]: määrittelee kohdan, johon voidaan hypätä muualta<br>
**JUMP** [kohta]: hyppää annettuun kohtaan<br>
**IF** [ehto] JUMP [kohta]: jos ehto pätee, hyppää annettuun kohtaan<br>
**END**: lopettaa ohjelman<br>
Ohjelmaa suoritetaan rivi kerrallaan ensimmäisestä rivistä aloittaen. Ohjelma päättyy, kun vastaan tulee komento END tai suoritus menee ohjelman viimeisen rivin yli.

Jokaisessa ohjelmassa on 26 muuttujaa, joiden nimet ovat A...Z. Jokaisen muuttujan arvo on 0 ohjelman alussa. Merkintä [muuttuja] viittaa tällaiseen muuttujaan.

Kaikki ohjelman käsittelemät arvot ovat kokonaislukuja. Merkintä [arvo] viittaa joko muuttujaan tai kokonaislukuna annettuun arvoon.

Merkintä [kohta] on mikä tahansa kohdan nimi, joka muodostuu pienistä kirjaimista a...z sekä numeroista 0...9. Kahdella kohdalla ei saa olla samaa nimeä.

Merkintä [ehto] tarkoittaa ehtoa muotoa [arvo] [vertailu] [arvo]. Tässä [vertailu] on aina yksi seuraavista: ==, !=, <, <=, > tai >=.

Ohjelma annetaan listana. Jokainen listan alkio on yksi ohjelman rivi. Funktio palauttaa listana kaikki PRINT-komentojen tulokset ohjelman suorituksen aikana.

Ohjelman funktiot eivät toteuta virheenkäsittelyä, joten älä kirjoita väärin!

Tiedostosta löytyy ajettavaksi esimerkkiohjelma (if main -lohkosta), joka tulostaa alkulukuja.
