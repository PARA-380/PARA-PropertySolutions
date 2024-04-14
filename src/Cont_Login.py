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
            # print(f'{account}')
            # print(f'tem_pass: {type(temp_password)}, account: {type(account.get_password())}')
            if temp_password == account.get_password():
                print(f'account match! : {type(account)}')
                self.cont_user.setMainAccount(account)
                return True
        return False

    def searchAccount(self, username = "") -> list[Account]:
        users = db.searchAccount(username)
        return users
    
    #TODO:
    def createAccount():
        pass

