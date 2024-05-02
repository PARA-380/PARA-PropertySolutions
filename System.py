"""
File: System.py
Name: Adrian Carreno, Ali Maamoun
Date: 04/23/24
Description: A system to handle controllers and a single session. Connects the Database to the rest of the application.
Purposes: an instance is called a 'session', The parent controller which handles their creation, and passing to other classes like GUI elements.
Passes the database file to controllers that need to import from System.
"""


from src.Entities.Account import Account
from src.Entities.Property import Property
from src.Entities.Tenant import Tenant
from src.Entities.Contractor import Contractor
from src.Entities.Bills import Bills
import src.Database.Database as db

from src.Cont_UserProfile import Cont_UserProfile
from src.Cont_Login import Cont_Login
from src.Cont_Tenant import Cont_Tenant
from src.Cont_Contractor import Cont_Contractor
from src.Cont_Property import Cont_Property
from src.Cont_Bills import Cont_Bills

class System():
    def __init__(self, main : Account = None):
        """
        Assigns main Account and sets up controllers
        @param main:
        @type main:
        """
        self.Accounts : Account = {}
        self.mainAccount : Account = main
        #controllers
        self.cont_userprofile : Cont_UserProfile
        self.cont_login : Cont_Login
        self.cont_tenant : Cont_Tenant
        self.cont_contractor : Cont_Contractor
        self.cont_property  : Cont_Property
        self.cont_bills : Cont_Bills
        #setup database and controllers
        self.StartSession()
        
        pass

    def __repr__(self):
        """
        Sets designated way of printing
        @return:
        @rtype:
        """
        return f"Accounts: {self.Accounts}"
    
    def setMainAccount(self, accID):
        """
        Sets the main account by using its ID from Database
        @param accID:
        @type accID:
        @return:
        @rtype:
        """
        self.mainAccount = self.getAccount(accID)

    def getMainAccount(self):
        """
        Returns Main Account
        @return:
        @rtype:
        """
        return self.mainAccount
    
    def getAccount(self,accID):
        """
        Returns Account base off of ID
        @param accID:
        @type accID:
        @return:
        @rtype:
        """
        return self.Accounts.get(accID)

    def StartSession(self):
        """
        Initializes Database and creates Login Controller
        @return:
        @rtype:
        """
        #TODO:
        #take in username and password and find corresponding Object
        #load data from JSON file and create Account Object
        
        db.init()
        try:
            #db.cleartables()    #for testing purposes
            db.createTables()   #creates the Account, Tenant, Property, etc. Tables
        except:
            pass
        self.cont_login = Cont_Login()
        
        #login will be validating here before creating user profile
        pass
    
    def setControllerUserProfile(self): #change name to setupControllers
        """
        Sets the controller to the active account in session
        @return:
        @rtype:
        """
        self.cont_userprofile = self.cont_login.getUserProfile()
        self.mainAccount = self.cont_userprofile.getMainAccount()
        self.cont_tenant = Cont_Tenant(self.mainAccount.getID()) #review this line
        self.cont_property = Cont_Property(self.mainAccount.getID())
        self.cont_contractor = Cont_Contractor(self.mainAccount.getID())

    def EndSession(self):
        """
        Supposed to close Database after Logout or page application exit
        @return:
        @rtype:
        """
        #Save data from Account object into Database and close session
        print(f'ending session...')
        pass



    



def main() -> None:
    session1 = System()
    session1.StartSession()
    session1.cont_userprofile.createAccount()

    #Search Database to create an Account Class
    session1.cont_userprofile.searchAccount(1)
    #print(f"Account Searched: {session1.cont_userprofile.mainAccount}")


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