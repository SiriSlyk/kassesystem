

#["red", "green", "yellow", "blue", "orange", "purple", "white", "gray"]
#State = 0 -> Hovedmeny
redFunksjon1 = ["Tilbake", "Artikkel", "Flere funksjoner", "Linjerabatt", "E-tjenester", "Kvitteringsfunksjoner", "Velikehold", ""]
whiteBetaling1 = ["Tilbake", "Kontanter", "Kort", "Rabatter", "Øvrige betalingsmåter", "", "Valutaer", ""]
greenArtikler2 = ["Tilbake", "", "", "", "", "", "Varegruppe", ""]
yellowFlereFunksjoner2 = ["Tilbake", "Linjeretur", "", "", "", "", "", ""]
purpleKvitteringsfunksjoner2 = ["Tilbake", "Skriv ut siste kvittering", "Gavekvittering", "Delsum", "Parker kvittering", "Makuler kvittering", "", "Kommentar", ""]
whiteVelikehold = ["Tilbake", "Endre passord", "Opplæringsmodus", "Logg av", "", "", "Åpne kasseskuff", ""]
blueRabatter = ["Tilbake", "Rabattbeløp", "Rabattprosent", "Personalrabatt", "", "", "", ""]

class FunctionKeys:
    def __init__(self):
        self.state = "start"

    def redButton(self):
        if self.state == "start":
            self.state == "funksjoner"
            return redFunksjon1
        else:
            print("TILBAKE")

    def greenButton(self):
        if self.state == "start":
            print("ENDRE ANTALL")
        if self.state == 1:
            self.state == 2
            return greenArtikler2

    def yellowButton(self):
        if self.state == "start":
            print("SØK ARTIKKEL")

    def blueButton(self):
        if self.state == "start":
            print("PRISFORESPØRSEL")

    def orangeButton(self):
        if self.state == "start":
            print("FJERN ARTIKKEL")

    def purpleButton(self):
        if self.state == "start":
            print("LOJALITET")

    def whiteButton(self):
        if self.state == "start":
            self.state == 1
            return whiteBetaling1
    def grayButton(self): #NOT IN USE YET
        pass