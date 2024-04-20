from System import Property, db

class Cont_Property:
    def __init__(self, accID : int = None):
        self.mainAccountID = accID

    def createProperty(self, property : Property):
        db.addToProperty(accID=self.mainAccountID, property=property)

    def getProperties(self):
        db.readProperty(self.mainAccountID)