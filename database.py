
import mysql
from mysql import connector
from var import *

db = mysql.connector.connect(
    host='localhost',
    username='root',
    passwd=password,
    database='products' 
)

cursor = db.cursor()

Q1 = "CREATE TABLE articles (id INT PRIMARY KEY AUTO_INCREMENT, articleNR VARCHAR(12), barcode BIGINT, article VARCHAR(50), price REAL)"

class Database:
    def __init__(self, db=db, cursor=cursor):
        self.db = db
        self.cursor = cursor
        self.tableFields = ['id', 'articleNR', 'barcode', 'article', 'price']
    
    def createTable(self, command):
        pass

    def inserRecord(self, tuple):
        
        insertCommand = "INSERT INTO articles (articleNR, barcode, article, price) VALUES (%s,%s,%s,%s)"
        self.cursor.execute(insertCommand, tuple)
        self.db.commit()

    def searchInRecords(self, keyword):
        liste = []
        #print("Keyword: " + keyword)
        for field in self.tableFields:
            
            command = f"SELECT * FROM articles WHERE {field}=%s"
            self.cursor.execute(command, (keyword,))
            for x in self.cursor:
                liste.append(x)
        print(liste)

    

    def commandToDatabase(self, command):
        self.cursor.execute(command)
        print("Command executed!")

    def deleteRecord(self, id):
        self.cursor.execute(f"DELETE FROM articles WHERE id={id}")  
    
    
    def printAllRows(self):
        
        printCommand = "SELECT * FROM articles"
        self.cursor.execute(printCommand)
        for line in self.cursor:
            print(line)





if __name__ == '__main__':
    database = Database(db, cursor)
    database.searchInRecords(("70-101"))


    
    