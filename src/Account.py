# from JsonReader import jsonwriter as json
import array
from Entity import Entity
from Tenant import Tenant


class Account(Entity):
    def __init__(self, name: str = "", username: str = "", password: str = "", tenants: list = None, total_revenue={},
                 dashboard={}):
        self.name = name
        self.username = username
        self.password = password  # might want to implement a security feature for storing passwords in json files
        self.properties = {}
        self.tenants = [] if tenants is None else tenants
        self.contractors = {}

    def addTenant(self, var):
        self.tenants.append(var)

    def addContractor(self):
        pass

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
    print(user.toJSON())
    user.addTenant(person2)
    print()
    print(user.toJSON())


if __name__ == "__main__":
    main()
