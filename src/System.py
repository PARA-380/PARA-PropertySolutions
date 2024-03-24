from Entity import Entity
from Account import Account
from Property import Property
from Tenant import Tenant
import Database as db

class System():
    def __init__(self):
        self.Accounts = {}
        pass

    def __repr__(self):
        return f"Accounts: {self.Accounts}"

    def StartSession(self):
        #TODO:
        #take in username and password and find corresponding Object
        #load data from JSON file and create Account Object
        db.init()
        db.cleartables()    #for testing purposes
        db.createTables()   #creates the Account, Tenant, Property, etc. Tables
        pass

    def EndSession(self):
        #Save data from Account object into Database and close session
        pass

    def _createAccount(self, first, last, username, password):
        acc = Account(first,last,username,password)
        acc.setID(db.addToAccounts(acc))
        self.Accounts[acc.getID()] = acc
        # try:
        #     db.addToAccounts(acc)
        #     self.Accounts.append(acc)
        # except:
        #     print(f"{acc} already exists!")
        #     pass
        pass

    def _createTenant(self,account : Account, first="",last="",ssn="",address="",phone="",email=""):
        ten = Tenant(firstname=first,lastname=last,ssn=ssn,address=address,phonenumber=phone,email=email)
        ten.setID(db.addToTenants(account,ten))
        account.addTenant(ten)

        return ten

    def _searchAccount(self, account : Account):
        pass


def main() -> None:
    session1 = System()
    session1.StartSession()
    session1._createAccount("ali","maamoun","amaamoun21","comp380")
    session1._createAccount("Ridham","Patel","rpatel20223","valorant")

    print(session1.Accounts)

    #add tenants to account 1
    user1 = session1.Accounts.get(2)
    tenant = session1._createTenant(user1,"joe","mamma","34212","431 Yojatruz Road", "3421023322","joemamma@csun.edu")
    print(f"added tenant {tenant}")
    pass

if __name__ == "__main__":
    main()
    pass