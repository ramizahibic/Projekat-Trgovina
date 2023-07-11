import sqlite3

def create_database():
    conn = sqlite3.connect('trgovina.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS Zaposleni (
                   ID INTEGER PRIMARY KEY,
                   Ime TEXT,
                   Prezime TEXT,
                   Adresa TEXT,
                   Grad TEXT,
                   Drzava TEXT,
                   Placa INTEGER
                   )''')

    c.execute('''CREATE TABLE IF NOT EXISTS Kupci (
                   ID INTEGER PRIMARY KEY,
                   Ime TEXT,
                   Prezime TEXT,
                   Grad TEXT
                   )''')

    c.execute('''CREATE TABLE IF NOT EXISTS Proizvodi (
                   ID INTEGER PRIMARY KEY,
                   Naziv_proizvoda TEXT,
                   Kolicina INTEGER,
                   Cijena INTEGER
                   )''')

    c.execute('''CREATE TABLE IF NOT EXISTS Dobavljaci (
                   ID INTEGER PRIMARY KEY,
                   Naziv_dobavljaca TEXT,
                   Mjesto TEXT
                   )''')

    conn.commit()
    conn.close()

create_database()


