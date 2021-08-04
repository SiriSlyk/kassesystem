
import tkinter
from database import *
from tkinter import messagebox

db = Database()


class GuiDatabase:
    def __init__(self):

        self.hovedvindu = tkinter.Tk()
        self.hovedvindu.title("Database")
        self.hovedvindu.geometry("650x600")
        self.masterPassword = "password"
        self.hovedvindu.config(background="#999")

        #STRINGVARS:
        articleNrStringVar = tkinter.StringVar()
        articleNrStringVar.set("00-0000")
        articleNameStringVar = tkinter.StringVar()
        articleNameStringVar.set("Name on article")

        self.search_label = tkinter.Label(self.hovedvindu, text="Søk: ", background="#999", font=("Arial", 16)).grid(column=0, row=0)
        self.search_Entry = tkinter.Entry(self.hovedvindu)
        self.search_Entry.grid(column=1, row=0)
        self.search_button = tkinter.Button(self.hovedvindu, text="Søk", command=self.searchFunc).grid(column=2, row=0)

        self.articleNr_label = tkinter.Label(self.hovedvindu, text="Artikkel nr: ", background="#999").grid(column=0, row=1)
        self.articleName_label = tkinter.Label(self.hovedvindu, text="Navn: ", background="#999").grid(column=0, row=2)

        self.articleNr_entry = tkinter.Entry(self.hovedvindu, textvariable=articleNrStringVar).grid(column=1, row=1)
        self.articleName_entry = tkinter.Entry(self.hovedvindu, textvariable=articleNameStringVar).grid(column=1, row=2)


        self.artikler_listbox = tkinter.Listbox(self.hovedvindu, selectmode=tkinter.SINGLE, width=50, height=50, background="#999", font=("Arial", 16))
        self.artikler_listbox.grid(column=0, row=3, columnspan=5)


        tkinter.mainloop()

    def searchFunc(self):
        searchkey = self.search_Entry.get()
        searchkey = searchkey.split(" ")
        self.artikler_listbox.delete(0,tkinter.END)

        resultatListe = convertDatabaseResult(db.searchInRecords(searchkey))
        if resultatListe:
            #self.artikler_listbox = tkinter.Listbox(self.hovedvindu, selectmode=tkinter.SINGLE, width=100, height=50, background="#999")
            for artikel in resultatListe:
                artikelEdit = f"{artikel[1]} {artikel[3]} \n Pris: {artikel[4]}kr"
                self.artikler_listbox.insert(tkinter.END, artikelEdit)
            #self.artikler_listbox.grid(column=0, row=3, columnspan=5)
        else:
            tkinter.messagebox.showerror("Advarsel", "Søket ga ingen resultater!")




def formaterTilTekst(liste):
    liste[1] = str(endreLengde(12, liste[1]))
    #liste[2] = str(endreLengde(15, liste[2]))
    liste[3] = (endreLengde(30, liste[3]))
    liste[4] = str(endreLengde(-8, liste[4], "kr"))
    del liste[0]
    del liste[1]
    return liste


    

def endreLengde(lengde, item, tilSlutt=""):
    lengden = len(str(item))
    leggTil = lengde - abs(lengden)
    whitespace = " " * leggTil
    if lengde > 0:
        return f"{item}{whitespace}"
    else:
        return f"{whitespace}{item}{tilSlutt}"




def convertDatabaseResult(liste):
    resultat = []
    for tuple in liste:
        record = []
        for element in tuple:
            record.append(element)
        resultat.append(record)     
    return resultat



if __name__ == '__main__':
    guiDatabase = GuiDatabase()
    