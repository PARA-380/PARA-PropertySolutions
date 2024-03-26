# from JsonReader import jsonwriter as json
# import array
from Entity import Entity
from Tenant import Tenant


class Account(Entity):
    def __init__(self, name: str = "", username: str = "", password: str = "", tenants: list = None, total_revenue={},
                 dashboard={}, contractors: list = None):
        self.name = name
        self.username = username
        self.password = password  # might want to implement a security feature for storing passwords in json files
        self.properties = []
        self.tenants = [] #if tenants is None else tenants
        self.contractors = [] #if contractors is None else contractors

    def addTenant(self, var):
        self.tenants.append(var)

    def addContractor(self, var):
        self.contractors.append(var)

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

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
            "name": self.name, "username": self.username, "password": self.password, "properties": self.properties,
            "tenants": [tenant.to_dict() for tenant in self.tenants], "contractors": self.contractors
        }

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
    user.addTenant(person2)
    # print(person2.__dict__)
    print(user.__dict__)


if __name__ == "__main__":
    main()
