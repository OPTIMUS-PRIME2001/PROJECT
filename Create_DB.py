import sqlite3
def create_DB():
    con=sqlite3.connect(database=r'InventoryData.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT)")
    con.commit()
create_DB()