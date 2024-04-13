from System import Account, db
# import Database as db
# from gui.UserProfile import Userprofile

class Cont_UserProfile:
    """Creates a controller of the Account Class. Maintains the main Account object and its database state
    """
    def __init__(self, mainAccount : Account = None):
        """Constructor of Controller User Profile

        Args:
            mainAccount (Account, optional): The main account associated to the Controller. Defaults to None.
        """
        self.mainAccount = mainAccount
        # self.createAccount(self.mainAccount)
        pass

    def setMainAccount(self, acc : Account = None):
        """Sets the main Account Object of this controller

        Args:
            acc (Account, optional): Account object to be the main Account of this controller. Defaults to None.
        """
        self.mainAccount = acc

    def getMainAccount(self) -> Account:
        """Returns the main Account Object

        Returns:
            Account: The main account object
        """
        return self.mainAccount

    def searchAccount(self, accID : int) -> None:
        """Searches the Database for the account associated with its ID

        Args:
            accID (int): The account ID to be searched for in the database
        """
        self.__setMainAccount(db.readAccount(accID))

    def updateAccount(self, accID : int, tempAcc : Account):
        """updates account with accID in database.
           and updates self main account
        Args:
            accID (_type_): account ID to be updated in Database
        """
        self.mainAccount.set_firstName(tempAcc.get_firstName())
        self.mainAccount.set_lastName(tempAcc.get_lastName())
        self.mainAccount.set_username(tempAcc.get_username())
        self.mainAccount.set_phonenumber(tempAcc.get_phonenumber())
        db.updateAccount(self.mainAccount)
        self.searchAccount(self.mainAccount.getID())

    def createAccount(self, account: Account):
        """Creates an Account and sets it as the main account. Useful for Signing up for an account

        Args:
            first (_type_): First Name 
            last (_type_): Last Name    
            username (_type_): Username
            password (_type_): Password
        """
        acc = account
        acc.setID(db.addToAccounts(acc))
        self.__setMainAccount(acc)

        # try:
        #     db.addToAccounts(acc)

        # except:
        #     print(f"{acc} already exists!")
        #     pass
        # self.Accounts.append(acc)
        pass