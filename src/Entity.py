from JsonReader import jsonwriter as json
from abc import ABC
class Entity(ABC):
    
    def toJSON(self):
        json.write(self.__dict__)
        pass