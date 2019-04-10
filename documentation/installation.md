# Asennusohje

### Sovelluksen käyttöönotto Herokussa
Aloittaaksesi sovelluksen käytön Herokussa, siirry ensin sovelluksen sivulle README.md-tiedostossa olevasta linkistä. Linkki ohjaa sovelluksen etusivulle. Käyttöä varten tarvitset käyttäjätilin, jonka voit luoda sivun oikeassa ylälaidassa olevasta Sign up-linkistä. Valitse itsellesi vähintään neljä merkkiä pitkä käyttäjänimi (mikäli käyttäjänimi on varattu, on sinun keksittävä jokin toinen nimi) ja vähintään nelimerkkinen salasana, jotka pääset täyttämään avautuvaan lomakkeeseen. Kun olet luonut käyttäjätilin, sinut ohjataan kirjautumissivulle.

Kun sinulla on käyttäjätunnukset, pääset kirjautumaan sovellukseen kirjautumissivulta. Kirjautumissivulle pääsee yläoikealla olevasta Log in-linkistä. Sisäänkirjautuminen tapahtuu kirjoittamalla lomakkeen kenttiin oma käyttäjänimi ja salasana.

Kirjauduttuasi sisään, olet valmis käyttämään sovellusta.

### Sovelluksen paikallinen käyttöönotto
Käyttääksesi sovellusta paikallisesti, lataa ensin sovellus tietokoneellesi. Tämän voit tehdä sovelluksen sisältävän GitHub-repositorion oikeassa ylälaidassa olevaa vihreää Clone or download -nappia painamalla. Valitse avautuvasta valikosta vaihtoehto Download ZIP.

Kun olet ladannut ZIP-tiedoston tietokoneellesi, siirrä se kansioon, jonka alle haluat Pokemon-tietokanta -sovelluksen tulevan. Tämän jälkeen klikkaa ZIP-tiedostoa hiiren oikealla painikkeella, ja valitse vaihtoehto Pura tänne (Extract here). Purettuasi tiedoston, syntyy kansioosi alikansio pokemon-tietokanta-master. Voit nyt poistaa ZIP-tiedoston.

Nyt sovellus on ladattuna koneellesi. Mene komentokehotteessa pokemon-tietokanta-master -kansion sisälle, ja luo kansioon Python-virtuaaliympäristö komennolla python3 -m venv venv (Linuxia käyttäessä). Tämän jälkeen aktivoi luotu virtuaaliympäristö komennolla venv/bin/activate. (Tämä komento on ajettava joka kerta ennen sovelluksen käyttöä). Tämän jälkeen voit käynnistää sovelluksen edelleen pokemon-tietokanta-master -kansion sisällä ollessasi komennolla python3 run.py. Sovellus käynnistetaan joka kerta samassa kansiossa tällä samalla komennolla.

Kun sovellus on käynnissä, pääset käyttämään sitä seuraamalla "Sovelluksen käyttöönotto Herokussa" -kohdassa olevia rekisteröitymis- ja sisäänkirjautumisohjeita.

### Sovelluksen asentaminen palvelimelle
Tässä ohjeessa oletetaan, että asennus halutaan tehdä Herokuun.

Sovelluksen käyttöönottamiseksi Herokussa suorita ensin kohdan "Sovelluksen paikallinen käyttöönotto" -ohjeet viimeistä ohjekappaletta lukuunottamatta. Kun tämä on tehty, lisätään sovellukselle Gunicorn-web-palvelin. Tämä tehdään ajamalla komentokehotteessa sovelluskansiossa (pokemon-tietokanta-master) ollessa komento pip install gunicorn.

Heroku tarvitsee sovelluksen riippuvuudet, joten samassa kasiossa ajetaan komento pip freeze > requirements.txt. Avaa sen jälkeen luotu requirements.txt -tiedosto haluamassasi tekstieditorissa, ja poista sieltä rivi pkg-resources==0.0.0. Aja vielä tämän jälkeen komento echo "web: gunicorn --preload --workers 1 hello:app" > Procfile.

Kun kyseiset komennot on suoritettu, kirjaudu komentoriviltä sisään Herokuun. Tämän jälkeen aja komento heroku create pokemon-database. Lisää vielä versionhallinnalle tieto Herokusta komennolla git remote add heroku https<i></i>://git<i></i>.heroku.<i></i>com/pokemon-database.git Lopuksi lähetä sovellus Herokuun seuraavalla komentosarjalla:
git add .
git commit -m "Sovellus siirretty Herokuun"
git push heroku master
