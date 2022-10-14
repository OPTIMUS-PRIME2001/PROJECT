import sqlite3
def create_DB():
    con=sqlite3.connect(database=r'InventoryData.db')

create_DB()