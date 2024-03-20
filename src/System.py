from Entity import Entity
from Account import Account
from Property import Property
from Tenant import Tenant

class System():
    def __init__(self):
        self.Accounts : Account = {}
        pass

    def __repr__(self):
        return f"Accounts: {self.Accounts}"

    def StartSession():
        #TODO:
        #take in username and password and find corresponding Object
        #load data from JSON file and create Account Object
        pass

    def EndSession():
        #Save data from Account object into JSON file
        pass



def main() -> None:
    session1 = System()
    print(session1.Accounts)
    pass

if __name__ == "__main__":
    main()
    pass