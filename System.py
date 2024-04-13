from src.Entities.Account import Account
from src.Entities.Property import Property
from src.Entities.Tenant import Tenant
import src.Database.Database as db

from src.Cont_UserProfile import Cont_UserProfile
from src.Cont_Login import Cont_Login

class System():
    def __init__(self, main : Account = None):
        self.Accounts : Account = {}
        self.mainAccount : Account = main
        #controllers
        self.cont_userprofile : Cont_UserProfile
        self.cont_login : Cont_Login
        #setup database and controllers
        self.StartSession()
        
        pass

    def __repr__(self):
        return f"Accounts: {self.Accounts}"
    
    def setMainAccount(self, accID):
        self.mainAccount = self.getAccount(accID)

    def getMainAccount(self):
        return self.mainAccount
    
    def getAccount(self,accID):
        return self.Accounts.get(accID)

    def StartSession(self):
        #TODO:
        #take in username and password and find corresponding Object
        #load data from JSON file and create Account Object
        
        db.init()
        try:
            # db.cleartables()    #for testing purposes
            db.createTables()   #creates the Account, Tenant, Property, etc. Tables
        except:
            pass
        self.cont_login = Cont_Login()
        #login will be validating here before creating user profile
        pass
    
    def setControllerUserProfile(self):
        self.cont_userprofile = self.cont_login.getUserProfile()

    def EndSession(self):
        #Save data from Account object into Database and close session
        print(f'ending session...')
        pass

    def createAccount(self, first, last, username, password):
        """_summary_

        Args:
            first (_type_): _description_
            last (_type_): _description_
            username (_type_): _description_
            password (_type_): _description_
        """
        acc = Account(first,last,username,password)
        acc.setID(db.addToAccounts(acc))
        self.Accounts[acc.getID()] = acc #dict.update()
        self.setMainAccount(acc.getID())
        # try:
        #     db.addToAccounts(acc)
        #     self.Accounts.append(acc)
        # except:
        #     print(f"{acc} already exists!")
        #     pass
        pass

    def createTenant(self, account : Account, first="", last="", ssn="", address="", phone="", email=""):
        ten = Tenant(firstname=first,lastname=last,ssn=ssn,address=address,phonenumber=phone,email=email)
        ten.setID(db.addToTenants(account,ten))#review whether to set ID in System or Database
        account.addTenant(ten.getID(),ten)

        return ten
    
    def createProperty(self, accID : int):
        property = Property()

    def searchAccount(self, accID : int) -> Account:
        return self.cont_userprofile._searchAccount(accID)
    
    def searchTenants(self, accID, tenID=None):
        if(tenID != None):
            return db.readTenants(accID)
        

    #UPDATE methods
    



def main() -> None:
    session1 = System()
    session1.StartSession()
    session1.cont_userprofile.createAccount()
    # session1._createAccount(first="Ridham",last="Patel",username="rpatel20223",password="valorant")

    # print(session1.Accounts)

    #add tenants to account 1
    # user1 = session1.Accounts.get(2)
    # tenant = session1._createTenant(user1,"joe","mamma","34212","431 Yojatruz Road", "3421023322","joemamma@csun.edu")
    # tenant = session1._createTenant(user1,"jacob","issa","332255","870 This is a Road", "8008135","JacobIssa@csun.edu")
    # tenant = session1._createTenant(user1,"Laska","MyDog","553324","870 This is a Road", "N/A","Laskipoo@csun.edu")
    # print(f"added tenant {tenant}")

    #Search Database to create an Account Class
    session1.cont_userprofile.searchAccount(1)
    print(f"Account Searched: {session1.cont_userprofile.mainAccount}")
    # print(f"Tenants Read: {session1._searchTenants(2)}")


    #testing update account method
    # myuser = session1.getAccount(1)
    # myuser.set_username("testing UPDATE")
    # print(myuser)
    # session1._updateAccount(myuser)
    # session1._searchAccount(myuser.getID())


    pass

if __name__ == "__main__":
    main()
    pass