
standardFunction = ["Funksjoner", "Endre antall", "Søk artikel", "Prisforespørsel", "Fjern artiel", "Lojalitet", "Betaling", ""]

functions = ["Tilbake", "Artikler", "Andre funksjoner", "Linjerabatt", "E-tjenester", "Kviteringsfunksjoner", "Velikehold"]
articles = ["Tilbake", "", "", "", "", "Varegruppe", "", ""]
otherFunctions = ["Tilbake", "Linjeretur", "", "", "", "", ""]
recipsFunctions = ["Tilbake", "Skriv ut siste kvittering", "Gavekvittering", "Delsum", "Parker kvittering", "Makuler kvittering", "", "Kommentar"]
vedlikehold = ["Tilbake", "Endre passord", "Opplæringsmodus", "Logg ut", "Åpne kasseskuff", "Z-...", "Dagsutlogging"]

payment = ["Tilbake", "Kontanter", "Kort", "Rabatter", "Øvringe betalingsmetoder", "", "Andre valautaer"]
discount = ["Tilbake", "Rabattbeløp", "Rabattprosent", "Personalrabatt", "", ""]
otherPayments = ["Tilbake", "", "", "", "", "Faktua" ""]



functionButtons_matrix = [[functions, articles, otherFunctions, recipsFunctions, vedlikehold],
                          [],
                          [],
                          [],
                          [],
                          [],
                          [payment, discount, otherPayments],
                          []]


class FunctionsKeys:
    def __init__(self):
        pass
    
    def buttonPressed(self, button):
        self.button = button

def printListe(liste):
    items = ""
    for item in liste:
        items += item + "\n"
    return items



if __name__ == '__main__':
    y = 0
    print(printListe(standardFunction))

    
    x = int(input("Skriv inn: "))

    print(printListe(functionButtons_matrix[x][y]))

    while True:
        y = int(input("Skriv inn: "))
        if x != 0:

            print(printListe(functionButtons_matrix[x][y]))
            if y != 1:
                y += 1
            else:
                print(printListe(functionButtons_matrix[x][y]))
                y, x = 0, 0
        
        if y < 0:
            x = 0

        else:
            print(printListe(standardFunction))
        
        
        