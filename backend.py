from artikler import artikler

#artikkler = {"70-8000": ["Bærepose S", 1.00, 999], "70-8001": ["Bærepose M", 2.00, 999], "70-101": ["Bærepose L", 3.00, 999]}

class Database:  # Midlertidlig får testning
    def __init__(self):
        self.artikler = artikler #{"70-8000": ["Bærepose S", 1.00, 999], "70-8001": ["Bærepose M", 2.00, 999], "70-101": ["Bærepose L", 3.00, 999]}


    def printToScreen(self, key):
        if self.checkKey(key):
            liste = self.artikler[key]
            space = " "

            return f"{key}{space}{liste[0]}  {liste[1]}kr"
        else:
            return None

    def editQuantity(self, key, quantity):
        if self.checkKey(key):
            self.artikler[key][2] += quantity

    def returnPrice(self, key):
        if self.checkKey(key):
            return self.artikler[key][1]

    def checkKey(self, key):
        try:
            if self.artikler[key]:
                return True
        except KeyError:
            return False



db = Database()

print(db.printToScreen("70-8000"))
db.editQuantity("70-8000", -2)
print(db.printToScreen("70-8000"))
print(db.printToScreen("70-800011"))
db.editQuantity("70-80000", -2)

