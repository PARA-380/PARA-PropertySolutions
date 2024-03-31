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
    
    def getAccount(self,accID):
        return self.Accounts.get(accID)

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

    def _searchAccount(self, accID) -> Account:
        return db.readAccount(accID)
    
    def _searchTenants(self, accID, tenID=None):
        if(tenID == None):
            return db.readTenants(accID,tenID)


def main() -> None:
    session1 = System()
    session1.StartSession()
    session1._createAccount("ali","maamoun","amaamoun21","comp380")
    session1._createAccount("Ridham","Patel","rpatel20223","valorant")

    print(session1.Accounts)

    #add tenants to account 1
    user1 = session1.Accounts.get(2)
    tenant = session1._createTenant(user1,"joe","mamma","34212","431 Yojatruz Road", "3421023322","joemamma@csun.edu")
    tenant = session1._createTenant(user1,"jacob","issa","332255","870 This is a Road", "8008135","JacobIssa@csun.edu")
    tenant = session1._createTenant(user1,"Laska","MyDog","553324","870 This is a Road", "N/A","Laskipoo@csun.edu")
    print(f"added tenant {tenant}")

    #Search Database to create an Account Class
    print(f"Account Searched: {session1._searchAccount(2)}")
    print(f"Tenants Read: {session1._searchTenants(2)}")

    pass

if __name__ == "__main__":
    main()
    pass