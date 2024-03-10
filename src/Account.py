#from JsonReader import jsonwriter as json
from Entity import Entity
from Tenant import Tenant


class Account(Entity):
    def __init__(self, name : str = "", username : str = "", password : str = "", tenants : Tenant = {}):
        self.name = name
        self.username = username
        self.password = password    #might want to implement a security feature for storing passwords in json files
        self.properties = {}
        self.tenants = tenants
        self.contractors = {}
        # self.dashboard
    


user = Account("Ridham",username="RidhamPlaysValorant123",password="iluv1D")

user.toJSON()