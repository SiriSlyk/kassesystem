
import tkinter
from database import *

db = Database()


class GuiDatabase:
    def __init__(self):

        self.hovedvindu = tkinter.Tk()
        self.hovedvindu.title("Database")
        self.masterPassword = "password"

        #STRINGVARS:
        articleNrStringVar = tkinter.StringVar()
        articleNrStringVar.set("00-0000")
        articleNameStringVar = tkinter.StringVar()
        articleNameStringVar.set("Name on article")

        self.search_label = tkinter.Label(self.hovedvindu, text="Søk: ").grid(column=0, row=0)
        self.search_Entry = tkinter.Entry(self.hovedvindu)
        self.search_Entry.grid(column=1, row=0)
        self.search_button = tkinter.Button(self.hovedvindu, text="Søk", command=self.searchFunc).grid(column=2, row=0)

        self.articleNr_label = tkinter.Label(self.hovedvindu, text="Artikkel nr: ").grid(column=0, row=1)
        self.articleName_label = tkinter.Label(self.hovedvindu, text="Navn: ").grid(column=0, row=2)

        self.articleNr_entry = tkinter.Entry(self.hovedvindu, textvariable=articleNrStringVar).grid(column=1, row=1)
        self.articleName_entry = tkinter.Entry(self.hovedvindu, textvariable=articleNameStringVar).grid(column=1, row=2)

        
        tkinter.mainloop()

    def searchFunc(self):
        searchkey = self.search_Entry.get()
        searchkey = searchkey.split(" ")
        searchTuple = tuple(searchkey)

        #print(db.searchInRecords(searchkey))





if __name__ == '__main__':
    guiDatabase = GuiDatabase()
    