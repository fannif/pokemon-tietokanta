### Käyttötapaukset

Käyttäjänä haluan voida luoda sovellukseen tilin, minkä jälkeen voin aina sisään kirjautuessani katsella, lisätä ja muokata nappaamiani pokemoneja. Käyttäjänä haluan myös pystyä muuttamaan salasanaani tai poistamaan koko tilini.

Kukin pokemon on yhtä tai useampaa tyyppiä, ja useampi pokemon voi olla samaa tyyppiä. Pokemon on aina jotain pokemonlajia, ja yhtä pokemonlajia voi olla useampi pokemon. Tietokannassa tulee siis olla erikseen taulu pokemonyksilöille, pokemonlajille, pokemonin tyypille ja käyttäjälle.

Käyttäjänä voisin pystyä hallinnoimaan nappaamiani pokemonyksilöitä. Niitä voi olla kuinka monta tahansa, mutta kuhunkin yksilöön liittyisi vain yksi käyttäjä. Käyttäjänä haluan voida poistaa tai lisätä pokemonyksilöitä tai muuttaa niihin liittyvää tietoa. 

Pokemonlajin ja tyypin välillä on monen suhde moneen -yhteys, koska yksi pokemonlaji voi olla montaa tyyppiä, ja samaan tyyppiin voi kuulua monta pokemonlajia.

Käyttäjänä tarvitsen käyttäjätunnuksen ja salasanan.
Pokemonyksilöilläni on ainakin lempinimi ja level, ja nappaamispäivämäärä sekä tieto siitä, kuuluuko se suosikkeihini.
Pokemonlajilla on nimi ja kuvaus sekä tieto siitä, onko se legendaarinen pokemon.
Pokemonin tyypillä on nimi.

Käyttäjänä haluan pystyä näkemään, kuinka monta pokemonia muut käyttäjät ovat napanneet. Myös jonkinlainen tieto parhaista käyttäjistä olisi näkyvillä (esimerkiksi eniten legendaarisia pokemoneja omistavien käyttäjien ja heidän legendaaristen pokemonlajiensa määrä sekä kaikki tunnetut pokemonlajit napanneet käyttäjät).

Sovelluksessa on siis seuraavanlaisia toimintoja:
- Käyttäjällä olevien pokemonien hakeminen nimen, lajin tai suosikkistatuksen (pelkästään suosikit tai kaikki yksilöt) perusteella.
- Pokemonien listaaminen nimen, levelin tai päivämäärän mukaan järjestyksessä.
- Uusien pokemonien ja pokemonlajien lisääminen.
- Käyttäjien pokemonmäärien listaaminen käyttäjittäin.
- Eniten legendaarisia pokemoneja napanneiden käyttäjien ja heidän legendaaristen pokemonlajiensa määrän listaaminen.
- Kaikki pokemonlajit napanneiden käyttäjien listaaminen.
- Pokemonin kehittyminen (pokemonin lajia muutetaan).
- Pokemonin lempinimen, levelin sekä suosikkistatuksen muuttaminen, ja pokemonin poistaminen.
- Käyttäjä voi luoda tai poistaa tilin tai vaihtaa salasanaansa.

#### Käyttötapausten SQL-kyselyt:
##### Käyttäjällä olevien pokemonien hakeminen:
Ensin on haettava lomakkeeseen täytetyn pokemonlajin id kyselyllä SELECT id FROM Species WHERE name = "laji"; (Tässä laji korvataan siis kenttään annetulla lajin nimellä.) Sitten päästään tekemään varsinaisia hakuja. Alla laji_id tarkoittaa edellisessä kyselyssä haettua id:tä, kayttaja_id käyttäjän id:tä ja nimi lomakkeeseen kirjoitettua pokemonin lempinimeä.

Jos haetaan sekä nimen että lajin että suosikkistatuksen perusteella, kysely on SELECT * FROM Individual WHERE account_id = kayttaja_id AND nickname = "nimi" AND favourite = True AND species_id = laji_id;

Jos haetaan nimen ja suosikkistatuksen perusteella, kysely on SELECT * FROM Individual WHERE account_id = kayttaja_id AND nickname = "nimi" AND favourite = True;

Jos haetaan lajin ja suosikkistatuksen perusteella, kysely on SELECT * FROM Individual WHERE account_id = kayttaja_id AND favourite = True AND species_id = laji_id;

Jos haetaan nimen ja lajin perusteella, kysely on SELECT * FROM Individual WHERE account_id = kayttaja_id AND nickname = "nimi" AND species_id = laji_id;

Jos haetaan vain lempinimen perusteella, kysely on SELECT * FROM Individual WHERE account_id = kayttaja_id AND nickname = "nimi";

Jos haetaan vain lajin perusteella, kysely on SELECT * FROM Individual WHERE account_id = kayttaja_id AND species_id = laji_id;

Jos haetaan vain suosikkipokemoneja, kysely on SELECT * FROM Individual WHERE account_id = kayttaja_id AND favourite = True;

Jos puolestaan mitään rajausta ei tehdä, haku palauttaa vain listan käyttäjän kaikista pokemonyksilöistä, jolloin kysely on SELECT * FROM Individual WHERE account_id = kayttaja_id;

##### Pokemonien listaaminen järjestyksessä nimen, levelin tai päivämäärän mukaan:
Kyselyissä otetaan myös Species-taulu mukaan, koska kun pokemonit listataan, näytetään myös lajiin liittyvää tietoa.

Jos järjestys halutaan lempinimen mukaan, kysely on SELECT * FROM Individual JOIN Species ON Individual.species_id = Species.id WHERE Individual.account_id = kayttaja_id ORDER BY Individual.nickname;

Jos järjestys halutaan levelin mukaan, kysely on SELECT * FROM Individual JOIN Species ON Individual.species_id = Species.id WHERE Individual.account_id = kayttaja_id ORDER BY Individual.level;

Jos puolestaan järjestys halutaan nappaamispäivämäärän mukaan, kysely on SELECT * FROM Individual JOIN Species ON Individual.species_id = Species.id WHERE Individual.account_id = kayttaja_id ORDER BY Individual.date_caught;

##### Uusien pokemonyksilöiden lisääminen:
Kun lisätään uutta pokemonyksilöä, selvitetään ensin sen lajin id kyselyllä "SELECT id FROM Species WHERE name = "laji";". Tässä laji korvataan lomakkeeseen kirjoitetulla lajilla. Jos lajia ei löytyisi, niin se pitää luoda ensin. Merkitään saatua id:tä laji_id.

Kun lajin id on selvitetty, yksilö voidaan lisätä kyselyllä "INSERT INTO Individual (date_caught, nickname, level, favourite, account_id, species_id) VALUES (lisäysajanhetki, "nimi", 1, 1, kayttaja_id, laji_id);". Tässä nimi korvattaisiin lisättävän yksilön lempinimellä ja ensimmäinen ykkönen sen levelillä. Toinen ykkönen kuvaa totuusarvoa true, ja sen arvo riippuu siitä, valittiinko, että pokemonyksilö kuuluu suosikeihin. Lisäysajanhetki kuvaa, että nappaamispäivämääräksi tulee sen hetkinen päivämäärä.

##### Uuden pokemonlajin lisääminen:
Uutta pokemonlajia lisättäessä käytetään kyselyä "INSERT INTO Species (name, description, legendary) VALUES ("nimi", "kuvaus", 1);". Tässä nimi korvataan lajin nimellä ja kuvaus kuvauksella. Vastaavasti kuin edellisessä kohdassa, tässäkin kohdassa 1 kuvaa totuusarvoa true, ja riippuu siitä määritetäänkö pokemonlaji legendaarikseksi lomakkeessa.

Koska lajin ja tyypin välillä on monen suhde moneen -tyyppinen yhteys, on niiden välillä liitostaulu. Niinpä lajin lisäyksen yhteydessä lisätään myös liitostauluun vähintään yksi rivi. Tämä tehdään kyselyllä "INSERT INTO SpeciesType (species_id, type_id) VALUES (laji_id, tyyppi_id);". Ohjelmassa tyypin id on saadaan suoraan käyttäjän valitsemasta listasta, joten sitä ei enää tässä vaiheessa tarvitse hakea kyselyllä. Listaan tyypit on saatu kyselyllä SELECT * FROM Type;

##### Tyyppien lisääminen:
Tyyppien lisääminen ei kuulu käyttäjälle näkyviin toiminnallisuuksiin. Se kuitenkin tehdään, mikäli Type-taulu on tyhjä, kyselyllä "INSERT INTO Type (name) VALUES ("tyyppi");". Tässä tyyppi korvataan vuorotellen kaikkien 18:n pokemontyypin nimillä.

##### Pokemonien määrien listaaminen käyttäjittäin:
Käyttäjäkohtaiset pokemonmäärät listataan kyselyllä SELECT Account.username, COUNT(Individual.id) FROM Account LEFT JOIN Individual ON Individual.account_id = Account.id GROUP BY Account.username;

##### Eniten legendaarisia pokemoneja napanneiden käyttäjien ja legendaaristen lajien määrien listaaminen:
Käyttäjät, joilla on vähintään yksi legendaarinen pokemon, ja heidän legendaaristen lajiensa määrä listataan seuraavalla kyselyllä (järjestyksessä eniten legendaarisia napanneesta alaspäin): 
"SELECT Account.id, Account.username, COUNT(Species.id) AS amount FROM Account LEFT JOIN Individual ON Account.id = Individual.account_id JOIN Species ON Individual.species_id = Species.id WHERE Species.legendary = '1' GROUP BY Account.id HAVING COUNT(Species.id) > 0 ORDER BY COUNT(Species.id) DESC LIMIT 10;

##### Kaikki pokemonlajit napanneiden käyttäjien listaaminen:
Kaikki tietokannassa olevat pokemonlajit napanneiden käyttäjien (enintään kymmenen käyttäjää) listaaminen tapahtuu kyselyllä "SELECT Account.username, COUNT(DISTINCT Species.name) FROM Account LEFT JOIN Individual ON Account.id = Individual.account_id JOIN Species ON Individual.species_id = Species.id GROUP BY Account.username HAVING COUNT(DISTINCT Species.name) = (SELECT COUNT(*) FROM Species) LIMIT 10;"

##### Pokemonyksilön tietojen muokkaaminen:
Alla merkitään käsiteltävän yksilön id:tä yksilon_id.

Pokemonin suosikkistatuksen muuttaminen: "UPDATE Individual SET favourite=1 WHERE Individual.id = yksilon_id;". Tässä oletetaan, että suosikkistatus muutettiin arvoon true. Jos yksilö haluttaisiin poistaa suosikeista, niin ykkösen tilalla olisi 0.

Pokemonin lempinimen muuttaminen: UPDATE Individual SET nickname = "uusi_lempinimi" WHERE Individual.id = yksilon_id;

Pokemonin levelin muuttaminen: UPDATE Individual SET level = uusi_level WHERE Individual.id = yksilon_id;

Pokemonin lajin muuttaminen (siis käytännössä pokemonin kehittyminen) tapahtuu sillä tavalla vastaavasti kuin yksilöä lisättäessä, että jos uusi laji on tietokannassa, niin ensin selvitetään lomakkeeseen kirjoitetun lajin nimen perusteella laji id kyselyllä "SELECT id FROM Species WHERE name = "laji";". Merkitään saatua id:tä lajin_id. Jos lajia ei ole tietokannassa, lisätään laji ensin ylläolevan lajin lisäämiseen liittivän kohdan kyselyiden mukaisesti. 

Kun uuden lajin id on selvillä, pokemonin lajia muutetaan kyselyllä UPDATE Individual SET species_id = lajin_id WHERE Individual.id = yksilon_id;

Jos monen sarakkeen arvo muutetaan kerralla, yhdistetään edellisiä kyselyitä. Esimerkiksi lempinimen ja levelin muuttaminen kerralla tehtäisiin kyselyllä UPDATE Individual SET nickname = "uusi_lempinimi", level = uusi_level WHERE Individual.id = yksilon_id;

##### Pokemonyksilön poistaminen:
Pokemonyksilö poistetaan kyselyllä "DELETE FROM Individual WHERE id = yksilon_id;". Tässäkin yksilon_id kuvaa poistettavan yksilön id:tä.

##### Käyttäjätilin luominen:
Uusi käyttäjätili luodaan kyselyllä "INSERT INTO Account (username, password) VALUES ("kayttajanimi", "salasana");". Tässä käyttäjänimen kohdalle laitetaan lomakkeesta saatava käyttäjänimi ja salasanan kohdalle salasana. Ennen käyttäjän luomista varmistetaan kuitenkin, ettei käyttäjänimi ole jo varattu. Tämä tehdään hyödyntäen kyselyä "SELECT * FROM Account WHERE username = "kayttajanimi";".

##### Käyttäjän salasanan vaihtaminen:
Käyttäjän salasana vaihdetaan kyselyllä "UPDATE Account SET password = "uusi_salasana" WHERE id = kayttajan_id;". Tässä uusi_salasana korvattaisiin lomakkeesta saadulla uudella salasanalla ja kayttajan_id muokattavan käyttäjän id:llä.

##### Käyttäjätilin poistaminen:
Käyttäjätilin poistaminen onnistuu kyselyllä "DELETE FROM Account WHERE id = kayttajan_id;", missä kayttajan_id on poistettavan käyttäjän id.
