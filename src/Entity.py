from JsonReader import jsonwriter as json
from abc import ABC

#This class will define the default attributes of any object that can be written as a JSON file to be saved.

class Entity(ABC):
    
    def toJSON(self):
        json.write()
        pass

    def toObj(self):
        json.read()
        pass