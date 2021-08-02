
artikkler = {"70-8000": ["Bærepose S", 1.00, 999], "70-8001": ["Bærepose M", 2.00, 999], "70-101": ["Bærepose L", 3.00, 999]}

class Database:  # Midlertidlig får testning
    def __init__(self):
        self.artikler = {"70-8000": ["Bærepose S", 1.00, 999], "70-8001": ["Bærepose M", 2.00, 999], "70-101": ["Bærepose L", 3.00, 999]}

    def printToScreen(self, key):
        liste = self.artikler[key]
        space = " "
        
        return f"{key}{space}{liste[0]}  {liste[1]}kr"

    def editQuantity(self, key, quantity):
        self.artikler[key][2] += quantity



db = Database()

print(db.printToScreen("70-8000"))
db.editQuantity("70-8000", -2)
print(db.printToScreen("70-8000"))

