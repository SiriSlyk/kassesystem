
import sqlite3


class Database:
    def __init__(self):
        #self.conn = sqlite3.connect("database.db")
        self.conn = sqlite3.connect(":memory:")
        self.c = self.conn.cursor()

    def createDatabase(self):
        self.c.execute("CREATE TABLE articles (id INTEGER PRIMARY KEY,artikelNR TEXT,barcode INTEGER NOT NULL,name TEXT,"
            "description TEXT,price TEXT,quantity INTEGER,shelf INTEGER)")
        print("Created")

    def insertArticle(self, articleNr, barcode, name, description, price, quantity, shelf):
        with self.conn:
            self.c.execute("INSERT INTO articles VALUES (:articleNr, :barcode, :name, :description, :price, :quantity, :shelf)",
                           {'articleNr':articleNr, 'barcode':barcode, 'name':name, 'description':description, 'price':price, 'quantity':quantity, 'shelf':shelf})


if __name__ == '__main__':
    db = Database()
    db.createDatabase()
