from Tenant import Tenant


class Account():
    def __init__(self, first: str = "", last: str = "", username: str = "", password: str = "", phone : str = "", tenants: list = None, total_revenue={},
                 dashboard={}, contractors: list = None):
        self.firstName = first
        self.lastName = last
        self.ID = None
        self.phoneNumber = phone
        self.username = username
        self.password = password  # might want to implement a security feature for storing passwords in json files

    def __repr__(self):
        return f"Account {self.getID()} {self.__dict__}"
    
    def setID(self, ID):
        self.ID = ID
    
    def getID(self):
        assert self.ID != None
        return self.ID
    
    def addTenant(self,id, tenant):
        self.tenants[id] = tenant

    def remove_tenant(self, key):
        self.tenants.pop(key)

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
    
    def get_phonenumber(self):
        return self.phoneNumber
    
    def set_phonenumber(self, phone):
        self.phoneNumber = phone

    def set_username(self, username):
        self.username = username

    def get_properties(self):
        for p in self.properties:
            print(p)

    def print_tenants(self):
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

def main() -> None:
    user = Account(name="Ridham", username="RidhamPlaysValorant123", password="iluv1D")
    person = Tenant("Ridham")
    person2 = Tenant("Adrian", "Carreno", "012-34-5678", "AHHHHHH", "(805) xxx - xxxx")
    user.addTenant(person)


if __name__ == "__main__":
    main()
