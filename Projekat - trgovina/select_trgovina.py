import sqlite3

def select_zaposleni(ID):
    conn = sqlite3.connect('trgovina.db')
    c = conn.cursor()

    ID = input("Unesite id: ")
    c.execute('SELECT * FROM Zaposleni WHERE ID = ?', ID)
    rows = c.fetchall()

    for row in rows:
        print(row)

    conn.close()

def select_kupci(ID):
    conn = sqlite3.connect('trgovina.db')
    c = conn.cursor()

    ID = input("Unesite id: ")
    c.execute('SELECT * FROM Kupci WHERE ID = ?', ID)
    rows = c.fetchall()

    for row in rows:
        print(row)

    conn.close()

def select_proizvodi(ID):
    conn = sqlite3.connect('trgovina.db')
    c = conn.cursor()

    ID = input("Unesite id: ")
    c.execute('SELECT * FROM Proizvodi WHERE ID = ?', ID)
    rows = c.fetchall()

    for row in rows:
        print(row)

    conn.close()

def select_dobavljaci(ID):
    conn = sqlite3.connect('trgovina.db')
    c = conn.cursor()

    ID = input("Unesite id: ")
    c.execute('SELECT * FROM Dobavljaci WHERE ID = ?', ID)
    rows = c.fetchall()

    for row in rows:
        print(row)

    conn.close()

select_zaposleni('id')
select_kupci('id')
select_proizvodi('id')
select_dobavljaci('id')