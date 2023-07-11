import sqlite3

def insert_zaposleni(id,ime, prezime, adresa, grad, drzava, placa):
    conn = sqlite3.connect('trgovina.db')
    c = conn.cursor()

    id = input("Unesite id: ")
    ime = input("Unesite ime: ")
    prezime = input("Unesite prezime: ")
    adresa = input("Unesite adresu: ")
    grad = input("Unesite grad: ")
    placa = input("Unesite iznos place: ")
    drzava = input("Unesite drzavu: ")


    c.execute("INSERT INTO Zaposleni (ID, Ime, Prezime, Adresa, Grad, Drzava, Placa) VALUES (?,?,?,?,?,?,?)",
              (id, ime, prezime, adresa, grad, drzava, placa))

    print("Uspjesno ste dodali novog zaposlenika u bazu! ")

    conn.commit()
    conn.close()

def insert_kupci(id, ime, prezime, grad):
    conn = sqlite3.connect('trgovina.db')
    c = conn.cursor()

    id = input("Unesite id: ")
    ime = input("Unesite ime: ")
    prezime = input("Unesite prezime: ")
    grad = input("Unesite grad: ")


    c.execute("INSERT INTO Kupci (ID, Ime, Prezime, Grad) VALUES (?,?,?,?)",
              (id, ime, prezime, grad))

    print("Uspjesno dodan novi kupac. ")

    conn.commit()
    conn.close()

def insert_proizvodi(id, naziv_proizvoda, kolicina, cijena):
    conn = sqlite3.connect('trgovina.db')
    c = conn.cursor()

    id = input("Unesite id: ")
    naziv_proizvoda = input("Unesite naziv: ")
    kolicina = input("Unesite kolicinu: ")
    cijena = input("Unesite cijenu: ")



    c.execute("INSERT INTO Proizvodi (ID, Naziv_proizvoda, Kolicina, Cijena) VALUES (?,?,?,?)",
              (id, naziv_proizvoda, kolicina, cijena))

    print("Dodan je novi proizvod!")

    conn.commit()
    conn.close()

def insert_dobavljaci(id, naziv_dobavljaca, mjesto):
    conn = sqlite3.connect('trgovina.db')
    c = conn.cursor()

    id = input("Unesite id: ")
    naziv_dobavljaca = input("Unesite naziv dobavljaca: ")
    mjesto = input("Unesite naziv mjesta: ")


    c.execute("INSERT INTO Dobavljaci (ID,Naziv_dobavljaca, Mjesto) VALUES (?,?,?)",
              (id, naziv_dobavljaca, mjesto))

    print("Uspjesno dodan dobavljac!")

    conn.commit()
    conn.close()

insert_zaposleni('id','ime','prezime','adresa','grad','drzava','placa')
insert_kupci('id','ime','prezime','grad')
insert_proizvodi('id','naziv_proizvoda','kolicina','cijena')
insert_dobavljaci('id','naziv_dobavljaca','mjesto')


