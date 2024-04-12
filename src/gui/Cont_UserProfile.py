from System import Account, db
# from gui.UserProfile import Userprofile

class Cont_UserProfile:

    def __init__(self, mainAccount : Account = None):
        self.mainAccount = mainAccount
        pass

    def __setMainAccount(self, acc : Account = None):
        self.mainAccount = acc

    def _getMainAccount(self):
        return self.getMainAccount()
    
    def _searchAccount(self, accID : int) -> None:
        self.__setMainAccount(db.readAccount(accID))

    def _updateAccount(self, account : Account):
        """updates account with accID in database.
           and updates self main account
        Args:
            accID (_type_): account ID to be updated in Database
        """
        db.updateAccount(account)
        self._searchAccount(account.getID())
        pass
    
    def _createAccount(self, first, last, username, password):
        acc = Account(first,last,username,password)
        acc.setID(db.addToAccounts(acc))
        self.__setMainAccount(acc)
        # try:
        #     db.addToAccounts(acc)
        #     self.Accounts.append(acc)
        # except:
        #     print(f"{acc} already exists!")
        #     pass