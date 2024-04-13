from System import Account, db, Cont_UserProfile


class Cont_Login:

    def __init__(self):
        self.cont_user = Cont_UserProfile()

    def getUserProfile(self) -> Cont_UserProfile:
        """returns Controller User Profile. Mainly for System to use.

        Returns:
            Cont_UserProfile: Controller for Main Account User
        """
        return self.cont_user

    def validateLogin(self, temp_username ="", temp_password = "") -> bool:
        users = self.searchAccount(temp_username) #returns Account objects
        for account in users:
            if temp_password is account.get_password():
                print(f'account match! : {account}')
                self.cont_user.__setMainAccount(account)
                return True
        return False

    def searchAccount(self, username = "") -> list[Account]:
        users : list[Account] = db.searchAccount(username)
        return users
    
    #TODO:
    def createAccount():
        pass

