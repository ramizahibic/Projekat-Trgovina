import sqlite3

def update_zaposleni(id,ime, prezime, adresa, grad,drzava,placa):
    conn = sqlite3.connect('trgovina.db')
    c = conn.cursor()

    id = input("Unesite id: ")
    ime = input("Unesite ime: ")
    prezime = input("Unesite prezime: ")
    adresa = input("Unesite adresu: ")
    grad = input("Unesite grad: ")
    placa = input("Unesite iznos place: ")
    drzava = input("Unesite drzavu: ")

    c.execute("UPDATE Zaposleni set Ime=?,Prezime=?,Adresa=?,Grad=?,Drzava=?,Placa=? WHERE id = ?",
              (id, ime, prezime, adresa, grad, drzava, placa))

    print("Uspjesno ste update-ovali zaposlenog! ")

    conn.commit()
    conn.close()

def update_kupci(id,ime, prezime,grad):
    conn = sqlite3.connect('trgovina.db')
    c = conn.cursor()

    id = input("Unesite id: ")
    ime = input("Unesite ime: ")
    prezime = input("Unesite prezime: ")
    grad = input("Unesite grad: ")

    c.execute("UPDATE Kupci set Ime=?, Prezime=?, Grad=? WHERE id=?",
              (id, ime, prezime, grad))

    print("Uspjesno ste update-ovali kupca! ")

    conn.commit()
    conn.close()

def update_proizvodi(id,naziv_proizvoda,kolicina,cijena,):
    conn = sqlite3.connect('trgovina.db')
    c = conn.cursor()

    id = input("Unesite id: ")
    naziv_proizvoda = input("Unesite naziv: ")
    kolicina = input("Unesite kolicinu: ")
    cijena = input("Unesite cijenu: ")

    c.execute("UPDATE Proizvodi set Naziv_proizvoda=?, Kolicina=?, Cijena=? WHERE id=?",
              (id, naziv_proizvoda, kolicina, cijena))

    print("Uspjesno ste update-ovali proizvod!")

    conn.commit()
    conn.close()

def update_dobavljaci(id,naziv_dobavljaca,mjesto):
    conn = sqlite3.connect('trgovina.db')
    c = conn.cursor()

    id = input("Unesite id: ")
    naziv_dobavljaca = input("Unesite naziv dobavljaca: ")
    mjesto = input("Unesite naziv mjesta: ")

    c.execute("UPDATE Dobavljaci set Naziv_dobavljaca=?, Mjesto=? WHERE id=?",
              (id,naziv_dobavljaca,mjesto))

    print("Uspjesno ste update-ovali dobavljaca!")

    conn.commit()
    conn.close()

update_zaposleni('id','ime','prezime','adresa','grad','drzava','placa')
update_kupci('id','ime','prezime','grad')
update_proizvodi('id','naziv_proizvoda','kolicina','cijena')
update_dobavljaci('id','naziv_dobavljaca','mjesto')