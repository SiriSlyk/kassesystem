
import mysql
from mysql import connector
from var import *
import tkinter
from tkinter import messagebox

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

    def searchInRecords_kassen(self, keyword):
            print(f"keyword: {keyword}")
        #try:
            if "-" in keyword:
                command = f"SELECT * FROM articles WHERE articleNR=%s LIMIT 1"
            else:
                command = f"SELECT * FROM articles WHERE barcode=%s LIMIT 1" 
            self.cursor.execute(command, (keyword,))
            for x in self.cursor:
                print(x)
                return x
        #except:
            pass
    
    def searchInRecords(self, keywords, fields="*"):
        liste = []
        #print("Keyword: " + keyword)
        for field in self.tableFields:
            for keyword in keywords:
                command = f"SELECT {fields} FROM articles WHERE {field}=%s"
                self.cursor.execute(command, (keyword,))
                for x in self.cursor:
                    liste.append(x)
        if len(liste) == 0:
            return None
        #print(liste)
        print("SUCCESS")
        return liste

    

    def commandToDatabase(self, command):
        self.cursor.execute(command)
        self.db.commit()
        print("Command executed!")

    def deleteRecord(self, id):
        self.cursor.execute(f"DELETE FROM articles WHERE id={id}")  
    
    
    def printAllRows(self):
        liste = []
        printCommand = "SELECT * FROM articles"
        self.cursor.execute(printCommand)
        for line in self.cursor:
            print(line)
            liste.append(line)
        return liste





if __name__ == '__main__':
    database = Database(db, cursor)
    #print(database.searchInRecords(("5"), "id"))
    #database.printAllRows()
    #Q1 = f"SELECT * FROM articles WHERE id='70-8000'"
    #database.commandToDatabase(Q1)
    #print(database.searchInRecords_kassen("70-8001"))
    #print(database.searchInRecords_kassen("70-8001"))
    #print(database.searchInRecords_kassen("70-101"))
    #database.searchInRecords_kassen("70-101")
    print(database.printAllRows())
    
    