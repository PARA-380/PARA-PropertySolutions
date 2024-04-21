from System import Property, db

class Cont_Property:
    def __init__(self, accID : int = None):
        self.mainAccountID = accID
        self.Properties = self.getProperties()
        self.property_IDs = { #[property_number] : property_ID
            }


    def createProperty(self, property : Property):
        db.addToProperty(accID=self.mainAccountID, property=property)

    def getProperties(self) -> list[Property]:
        return db.readProperty(self.mainAccountID)

    def addPropertyID(self,key,ID):
        self.property_IDs[key] = ID
    
    def getPropertyID(self, key):
        return self.property_IDs[key]

    #TODO: setters and getters for Address and other attributes
        #get a property from property_IDs and return a requested value
        #get_property_Address should search the list find the property by ID then return its address.
        #note: might only be able to give a property_number key... so keep in mind when translating.
        #note: you can look up by property number in dictionary if given a key.

    #TODO: Reading Database and putting Address in GUI