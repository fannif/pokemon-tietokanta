## Tietokannan kuvaus

Tietokantatauluilla on yhteistä, että paria poikkeusta lukuunottamatta mikään niiden sarake ei saa jäädä tyhjäksi.

#### Account
Account-taulu sisältää sovelluksen käyttjien tiedot. Kukin rivi kuvaa yhtä käyttäjää. Attribuutteina taulussa on kokonaislukumuotoisen id:n lisäksi merkkijonot käyttäjänimi (username) ja salasana (password), koska muita tietoja käyttäjästä ei sovelluksessa käytetä. Käyttäjänimeä ja salasanaa käytetään pääosin sisäänkirjautumisessa. Id:tä käytetään muun muassa siinä, että näytetään käyttäjälle vain hänen omia pokemonejaan. Käyttäjään voi liittyä nolla tai useampi Individual-taulun riviä.

Account-taulua ei ole denormalisoitu. Denormalisointia ei koettu taululle tarpeelliseksi.

Account-taulu on toinen sovelluksen CRUD-tauluista. Account-taulun rivejä voi nimittäin muokata sovelluksessa salasanaa vaihtamalla, ja taulun riveistä löytyy myös listaus, tietojenkatselu ja poistomahdollisuus.

#### Individual
Individual-taulun kukin rivi sisältää yhden pokemonyksilön tiedon. Rivissä on kokonaislukumuotoinen pääavain sekä viiteavaimet yksilön omistavaan käyttäjään ja yksilön lajiin. Näiden lisäksi rivillä on merkkijonomuotoinen lempinimi (nickname), kokonaisluku taso (level), totuusarvo suosikki (favourite) ja lisäyspäivämäärä (date_caught). Favourite kuvaa sitä, kuuluuko yksilö käyttäjän suosikeihin vai ei. Lempinimeä ja tasoa käytetään yksilön kuvaamiseen. Lisäyspäivämäärää käytetään yksilöiden järjesteämisessä.

Myöskään Individual-taulua ei olla denormalisoitu. Se on toinen sovelluksen CRUD-tauluista, sillä käyttäjä voi listata yksilönsä, katsoa niiden tietoja ja muokata ja poistaa niitä.

#### Species
Species-taulun rivit kuvaavat pokemonlajeja. Yhteen Species-taulun riviin voi liittyä nolla tai useampi Individual-taulun riviä. Lisäksi Species-taulun ja Type-taulun välillä on monen suhde moneen -yhteys, joka on korvattu liitostaululla SpeciesType. Niinpä yhteen Species-taulun riviin voi liittyä yksi tai useampi SpeciesType-taulun rivi.

Species-taulussa on attribuutteina id:n lisäksi merkkijono name, joka kertoo lajin nimen, merkkijono description, joka sisätää kuvauksen lajista, ja totuusarvo legendary, joka on tosi, jos pokemonlaji on legendaarinen, ja muuten epätosi.

Species-taulua ei olla denormalisoitu.

#### Type
Type-taulun kukin rivi kuvaa pokemontyyppiä. Tyypillä on id:n lisäksi merkkijono name, joka kuvaa tyypin nimeä. Tyyppejä on kahdeksantoista erilaista, ja ne kaikki luodaan tietokantaan valiiksi, mikäli taulu on tyhjä.

Yhteen Type-taulun riviin voi liittyä nolla tai useampi SpeciesType-taulun rivi. Type-taulua ei ole denormalisoitu.

#### SpeciesType
SpeciesType on liitostaulu, joka yhdistää Species- ja Type-taulut. Taulussa on siten attribuutteina viiteavaimet species_id ja type_id Species- ja Type-tauluihin. Taulun viiteavaimet saavat olla hetkellisesti tyhjiä, joten kenttiä ei CREATE TABLE -lauseessa ole merkattu pakollisiksi. Rivin luonnin yhteydessä viiteavaimiin lisätään kuitenkin arvot.

Liitostauluakaan ei ole denormalisoitu. Tauluun on lisätty unikki indeksi viiteavainten yhdistelmän perusteella.


### CREATE TABLE -lauseet

#### Account
`CREATE TABLE Account (
	id INTEGER NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);`

#### Individual
`CREATE TABLE Individual (
	id INTEGER NOT NULL, 
	date_caught DATETIME, 
	nickname VARCHAR(144) NOT NULL, 
	level INTEGER NOT NULL, 
	favourite BOOLEAN NOT NULL, 
	account_id INTEGER NOT NULL, 
	species_id INTEGER NOT NULL, 
	PRIMARY KEY (id),
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(species_id) REFERENCES species (id)
);`

#### Species
`CREATE TABLE Species (
	id INTEGER NOT NULL, 
	name VARCHAR(144) NOT NULL, 
	description VARCHAR(512), 
	legendary BOOLEAN NOT NULL, 
	PRIMARY KEY (id)
);`

#### Type
`CREATE TABLE Type (
	id INTEGER NOT NULL, 
	name VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
);`

#### SpeciesType
`CREATE TABLE SpeciesType (
	id INTEGER NOT NULL, 
	species_id INTEGER, 
	type_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(species_id) REFERENCES species (id), 
	FOREIGN KEY(type_id) REFERENCES type (id)
);`
