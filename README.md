# PROJEKT2-FLASK APLIKACIJA
Za aplikaciju drugog projekta tema je bila Memories apartmani u Svetom Petru na moru kraj Zadra.
Aplikacija se sastoji od više web stranica 

Na pocetnoj stranici glavne opcije su log in i nastavi kao gost.
Uz navedene opcije nalazi slideshow sa nekoliko slika i tablica sa trenutnim vremenskim prilikama u gradu Zadru.
Razlika u odabira opcija log in ili nastavi kao gost ogleda se u tome da ako se logira, na stranici pise 
hello i username a ako se odabere opcija nastavi kao gost stranice su bez pozrdava.

Na savim stranicama osim pocetne nalazi se i opcija za direktni pozivv na sluzbeni broj apartmana.
Takoder se na svim stranicama nalazi i tablica sa trenutnim vremenskim podatcima koji se preuzimaju sa https://openweathermap.org/
U mobilnoj verziji, traka za navigaciju unutar aplikacije se pretvara u padajuci "hamburger" izbornik.

### Log in
Buduci da aplikacija nije povezana sa bazom podataka, podatci za log in nalaza se u app.py datoteci (lista users:<br>
username='Nikola', password='password'<br>
username='Luka', password='123'<br>
username='Andela', password='321'<br>
username='Mateo', password='456'<br>
username='Elvis', password='789'<br>
)

## Pokretanje aplikacije
1.Instaliramo virtualno okruženje u CMD ili Poweshell-u ( py -m venv venv ili python -m venv venv)<br>
2.Ulazimo u direktorij Scripts unutar venv foldera kako bi ga aktivirali (venv\Scripts\activate)<br>
3.Instalacija sa requirements (pip install -r requirements.txt)<br>
4.set FLASK_APP=app.py<br>
5.set FLASK_DEBUG=1<br>
6.flask run<br>
7.Otvoriti browser te upisati(http://127.0.0.1:5000/)
