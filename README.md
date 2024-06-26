**Sovellus ravintola-arvosteluja varten**

Sovelluksen avulla voi kertoa ravintolakokemuksistaan muille käyttäjille. Sovellukseen voi jättää arvostelun vierailemastaan ravintolasta. Lisäksi sovelluksessa on viestialue, johon voi jättää viestejä etukäteen määritellyistä aihealueista.

Sovelluksen ominaisuuksia: 

- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
- Käyttäjä voi jättää arvostelun vierailemastaan ravintolasta. Arvostelu sisältää seuraavat osa-alueet:
  - Taustatiedot
      - Ravintolan nimi
      - Vierailuajankohta
  - Arvostelu asteikolla 1-5
      - Ruoka
      - Tunnelma
      - Palvelu
  - Vapaa palaute
- Käyttäjät voivat lukea muiden jättämiä arvosteluja ja etsiä arvosteluja ravintolan nimellä.
- Käyttäjät voivat kirjoittaa viestejä viestialueelle ja lukea muiden jättämiä viestejä.
- Käyttäjät voivat etsiä kaikki viestit, joiden osana on annettu sana.
- Ylläpitäjä voi poistaa tarvittaessa muiden jättämän arvostelun tai viestin. 
- Käyttäjät voivat jättää palautetta tai kehitysideoita sovelluksesta. 
- Vain ylläpitäjä voi nähdä jätetyt palautteet. 

- Ylläpitäjän oikeuksia voi testata luomalla uuden tunnuksen ja lisäämällä tuohon tunnukseen ylläpitäjän oikeudet komennolla: 
    UPDATE users SET admin=1 WHERE username='luomasi käyttäjätunnus';

**Sovellus ei ole testattavissa Fly.io:ssa**

**Ohjeet sovelluksen käynnistämiseen paikallisesti**

- Kloonaa tämä repositorio omalle koneellesi ja siirry sen juurikansioon. Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi:

DATABASE_URL=<tähän tietokannan-paikallinen-osoite>

SECRET_KEY=<tähän oma salainen-avain>

- Seuraavaksi aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla

$ python3 -m venv venv

$ source venv/bin/activate

$ pip install -r ./requirements.txt

- Määritä vielä tietokannan skeema komennolla

$ psql < schema.sql

- Nyt voit käynnistää sovelluksen komennolla

$ flask run
