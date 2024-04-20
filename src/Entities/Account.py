from .Tenant import Tenant


class Account:

    def __init__(self, first: str = "", last: str = "", username: str = "", password: str = "", phone : str = ""):
        """
        @param first:
        @param last:
        @param username:
        @param password:
        @param phone:
        """
        self.firstName = first
        self.lastName = last
        self.ID = None
        self.phoneNumber = phone
        self.username = username
        self.password = password  # might want to implement a security feature for storing passwords in json files


    def __repr__(self):
        """
        Specifies how class will be printed
        @return:
        """
        return f"Account {self.getID()} {self.__dict__}"
    
    def setID(self, ID):
        """
        Sets the Account ID
        @type ID: object
        """
        self.ID = ID
    
    def getID(self):
        """
        Returns the Account ID
        @return:
        """
        assert self.ID != None
        return self.ID
    
    def addTenant(self,id, tenant):
        """
        Adds Tenants to the list
        @param id:
        @param tenant:
        @return:
        """
        self.tenants[id] = tenant

    def remove_tenant(self, key):
        """
        Removes Tenants from the list
        @param key:
        @return:
        """
        self.tenants.pop(key)

    def addContractor(self, var):
        self.contractors.append(var)

    def set_firstName(self, first):
        """
        Sets the First Name of the account
        @param first:
        @return:
        """
        self.firstName = first
    
    def set_lastName(self, last):
        """
        Sets the Last Name of the account
        @param last:
        @return:
        """
        self.lastName = last

    def get_firstName(self):
        """
        Returns the First Name of the account
        @return:
        """
        return self.firstName
    
    def get_lastName(self):
        """
        Returns the Last Name of the account
        @return:
        """
        return self.lastName 

    def get_name(self):
        """
        Returns both First and Last name of the account
        @return:
        """
        return self.firstName + self.lastName
    
    def get_phonenumber(self):
        """
        Returns the Phone Number of the account
        @return:
        """
        return self.phoneNumber
    
    def set_phonenumber(self, phone):
        """
        Sets the Phone Number of the account
        @param phone:
        @return:
        """
        self.phoneNumber = phone

    def set_username(self, username):
        """
        Sets the Username for the account
        @param username:
        @return:
        """
        self.username = username

    def get_properties(self):
        """
        Prints a list of Properties
        @return:
        """
        for p in self.properties:
            print(p)

    def print_tenants(self):
        """
        Prints a list of tenants
        @return:
        """
        for t in self.tenants:
            print(t)

    def get_username(self):
        """
        Returns the Username of the account
        @return:
        """
        return self.username

    def set_password(self, password):
        """
        Sets the Password for the account
        @param password:
        @return:
        """
        self.password = password

    def get_password(self):
        """
        Returns the Password for the account
        @return:
        """
        return self.password

    def get_contractors(self):
        """
        Prints a list of Contractors
        @return:
        """
        for c in self.contractors:
            print(c)

    def to_dict(self):
        """
        Returns Print statement for account class
        @return:
        """
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
