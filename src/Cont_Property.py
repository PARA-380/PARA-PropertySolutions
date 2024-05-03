from System import Property, db

class Cont_Property:
    def __init__(self, accID : int = None):
        self.mainAccountID = accID
        self.Properties = self.getProperties()
        self.property_IDs = { #[property_number] : property_ID
            }


    def createProperty(self, property : Property = Property()) -> int:
        new_id = db.addToProperty(accID=self.mainAccountID, property=property)
        self.Properties = self.getProperties()
        return new_id
    
    def deleteProperty(self, prop_number : int):
        prop_id = self.property_IDs.pop(prop_number)
        db.deleteProperty(prop_id)
        self.Properties = self.getProperties()


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

    def find_property_by_id(self, prop_id):
        for property in self.Properties:
            if property.get_property_id() == prop_id:
                return property
        print("Property not found")
        return None

    def get_property_address(self, prop_id: int):
        return self.find_property_by_id(prop_id).get_address()

    def update_address(self, address: str, prop_id: int):
        self.Properties = self.getProperties()
        prop = self.find_property_by_id(prop_id)
        prop.set_address(address)
        db.updateProperty(prop)

    def update_link_images(self, link_images: str, prop_id: int):
        self.Properties = self.getProperties()
        prop = self.find_property_by_id(prop_id)
        prop.set_link_images(link_images)
        db.updateProperty(prop)

    def get_property_link_images(self, prop_id: int):
        return self.find_property_by_id(prop_id).get_link_images()
    
