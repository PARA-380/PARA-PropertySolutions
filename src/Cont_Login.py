"""
File: Cont_Login.py
Name: Adrian Carreno, Ali Maamoun
Date: 04/23/24
Description: Controller for Login_Page class
Purposes: Controller Class for Login_Page to connect Login Operations to Database and GUI.
Sets the main account to be used in active session and handles Login verification.
"""

from System import Account, db, Cont_UserProfile


class Cont_Login:
    """Connects the GUI To the Database
    """

    def __init__(self):
        """Knows Controller of User Profile, to set up the main account after logging in."""
        self.cont_user = Cont_UserProfile()

    def getUserProfile(self) -> Cont_UserProfile:
        """returns Controller User Profile. Mainly for System to use.

        Returns:
            Cont_UserProfile: Controller for Main Account User
        """
        return self.cont_user

    def setUserProfile(self, account : Account):
        """sets the User Profile Controller's Main Account it referrs to.

        Args:
            account (Account): The account to be the main account
        """
        self.cont_user.setMainAccount(account)

    def validateLogin(self, temp_username ="", temp_password = "") -> bool:
        """Boolean Method to Validate the proper username and password combination.

        Args:
            temp_username (str, optional): Given Username to search for. Defaults to "".
            temp_password (str, optional): Given Password to see if matches with given username. Defaults to "".

        Returns:
            bool: Whether the combination was a match to the Database
        """
        users = self.searchAccount(temp_username) #returns Account objects

        for account in users:
            # print(f'{account}')
            # print(f'tem_pass: {type(temp_password)}, account: {type(account.get_password())}')
            if temp_password == account.get_password():
                self.cont_user.setMainAccount(account)
                return True
        return False

    def searchAccount(self, username = "") -> list[Account]:
        """Searches the Database for the given Username

        Args:
            username (str, optional): Username to search for. Defaults to "".

        Returns:
            list[Account]: list of matching Usernames
        """
        users = db.searchAccount(username)
        return users
    
    #TODO:
    def createAccount(self, username = "", password = ""):
        """Creates an account to the Database given a username and password

        Args:
            username (str, optional): _description_. Defaults to "".
            password (str, optional): _description_. Defaults to "".
        """
        self.setUserProfile(db.addToAccounts(Account(username=username,password=password)))

