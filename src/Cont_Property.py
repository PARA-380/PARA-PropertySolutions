from System import Property, db

class Cont_Property:
    def __init__(self, accID : int = None):
        self.mainAccountID = accID
        self.Properties = self.getProperties()
        

    def createProperty(self, property : Property):
        db.addToProperty(accID=self.mainAccountID, property=property)

    def getProperties(self) -> list[Property]:
        return db.readProperty(self.mainAccountID)