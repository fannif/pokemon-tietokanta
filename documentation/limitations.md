## Sovelluksen rajoitteet ja puuttuvat toiminnallisuudet

Sovelluksessa on käytön kannalta pieniä rajoitteita. Esimerkiksi tilanne, jossa käyttäjä pystyisi kehittämään pokemoninsa yksinkertaisesti vain painamalla jotain valmista Kehitä-nappia, ei ole sovelluksessa mahdollinen. Sovelluksessa pokemonin kehittäminen pitää tehdä pokemonin lajia muuttamalla niin, että mahdollisesti käyttäjä joutuu ensin myös lisäämään lajin tietokantaan. Tämä ei ole käyttäjän kannalta kovin tehoksta.

Pokemonyksilöiden haku päätettiin toteuttaa niin, että esimerkiksi lempinimellä hakiessa haetaan täsmälleen kyseistä lempinimeä. Tämä kuitenkin rajoittaa hiukan hakumahdollisuuksia, koska usein hauissa haetaan niin, että riittää, että sana sisältää haettavan merkkijonon. Tämän sovelluksen tapauksessa kuitenkin näytetään vain ne yksilöt joiden lempinimi on täsmälleen sama, kuin kirjoitettu merkkijono (paitsi jos merkkijono on tyhjä, jolloin haetaan kaikki lempinimet).

Käyttäjän poistamiseen liittyy myös pieni laajassa käytössä mahdollisesti ongelmaksi muodostuva seikka. Kun käyttäjä poistetaan, ei hänen lisäämiä yksilöitään kuitenkaan poisteta. Kukaan muu ei kuitenkaan käytä tai tarvitse kyseisiä yksilöitä. Näin ollen suuressa käytössä käyttäjiä poistaessa tietokantaa kerääntyy turhaa dataa, joka vie tilaa.

Sovelluksesta päätettiin tietoisesti jättää pois mahdollisuus pokemonlajien listaamiseen siltä varalta, että joku käyttäjä lisäisi lajiksi jotain loukkaavaa. Tällä järjestelyllä toiset käyttäjät eivät joutuisi näkemään luokkaavaa lajia. Kuitenkin tästä aiheutuu pienni rajoite. Etusivulla on listattuna käyttäjät, jotka ovat saaneet kaikki pokemonit. Kuitenkin koska kaikkia lajeja ei voi nähdä mistään, voi halukkaan olla vaikea päästä listalle, kun ei tiedä, mitä kaikkia lajeja tietokannassa on.

Sovelluksessa ei ole erikseen järjestelmänvalvojia. Näin ollen kukaan ei toistaiseksi voi esimerkiksi poistaa häirköiviä käyttjiä tai virheellisiä pokemonlajeja. Järjestelmänvalvojien lisääminen tulevaisuudessa olisi kuitenkin melko suoraviivaista.

Sovellukseen kaavailtiin alunperin mahdollisuutta hakea pokemonyksilöitä myös sen mukaan, ovatko ne legendaarisia. Toiminnallisuus päätettiin kuitenkin jättää pois, koska haussa oli jo vastaavalla tavalla toimiva haku suosikkistatuksen perusteella.

Sovellukseen olisi myös voinut olla hyvä lisätä enemmänkin asiaa käyttäjän tiedot näyttävälle Account info -sivulle. Alkuperäisiin ideoihin kuului esimerkiksi, että kyseiselle sivulle voitaisiin laittaa käyttäjän pokemonien kokonaismäärä ja legendaaristen määrä. Kuitenkin nämä toiminnallisuudet tuntuivat melko turhilta, joten ne päätettiin jättää pois.
