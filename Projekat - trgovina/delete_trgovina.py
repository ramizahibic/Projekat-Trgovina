import sqlite3

def delete_zaposleni(id):
    conn = sqlite3.connect('trgovina.db')
    c = conn.cursor()

    id = input("Unesite id: ")

    print("Uspjesno ste obrisali zaposlenika ! ")

    c.execute("DELETE FROM Zaposleni WHERE ID = ?;",(id))


    conn.commit()
    conn.close()

def delete_kupci(id):
    conn = sqlite3.connect('trgovina.db')
    c = conn.cursor()

    id = input("Unesite id: ")

    print("Uspjesno ste obrisali kupca. ")

    c.execute("DELETE FROM Kupci WHERE ID = ?;", (id))

    conn.commit()
    conn.close()

def delete_proizvodi(id):
    conn = sqlite3.connect('trgovina.db')
    c = conn.cursor()

    id = input("Unesite id: ")

    print("Obrisali ste proizvod!")


    c.execute("DELETE FROM Proizvodi WHERE ID = ?;", (id))


    conn.commit()
    conn.close()

def delete_dobavljaci(id):
    conn = sqlite3.connect('trgovina.db')
    c = conn.cursor()

    id = input("Unesite id:")

    print("Obrisali ste dobavljaca!")

    c.execute("DELETE FROM Dobavljaci WHERE ID = ?;", (id))


    conn.commit()
    conn.close()

delete_zaposleni('id')
delete_kupci('id')
delete_proizvodi('id')
delete_dobavljaci('id')