import tkinter
from backend import *

items = ["Ienhet", "Dndpfsd", "Nflpwnf"]


rodListe = ["Funksjoner", "Tilbake"]
gronnListe = ["Endre antall", "Artikkel"]
gulListe = ["Søk artikkel", "Flere funksjoner"]
blaListe = ["Prisforespørsel", "Linjerabatt"]
orangeListe = ["Fjern artikkel", "E-tjenester"]
lillaListe = ["Lojalitet", "Kvitteringsfunksjoner"]
hvitListe = ["Betaling", "Velikehold"]



class GUI:
    def __init__(self):
        self.hovedvindu = tkinter.Tk()
        self.hovedvindu.title("Kassesystem")
        #self.hovedvindu.attributes('-fullscreen', True)  # FULLSCREEN

        self.HEIGHT = self.hovedvindu.winfo_screenwidth()

        # Frames
        self.showItemsFrame = tkinter.Frame(self.hovedvindu)
        self.showItemsFrame.grid(column=0, row=0)

        self.angiFrame = tkinter.Frame(self.hovedvindu)
        self.angiFrame.grid(column=0, row=1)

        self.funcFrame = tkinter.Frame(self.hovedvindu, background="#31B4D8")
        self.funcFrame.grid(column=1, row=0, rowspan=3)  # , sticky="e")

        #self.numFrame = tkinter.Frame(self.hovedvindu)
        #self.numFrame.grid(column=0, row=2)

        self.keysFrame = tkinter.Frame(self.hovedvindu)
        self.keysFrame.grid(column=0, row=2)

        self.state = 0






        self.footerFrame = tkinter.Frame(self.hovedvindu, background="red")
        self.footerFrame.grid(column=0, row=3, sticky="we", columnspan=2)

        self.textfelt()
        self.angifelt()
        self.funcfelt()
        self.numfelt()
        self.footer()

        tkinter.mainloop()

    def textfelt(self):
        self.text = tkinter.Text(self.showItemsFrame)
        self.text.grid(column=0, row=0)
        self.text.config(state=tkinter.DISABLED)

    def angifelt(self):
        self.label = tkinter.Label(self.angiFrame, text="Angi/skann artikkel:")
        self.label.grid(column=0, row=0)

        self.entry = tkinter.Entry(self.angiFrame, width=100)
        self.entry.grid(column=0, row=1)

    def funcfelt(self):
        x_margin = 10
        y_margin = self.HEIGHT / 150
        x_padding = 100
        y_padding = 25
        borderWidth = 5


        self.rodStringvar = tkinter.StringVar()
        self.rodStringvar.set("F1\n" + rodListe[self.state])

        self.gronnStringvar = tkinter.StringVar()
        self.gronnStringvar.set("F2\n" + gronnListe[self.state])

        self.gulStringvar = tkinter.StringVar()
        self.gulStringvar.set("F3\n" + gulListe[self.state])

        self.blaStringvar = tkinter.StringVar()
        self.blaStringvar.set("F4\n" + blaListe[self.state])

        self.orangeStringvar = tkinter.StringVar()
        self.orangeStringvar.set("F5\n" + orangeListe[self.state])

        self.lillaStringvar = tkinter.StringVar()
        self.lillaStringvar.set("F6\n" + lillaListe[self.state])

        self.hvitStringvar = tkinter.StringVar()
        self.hvitStringvar.set("F7\n" + hvitListe[self.state])

        self.funksjonButton = tkinter.Button(self.funcFrame, textvariable=self.rodStringvar, width=2, command=self.rodFunk, background="#EB4521", borderwidth=borderWidth) \
            .grid(column=0, row=0, ipadx=x_padding, ipady=y_padding, pady=y_margin, padx=x_margin)
        self.endre_antallButton = tkinter.Button(self.funcFrame, textvariable=self.gronnStringvar, width=2, command=self.gjorIngenting, background="green", borderwidth=borderWidth) \
            .grid(column=0, row=1, ipadx=x_padding, ipady=y_padding, pady=y_margin, padx=x_margin)
        self.sok_artikkelButton = tkinter.Button(self.funcFrame, textvariable=self.gulStringvar, width=2, command=self.gjorIngenting, background="#EEF422", borderwidth=borderWidth) \
            .grid(column=0, row=2, ipadx=x_padding, ipady=y_padding, pady=y_margin, padx=x_margin)
        self.prisforesporselButton = tkinter.Button(self.funcFrame, textvariable=self.blaStringvar, width=2, command=self.gjorIngenting, background="#00BFF3", borderwidth=borderWidth) \
            .grid(column=0, row=3, ipadx=x_padding, ipady=y_padding, pady=y_margin, padx=x_margin)
        self.fjern_artikkelButton = tkinter.Button(self.funcFrame, textvariable=self.orangeStringvar, width=2, command=self.gjorIngenting, background="orange", borderwidth=borderWidth) \
            .grid(column=0, row=4, ipadx=x_padding, ipady=y_padding, pady=y_margin, padx=x_margin)
        self.lojalitetButton = tkinter.Button(self.funcFrame, textvariable=self.lillaStringvar, width=2, command=self.gjorIngenting, background="#B135D0", borderwidth=borderWidth) \
            .grid(column=0, row=5, ipadx=x_padding, ipady=y_padding, pady=y_margin, padx=x_margin)
        self.velikeholdButton = tkinter.Button(self.funcFrame, textvariable=self.hvitStringvar, width=2, command=self.gjorIngenting, background="#ffffff", borderwidth=borderWidth) \
            .grid(column=0, row=7, ipadx=x_padding, ipady=y_padding, pady=y_margin, padx=x_margin)

    def numfelt(self):
        x_margin = 5
        y_margin = 5
        x_padding = 20
        y_padding = 10

        tupple_y_margin = (10, 100)
        tupple_x_margin = (50, 10)

        rectangle_padding = 35



        self.numFrame = tkinter.Frame(self.keysFrame)
        self.numFrame.grid(column=0, row=0)

        self.actionFrame = tkinter.Frame(self.keysFrame)
        self.actionFrame.grid(column=1, row=0)

        self.laasButton = tkinter.Button(self.numFrame, text="Lås", width=2, command=self.gjorIngenting) \
            .grid(column=0, row=0, ipadx=x_padding+25, ipady=y_padding, padx=tupple_y_margin, pady=y_margin)
        self.tilbakeButton = tkinter.Button(self.numFrame, text="Tilbake", width=2, command=self.gjorIngenting) \
            .grid(column=0, row=1, ipadx=x_padding+25, ipady=y_padding, padx=tupple_y_margin, pady=y_margin)
        self.slettButton = tkinter.Button(self.numFrame, text="Slett", width=2, command=self.slett) \
            .grid(column=0, row=2, ipadx=x_padding+25, ipady=y_padding, padx=tupple_y_margin, pady=y_margin)
        self.angreButton = tkinter.Button(self.numFrame, text="Angre", width=2, command=self.gjorIngenting) \
            .grid(column=0, row=3, ipadx=x_padding+25, ipady=y_padding, padx=tupple_y_margin, pady=y_margin)

        row = 0

        self.numenButton = tkinter.Button(self.numFrame, text="1", width=2, command=lambda: self.numpad("1"), background="#222", fg="#fff").grid(
            column=1, row=row, ipadx=20, ipady=10, padx=5, pady=5)
        self.numtoButton = tkinter.Button(self.numFrame, text="2", width=2, command=lambda: self.numpad("2"), background="#222", fg="#fff").grid(
            column=2, row=row, ipadx=20, ipady=10, padx=5, pady=5)
        self.numtreButton = tkinter.Button(self.numFrame, text="3", width=2, command=lambda: self.numpad("3"), background="#222", fg="#fff").grid(
            column=3, row=row, ipadx=20, ipady=10, padx=5, pady=5)
        row += 1
        self.numfireButton = tkinter.Button(self.numFrame, text="4", width=2, command=lambda: self.numpad("4"), background="#222", fg="#fff").grid(
            column=1, row=row, ipadx=20, ipady=10, padx=5, pady=5)
        self.numfemButton = tkinter.Button(self.numFrame, text="5", width=2, command=lambda: self.numpad("5"), background="#222", fg="#fff").grid(
            column=2, row=row, ipadx=20, ipady=10, padx=5, pady=5)
        self.numseksButton = tkinter.Button(self.numFrame, text="6", width=2, command=lambda: self.numpad("6"), background="#222", fg="#fff").grid(
            column=3, row=row, ipadx=20, ipady=10, padx=5, pady=5)
        row += 1
        self.numsyvButton = tkinter.Button(self.numFrame, text="7", width=2, command=lambda: self.numpad("7"), background="#222", fg="#fff").grid(
            column=1, row=row, ipadx=20, ipady=10, padx=5, pady=5)
        self.numotteButton = tkinter.Button(self.numFrame, text="8", width=2, command=lambda: self.numpad("8"), background="#222", fg="#fff").grid(
            column=2, row=row, ipadx=20, ipady=10, padx=5, pady=5)
        self.numniButton = tkinter.Button(self.numFrame, text="9", width=2, command=lambda: self.numpad("9"), background="#222", fg="#fff").grid(
            column=3, row=row, ipadx=20, ipady=10, padx=5, pady=5)
        row += 1
        self.numnullButton = tkinter.Button(self.numFrame, text="0", width=2, command=lambda: self.numpad("0"), background="#222", fg="#fff").grid(
            column=1, row=row, ipadx=20, ipady=10, padx=5, pady=5)
        self.numnull_nullButton = tkinter.Button(self.numFrame, text="00", width=2, command=lambda: self.numpad("00"), background="#222", fg="#fff")\
            .grid(column=2, row=row, ipadx=20, ipady=10, padx=5, pady=5)
        self.numkommaButton = tkinter.Button(self.numFrame, text=".", width=2, command=lambda: self.numpad("."), background="#222", fg="#fff").grid(
            column=3, row=row, ipadx=20, ipady=10, padx=5, pady=5)

        self.sumButton = tkinter.Button(self.actionFrame, text="Sum", width=2, command=self.gjorIngenting)\
            .grid(column=4, row=0, columnspan=1, ipadx=rectangle_padding, ipady=rectangle_padding, padx=tupple_x_margin, pady=y_margin)
        self.enterButton = tkinter.Button(self.actionFrame, text="Enter", width=2, command=self.enterFunk)\
            .grid(column=4, row=2, columnspan=1, ipadx=rectangle_padding, ipady=rectangle_padding, padx=tupple_x_margin, pady=y_margin)


    def footer(self):
        self.labelTime = tkinter.Label(self.footerFrame, text="Dette er en test")
        self.labelTime.grid(column=0, row=0)

        self.exitButton = tkinter.Button(self.footerFrame, text="Exit fullscreen", command=self.exitFullscreen)
        self.exitButton.grid(column=1, row=0)

    # FUNKSJONER
    def exitFullscreen(self):
        #self.hovedvindu.attributes('-fullscreen', False)  # FULLSCREEN OFF
        self.hovedvindu.destroy()

    def numpad(self, num):
        self.entry.insert(tkinter.END, num)

    def enterFunk(self):
        artikkel = self.entry.get()
        self.entry.delete(0, tkinter.END)
        if artikkel != "":
            self.text.config(state=tkinter.NORMAL)
            self.text.insert(tkinter.END, artikkel+"\n")
            self.text.config(state=tkinter.DISABLED)

    def slett(self):
        self.entry.delete(0, tkinter.END)

    def gjorIngenting(self): # Denne skal slettes
        print("Jeg gjør ingenting enda!")

    def rodFunk(self):
        if self.state == 0:
            self.state = 1
        elif self.state == 1:
            self.state = 0

        self.rodStringvar.set("F1\n" + rodListe[self.state])
        self.gronnStringvar.set("F2\n" + gronnListe[self.state])
        self.gulStringvar.set("F3\n" + gulListe[self.state])
        self.blaStringvar.set("F4\n" + blaListe[self.state])
        self.orangeStringvar.set("F5\n" + orangeListe[self.state])
        self.lillaStringvar.set("F6\n" + lillaListe[self.state])
        self.hvitStringvar.set("F7\n" + hvitListe[self.state])



if __name__ == "__main__":
    gui = GUI()