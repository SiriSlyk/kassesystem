import tkinter
from tkinter import ttk
#from backend import *
from database import *
from kortTerminal import *

items = ["Ienhet", "Dndpfsd", "Nflpwnf"]
db = Database()


rodListe = ["Funksjoner", "Tilbake", "Tilbake", "Tilbake"]
gronnListe = ["Endre antall", "Artikkel", "Kort", "Linjeretur"]
gulListe = ["Søk artikkel", "Flere funksjoner", "Kontanter", ""]
blaListe = ["Prisforespørsel", "Linjerabatt", "Rabatter", ""]
orangeListe = ["Fjern artikkel", "E-tjenester", "Andre betalingsmåter", ""]
lillaListe = ["Lojalitet", "Kvitteringsfunksjoner", "", ""]
hvitListe = ["Betaling", "Velikehold", "", ""]



class GuiKasse:
    def __init__(self, userId=0):
        print(userId, "s6k")
        self.hovedvindu = tkinter.Tk()
        self.hovedvindu.title("Kassesystem")
        #self.hovedvindu.attributes('-fullscreen', True)  # FULLSCREEN
        self.hovedvindu.geometry("")

        self.HEIGHT = self.hovedvindu.winfo_screenwidth()


        

    # Frames

        #Widgets
        self.showItemsFrame = tkinter.Frame(self.hovedvindu, background="#111")
        self.showItemsFrame.grid(column=0, row=0, columnspan=2)

        self.angiFrame = tkinter.Frame(self.hovedvindu)
        self.angiFrame.grid(column=0, row=1, sticky="W")

        self.funcFrame = tkinter.Frame(self.hovedvindu, background="#31B4D8")
        self.funcFrame.grid(column=3, row=0, rowspan=3)  # , sticky="e")

        self.keysFrame = tkinter.Frame(self.hovedvindu)
        self.keysFrame.grid(column=0, row=2)

        self.footerFrame = tkinter.Frame(self.hovedvindu, background="red")
        self.footerFrame.grid(column=0, row=3, sticky="WE", columnspan=4)


        #Widget TREEVIEW
        self.display_treeview = ttk.Treeview(self.showItemsFrame, selectmode=tkinter.BROWSE, show="tree", column=('artikelNr', 'article', 'price'), height=10)

        #Variabler
        self.state = 0
        self.artiklerIKurv = []
        self.antallLinjer = 0
        self.treeviewID = 0
        self.treeListLen = 0
        self.currentScollPOS = -1

        #Stringvar
        self.sumStringvar = tkinter.StringVar()
        self.sumStringvar.set("")

        self.antallArtikler_stringvar = tkinter.StringVar()
        self.antallArtikler_stringvar.set("")

        #EVENTS
        self.hovedvindu.bind('<Return>', self.enterKEY_Funk)
        self.display_treeview.bind('<Button-1>', self.selectFromTree_func)

        #Bulding the GUI:    
        self.treeview()
        self.angifelt()
        self.funcfelt()
        self.numfelt()
        self.footer()

        #MAINLOOP
        tkinter.mainloop()

    #Building functions

    def treeview(self):
        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 14), rowheight=25)
        #self.display_treeview = ttk.Treeview(self.showItemsFrame, show="tree", column=('artikelNr', 'article', 'price'))
        self.display_treeview.heading('#1', text="artikelNr", anchor=tkinter.CENTER)
        self.display_treeview.heading('#2', text="article", anchor=tkinter.CENTER)
        self.display_treeview.heading('#3', text="price", anchor=tkinter.CENTER)

        self.display_treeview.column('#0', minwidth=0, width=0)
        self.display_treeview.column('#1', minwidth=0, width=150, anchor=tkinter.W)
        self.display_treeview.column('#2', minwidth=0, width=250, anchor=tkinter.W)
        self.display_treeview.column('#3', minwidth=0, width=160, anchor=tkinter.W)

        self.display_treeview.grid(column=0, row=0, columnspan=3)

        #self.display_treeview.insert("", "end", value=('70-8001', 'Bærepose S', '1.00'))
        #self.display_treeview.insert("", "end", value=('70-8001', 'Bærepose S', '1.00'))

        #self.scrollUP_button = tkinter.Button(self.showItemsFrame, text="^", command=self.selectFromTree_func).grid(column=1, row=0)
        #self.scrollDOWN_button = tkinter.Button(self.showItemsFrame, text="v", command=self.selectFromTree_func).grid(column=1, row=1)

        self.antallArtikler = tkinter.Label(self.showItemsFrame, textvariable=self.antallArtikler_stringvar, fg="#fff", bg="#111", font=("Arial", 14))
        self.antallArtikler.grid(column=0, row=1, sticky="NW")

        self.sumLabel = tkinter.Label(self.showItemsFrame, text="Sum", fg="#fff", bg="#111", font=("Arial", 14))
        self.sumLabel.grid(column=1, row=1, sticky="WE")

        self.sumNumberLabel = tkinter.Label(self.showItemsFrame, textvariable=self.sumStringvar, fg="#fff", bg="#111", font=("Arial", 14))
        self.sumNumberLabel.grid(column=2, row=1, sticky="E")
        
        #self.scroll_canvas = tkinter.Canvas(self.scrollFrame, background="#111", width=10)
        #self.scroll_canvas.grid(column=0, row=0)
        
        #self.scroll_canvas.create_oval(2, 2, 2, 2)

        #self.scrollUP_button = tkinter.Button(self.scrollFrame, text="^", command=self.selectFromTree_func).grid(column=0, row=0, pady=5, padx=(0, 10))
        #self.scrollDOWN_button = tkinter.Button(self.scrollFrame, text="v", command=self.selectFromTree_func).grid(column=0, row=1,  pady=2)

    def angifelt(self):
        #Widgets:
        self.label = tkinter.Label(self.angiFrame, text="Angi/skann artikkel:", font=("Arial", 14))
        self.entry = tkinter.Entry(self.angiFrame, width=50, font=("Arial", 14))
        
        #Placement
        self.label.grid(column=0, row=0, sticky="NW", pady=0, padx=20)
        self.entry.grid(column=0, row=1, sticky="NW", pady=0, padx=20)


    def funcfelt(self):
        x_margin = 10
        y_margin = 5
        x_padding = 100
        y_padding = 25-5
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

        #Widgets
        self.funksjonButton = tkinter.Button(self.funcFrame, textvariable=self.rodStringvar, width=2, command=self.rodFunk, background="#EB4521", borderwidth=borderWidth)
        self.endre_antallButton = tkinter.Button(self.funcFrame, textvariable=self.gronnStringvar, width=2, command=self.gjorIngenting, background="green", borderwidth=borderWidth)
        self.sok_artikkelButton = tkinter.Button(self.funcFrame, textvariable=self.gulStringvar, width=2, command=self.gulFunk, background="#EEF422", borderwidth=borderWidth)
        self.prisforesporselButton = tkinter.Button(self.funcFrame, textvariable=self.blaStringvar, width=2, command=self.gjorIngenting, background="#00BFF3", borderwidth=borderWidth)
        self.fjern_artikkelButton = tkinter.Button(self.funcFrame, textvariable=self.orangeStringvar, width=2, command=self.gjorIngenting, background="orange", borderwidth=borderWidth)
        self.lojalitetButton = tkinter.Button(self.funcFrame, textvariable=self.lillaStringvar, width=2, command=self.gjorIngenting, background="#B135D0", borderwidth=borderWidth)
        self.velikeholdButton = tkinter.Button(self.funcFrame, textvariable=self.hvitStringvar, width=2, command=self.hvitFunk, background="#ffffff", borderwidth=borderWidth)


        #Placement
        self.funksjonButton.grid(column=0, row=0, ipadx=x_padding, ipady=y_padding, pady=y_margin, padx=x_margin)
        self.endre_antallButton.grid(column=0, row=1, ipadx=x_padding, ipady=y_padding, pady=y_margin, padx=x_margin)
        self.sok_artikkelButton.grid(column=0, row=2, ipadx=x_padding, ipady=y_padding, pady=y_margin, padx=x_margin)
        self.prisforesporselButton.grid(column=0, row=3, ipadx=x_padding, ipady=y_padding, pady=y_margin, padx=x_margin)
        self.fjern_artikkelButton.grid(column=0, row=4, ipadx=x_padding, ipady=y_padding, pady=y_margin, padx=x_margin)
        self.lojalitetButton.grid(column=0, row=5, ipadx=x_padding, ipady=y_padding, pady=y_margin, padx=x_margin)
        self.velikeholdButton.grid(column=0, row=7, ipadx=x_padding, ipady=y_padding, pady=y_margin, padx=x_margin)
        

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

        self.laasButton = tkinter.Button(self.numFrame, text="Lås", width=2, command=self.gjorIngenting)
        self.tilbakeButton = tkinter.Button(self.numFrame, text="Tilbake", width=2, command=self.gjorIngenting)
        self.slettButton = tkinter.Button(self.numFrame, text="Slett", width=2, command=self.slett)
        self.angreButton = tkinter.Button(self.numFrame, text="Angre", width=2, command=self.gjorIngenting)

        self.numenButton = tkinter.Button(self.numFrame, text="1", width=2, command=lambda: self.numpad("1"), background="#222", fg="#fff")
        self.numtoButton = tkinter.Button(self.numFrame, text="2", width=2, command=lambda: self.numpad("2"), background="#222", fg="#fff")
        self.numtreButton = tkinter.Button(self.numFrame, text="3", width=2, command=lambda: self.numpad("3"), background="#222", fg="#fff")

        self.numfireButton = tkinter.Button(self.numFrame, text="4", width=2, command=lambda: self.numpad("4"), background="#222", fg="#fff")
        self.numfemButton = tkinter.Button(self.numFrame, text="5", width=2, command=lambda: self.numpad("5"), background="#222", fg="#fff")
        self.numseksButton = tkinter.Button(self.numFrame, text="6", width=2, command=lambda: self.numpad("6"), background="#222", fg="#fff")

        self.numsyvButton = tkinter.Button(self.numFrame, text="7", width=2, command=lambda: self.numpad("7"), background="#222", fg="#fff")
        self.numotteButton = tkinter.Button(self.numFrame, text="8", width=2, command=lambda: self.numpad("8"), background="#222", fg="#fff")
        self.numniButton = tkinter.Button(self.numFrame, text="9", width=2, command=lambda: self.numpad("9"), background="#222", fg="#fff")
        
        self.numnullButton = tkinter.Button(self.numFrame, text="0", width=2, command=lambda: self.numpad("0"), background="#222", fg="#fff")
        self.numnull_nullButton = tkinter.Button(self.numFrame, text="00", width=2, command=lambda: self.numpad("00"), background="#222", fg="#fff")
        self.numkommaButton = tkinter.Button(self.numFrame, text=".", width=2, command=lambda: self.numpad("."), background="#222", fg="#fff")

        self.sumButton = tkinter.Button(self.actionFrame, text="Sum", width=2, command=self.sumFunk)
        self.enterButton = tkinter.Button(self.actionFrame, text="Enter", width=2, command=self.enterFunk)

        #Placement
        
        self.laasButton.grid(column=0, row=0, ipadx=x_padding+25, ipady=y_padding, padx=tupple_y_margin, pady=y_margin)
        self.tilbakeButton.grid(column=0, row=1, ipadx=x_padding+25, ipady=y_padding, padx=tupple_y_margin, pady=y_margin)
        self.slettButton.grid(column=0, row=2, ipadx=x_padding+25, ipady=y_padding, padx=tupple_y_margin, pady=y_margin)
        self.angreButton.grid(column=0, row=3, ipadx=x_padding+25, ipady=y_padding, padx=tupple_y_margin, pady=y_margin)
        row = 0
        self.numenButton.grid(column=1, row=row, ipadx=20, ipady=10, padx=5, pady=5)
        self.numtoButton.grid(column=2, row=row, ipadx=20, ipady=10, padx=5, pady=5)
        self.numtreButton.grid(column=3, row=row, ipadx=20, ipady=10, padx=5, pady=5)
        row += 1
        self.numfireButton.grid(column=1, row=row, ipadx=20, ipady=10, padx=5, pady=5)
        self.numfemButton.grid(column=2, row=row, ipadx=20, ipady=10, padx=5, pady=5)
        self.numseksButton.grid(column=3, row=row, ipadx=20, ipady=10, padx=5, pady=5)
        row += 1
        self.numsyvButton.grid(column=1, row=row, ipadx=20, ipady=10, padx=5, pady=5)
        self.numotteButton.grid(column=2, row=row, ipadx=20, ipady=10, padx=5, pady=5)
        self.numniButton.grid(column=3, row=row, ipadx=20, ipady=10, padx=5, pady=5)
        row += 1
        self.numnullButton.grid(column=1, row=row, ipadx=20, ipady=10, padx=5, pady=5)
        self.numnull_nullButton.grid(column=2, row=row, ipadx=20, ipady=10, padx=5, pady=5)

        self.numkommaButton.grid(column=3, row=row, ipadx=20, ipady=10, padx=5, pady=5)
        self.sumButton.grid(column=4, row=0, columnspan=1, ipadx=rectangle_padding, ipady=rectangle_padding, padx=tupple_x_margin, pady=y_margin)
        self.enterButton.grid(column=4, row=2, columnspan=1, ipadx=rectangle_padding, ipady=rectangle_padding, padx=tupple_x_margin, pady=y_margin)


    def footer(self):
        self.labelTime = tkinter.Label(self.footerFrame, text="Dette er en test")
        self.exitButton = tkinter.Button(self.footerFrame, text="Exit fullscreen", command=self.exitFullscreen)

        self.scrollUP_button = tkinter.Button(self.footerFrame, text="UP", command=self.scrollUP).grid(column=2, row=0)
        
        self.openPCI_Button = tkinter.Button(self.footerFrame, text="Kort", command=self.openPCI_Func)

        #Position
        self.labelTime.grid(column=0, row=0)
        self.exitButton.grid(column=1, row=0)

        self.openPCI_Button.grid(column=3, row=0)

    # Functions
    def exitFullscreen(self):
        #self.hovedvindu.attributes('-fullscreen', False)  # FULLSCREEN OFF
        self.hovedvindu.destroy()

    def numpad(self, num):
        self.entry.insert(tkinter.END, num)

    def enterKEY_Funk(self, hendelse):
        self.enterFunk()

    def enterFunk(self):
        artikel = self.entry.get()
        try:
            self.entry.delete(0, tkinter.END)
            print(artikel)

            artikel = db.searchInRecords_kassen(artikel)
            print(f"artikel: {artikel}")
            print(type(artikel[4]))
            if artikel:
                itemTuple = (artikel[1], artikel[3], f"{artikel[4]}kr")
                self.artiklerIKurv.append(artikel[4])
                self.display_treeview.insert("", "end", value=itemTuple)
                self.treeListe = self.display_treeview.get_children()
                self.treeListLen = len(self.treeListe)
                if self.treeListLen > 1:
                    textTil_antallArtikler_stringvar = "artikler"
                else:
                    textTil_antallArtikler_stringvar = "artikel"
                self.antallArtikler_stringvar.set(f"{self.treeListLen} {textTil_antallArtikler_stringvar}")
        except TypeError:
            pass


    def slett(self):
        self.entry.delete(0, tkinter.END)

    def gjorIngenting(self): # Denne skal slettes
        print("Jeg gjør ingenting enda!")

    def rodFunk(self):
        if self.state == 0:
            self.state = 1 # Funksjoner
        else:
            self.state = 0 # Tilbake til start

        self.endreFunksjonsKnapp()

    def gronnFunk(self):
        pass

        self.endreFunksjonsKnapp()

    def gulFunk(self):
        if self.state == 1:
            self.state = 3
        self.endreFunksjonsKnapp()

    def blueFunk(self):
        pass

    def orangeFunk(self):
        pass

    def purpleFunk(self):
        pass

    def hvitFunk(self):
        if self.state == 0:
            self.state = 2 # Betalinger

        self.endreFunksjonsKnapp()

    def endreFunksjonsKnapp(self):
        self.rodStringvar.set("F1\n" + rodListe[self.state])
        self.gronnStringvar.set("F2\n" + gronnListe[self.state])
        self.gulStringvar.set("F3\n" + gulListe[self.state])
        self.blaStringvar.set("F4\n" + blaListe[self.state])
        self.orangeStringvar.set("F5\n" + orangeListe[self.state])
        self.lillaStringvar.set("F6\n" + lillaListe[self.state])
        self.hvitStringvar.set("F7\n" + hvitListe[self.state])

    def sumFunk(self):
        price = 0
        for item in self.artiklerIKurv:
            price += item
        self.sumStringvar.set(f"{round(price)},-")

    def selectFromTree_func1(self):
        #print(len(self.display_treeview.selection()))
        try:
            self.treeviewID = self.display_treeview.get_children()[self.treeviewID]
            self.display_treeview.focus(self.treeviewID)
            self.display_treeview.selection_set(self.treeviewID)
            print(self.treeviewID)
            self.treeviewID = 1
            self.treeviewID = self.display_treeview.get_children()[self.treeviewID]
            self.display_treeview.focus(self.treeviewID)
            self.display_treeview.selection_set(self.treeviewID)
            print(self.treeviewID)
            self.treeviewID = 0
            self.treeviewID = self.display_treeview.get_children()[self.treeviewID]
            self.display_treeview.focus(self.treeviewID)
            self.display_treeview.selection_set("I010")
            print(self.treeviewID)
        except IndexError:
            pass



    def selectFromTree_func(self, hendelse):
        try:
            row_id = self.display_treeview.selection()[0]
            selection = self.display_treeview.set(row_id)
            # --> Selection = ["artikelNR", "Artikel", "Pris"]
            for item in selection:
                print(item)
        except IndexError:
            pass

    def scrollUP(self):
        self.treeListe
        self.currentScollPOS += 1
        try:
            row_id = 'I001' #self.display_treeview.selection()[self.currentScollPOS]
            self.display_treeview.set(row_id)
        except IndexError:
            pass

        #Representasjon av elementene i forhold til hvordan skrolling fungerer
        #('I001', 'I002', 'I003', 'I004', 'I005', 'I006', 'I007', 'I008', 'I009', 'I00A', 'I00B', 'I00C', 'I00D', 'I00E', 'I00F', 'I010', 'I011', 'I012', 'I013', 'I014', 'I015', 'I016', 'I017', 'I018', 'I019', 'I01A', 'I01B', 'I01C', 'I01D', 'I01E')


        

        #print(self.treeviewID)
        #self.display_treeview.selection_set(self.treeviewID)
        #self.display_treeview.selection_set("I010")

    def openPCI_Func(self):
        KortBetaling(self.hovedvindu)


class Login: #INGEN LOGIKK MED BRUKENAVN OG PASSORD SKAL LAGE DATABASE!!!!!
    def __init__(self):
        self.frame = tkinter.Tk()

        self.title_label = tkinter.Label(self.frame, text="Login").grid(column=0, row=0, columnspan=2)

        self.username_label = tkinter.Label(self.frame, text="Username: ").grid(column=0, row=1)
        self.password_label = tkinter.Label(self.frame, text="Password: ").grid(column=0, row=2)
        self.username = tkinter.Entry(self.frame).grid(column=1, row=1)
        self.password = tkinter.Entry(self.frame, show="*").grid(column=1, row=2)
        self.button = tkinter.Button(self.frame, text="Login", command=self.loginFunc).grid(column=0, row=3, columnspan=2)


        #EVENTS
        self.frame.bind('<Return>', self.loginFunc)

        tkinter.mainloop()




    def loginFunc(self, hendelse=0):
        self.frame.destroy()
        GuiKasse(1)
        



if __name__ == "__main__":
    #guiKasse = GuiKasse()
    #Login()
    GuiKasse(1)
