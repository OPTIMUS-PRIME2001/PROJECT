import sqlite3
def create_DB():
    con=sqlite3.connect(database=r'InventoryData.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,email TEXT,gender TEXT,contact TEXT,dob TEXT,doj TEXT,uname TEXT,pass TEXT,utype TEXT,address TEXT,salary TEXT)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,contact TEXT,desc TEXT)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS PRODUCTS(P_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,Pname TEXT NOT NULL, cid INTEGER NOT NULL, supplier TEXT, price REAL, Qty INTEGER, Status TEXT, icon BLOB)")
    con.commit()

    cur.execute("CREATE TABLE Bills( Bill_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, Invoice INTEGER NOT NULL UNIQUE, Date TEXT NOT NULL, Net_pay REAL NOT NULL, src BLOB)")
    con.commit()    
    
create_DB()