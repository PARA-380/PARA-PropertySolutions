from Entity import Entity
from Account import Account
from Property import Property
from Tenant import Tenant
import Database as db

class System():
    def __init__(self):
        self.Accounts = []
        pass

    def __repr__(self):
        return f"Accounts: {self.Accounts}"

    def StartSession(self):
        #TODO:
        #take in username and password and find corresponding Object
        #load data from JSON file and create Account Object
        db.init()
        db.cleartables()
        db.createTables()
        pass

    def EndSession(self):
        #Save data from Account object into JSON file
        pass

    def _createAccount(self, first, last, username, password):
        acc = Account(first,last,username,password)
        db.addToAccounts(acc)
        self.Accounts.append(acc)
        # try:
        #     db.addToAccounts(acc)
        #     self.Accounts.append(acc)
        # except:
        #     print(f"{acc} already exists!")
        #     pass
        pass


def main() -> None:
    session1 = System()
    session1.StartSession()
    session1._createAccount("ali","maamoun","amaamoun21","comp380")
    print(session1.Accounts)
    pass

if __name__ == "__main__":
    main()
    pass