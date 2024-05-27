**Sovellus ravintola-arvosteluja varten**

Sovelluksen avulla voi kertoa ravintolakokemuksistaan muille käyttäjille. Sovellukseen voi jättää arvostelun vierailemastaan ravintolasta. Lisäksi sovelluksessa on keskustelualue, jossa voi kysellä muilta käyttäjiltä ravintolasuosituksia. 

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
- Käyttäjät voivat lukea muiden jättämiä palautteita ja etsiä arvosteluja ravintolan nimellä.
- Käyttäjät voivat kirjoittaa viestejä keskustelupalstalle ja lukea muiden jättämiä viestejä.
- Käyttäjät voivat etsiä kaikki viestit, joiden osana on annettu sana.

**Tätä ei voi tehdä vielä välipalautuksessa 2**

- Ylläpitäjä voi poistaa tarvittaessa muiden jättämän arvostelun tai viestin. 

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
