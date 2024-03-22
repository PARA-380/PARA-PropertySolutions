# from JsonReader import jsonwriter as json
# import array
from Entity import Entity
from Tenant import Tenant


class Account(Entity):
    def __init__(self, first: str = "", last: str = "", username: str = "", password: str = "", tenants: list = None, total_revenue={},
                 dashboard={}, contractors: list = None):
        self.firstName = first
        self.lastName = last
        self.ID = None
        self.username = username
        self.password = password  # might want to implement a security feature for storing passwords in json files
        self.properties = {}
        self.tenants = [] 
        self.contractors = [] if contractors is None else contractors

    def __repr__(self):
        return f"Account {self.__dict__}"
    
    def __createID(self, ID):
        self.ID = ID
    
    def getID(self):
        assert self.ID != None
        return self.ID
    
    def addTenant(self, var):
        self.tenants.append(var)

    def addContractor(self, var):
        self.contractors.append(var)

    def set_firstName(self, first):
        self.firstName = first
    
    def set_lastName(self, last):
        self.lastName = last

    def get_firstName(self):
        return self.firstName
    
    def get_lastName(self):
        return self.lastName 

    def get_name(self):
        return self.firstName + self.lastName

    def set_username(self, username):
        self.username = username

    def get_properties(self):
        for p in self.properties:
            print(p)

    def get_tenants(self):
        for t in self.tenants:
            print(t)

    def get_username(self):
        return self.username

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password

    def get_contractors(self):
        for c in self.contractors:
            print(c)

    def to_dict(self):
        return {
            "first": self.firstName, "last": self.lastName, "username": self.username, "password": self.password, "properties": self.properties,
            "tenants": [tenant.to_dict() for tenant in self.tenants], "contractors": self.contractors
        }
    
    def to_sql(self):
        pass

    """
    def toJSON(self):
        import json
        return json.dumps(self.to_dict())
    """


def main() -> None:
    user = Account(name="Ridham", username="RidhamPlaysValorant123", password="iluv1D")
    person = Tenant("Ridham")
    person2 = Tenant("Adrian", "Carreno", "012-34-5678", "AHHHHHH", "(805) xxx - xxxx")
    user.addTenant(person)

    person2.toJSON()
    user.toJSON()


if __name__ == "__main__":
    main()