import sqlite3
import pytest
from src.Entities.Account import Account
from src.Entities.Tenant import Tenant

class DatabaseTest:
    def __init__(self):
        self.init()

    def init(self):
        """Starts up the Database and provides the connection and the cursor, which are crucial to executing.
        self.__cursor : is responsible for executing sql commands
        self.__conn   : is the current connection to a certain database file. (stored locally)
        """
        # global self.__conn, self.__cursor
        # self.__conn = sqlite3.connect('../data/sql.db')
        self.__conn = sqlite3.connect('data/testdb.db')
        self.__cursor = self.__conn.cursor()

    def closeConnection(self):
        """Closes connection to the Database
        """
        if self.__conn is not None:
            self.__conn.close()
            self.__conn = None
            self.__cursor = None

    def cleartables(self):
        """Clears all Database Tables for Testing purposes
        """
        # global self.__conn, self.__cursor
        #Delete Table each time run for testing purposes
        self.__cursor.execute("DROP TABLE IF EXISTS Account")
        self.__cursor.execute("DROP TABLE IF EXISTS Tenant")
        self.__cursor.execute("DROP TABLE IF EXISTS Property")
        self.__cursor.execute("DROP TABLE IF EXISTS Contractor")

    def createTables(self):
        """Creates All Tables needed for initializing the Database
        """    
        # global self.__conn, self.__cursor
            #create Table for Accounts
        self.__cursor.execute("""CREATE TABLE Account(  
                        acc_ID integer PRIMARY KEY,
                        first text,
                        last text,
                        username text,
                        phonenumber text,
                        password text
                    )""")

        #create Table for Tenants 
        #address should link to property id
        self.__cursor.execute("""CREATE TABLE Tenant(  
                        Ten_ID integer NOT NULL PRIMARY KEY AUTOINCREMENT,
                        acc_ID integer,
                        prop_ID integer,
                        first text,
                        last text,
                        ssn text,
                        address text,
                        phone text,
                        email text
                    )""")

        # create Table for Property 
        # address should link to property id
        self.__cursor.execute("""CREATE TABLE Property(
                        prop_ID integer PRIMARY KEY AUTOINCREMENT,
                        acc_ID integer,
                        address text,
                        sqft int,
                        hometype text,
                        max_living int
                    )""")
        
        # create Table for Contractors
        self.__cursor.execute("""CREATE TABLE Contractor(
                        contractor_ID integer PRIMARY KEY AUTOINCREMENT,
                        acc_ID integer,
                        specialization text,
                        first text,
                        last text,
                        phone text
                    )""")
        
        self.__conn.commit()


    def addToAccounts(self, account : Account):
        """Creates new row in Account Table and returns the KEY generated
        

        Args:
            account (Account): Account Object

        Returns:
            _type_: KEY id generated
        """
        # global self.__conn, self.__cursor
        if account is None:
            return TypeError
        self.__cursor.execute("INSERT INTO Account (first,last,username,phonenumber,password) VALUES (:first,:last,:username,:phonenumber, :password)",
                        {   
                            'first' : account.get_firstName(),
                            'last': account.get_lastName(),
                            'username': account.get_username(),
                            'phonenumber' : account.get_phonenumber(),
                            'password' : account.get_password()

                        })
        self.__conn.commit()
        account.setID(self.__cursor.lastrowid)

        #NOTICE: CHANGED to account FROM self.__cursor.lastrowid
        return account


    #Reads the database and returns an object of the account
    def readAccount(self, accID: int) -> Account:
        """Reads the Database Account Table and returns the row associated with an Account ID

        Args:
            accID (int): The Account ID to lookup as the KEY

        Returns:
            Account: an Account object with the data recieved from Database
        """
        # global self.__conn, self.__cursor

        data=self.__cursor.execute("SELECT * FROM ACCOUNT WHERE (acc_ID) = (:acc_ID)",{
            'acc_ID' : accID
        }).fetchone()
        account = Account(first=data[1],last=data[2],username=data[3],phone=data[4],password=data[5])
        account.setID(data[0])
        
        return account


    def searchAccount(self, username : str) -> list[Account]:
        """Searches the accounts based on matching usernames

        Args:
            username (str): Username to search for

        Returns:
            list[Account]: List of matching Account objects.
        """
        # global self.__conn, self.__cursor
        users = list()
        data=self.__cursor.execute("SELECT * FROM ACCOUNT WHERE (username) = (:username)",{
            'username' : username
        }).fetchall() 
        
        for user in data:
            # users.append(Account(first=user[1],last=user[2],username=user[3],phone=user[4],password=user[5]).setID(user[0]))
            acc = Account(first=user[1],last=user[2],username=user[3],phone=user[4],password=user[5])
            acc.setID(user[0])
            users.append(acc)
        return users


    #UPDATE METHODS

    def updateAccount(self, account : Account):
        """Updates the Account in the Database. Copies all its contents into exisitng Account Entry in table

        Args:
            account (Account): Account to copy
        """
        if account is None:
            return TypeError
        # global self.__conn, self.__cursor
        self.__cursor.execute("""UPDATE Account SET (first,last,username,phonenumber,password) = 
                              (:first, :last, :username,:phone, :password) WHERE (acc_ID) = (:acc_ID)""",
                              {'first': account.get_firstName(), 'last' : account.get_lastName(), 'username' : account.get_username(), 
                               'acc_ID' : account.getID(),'phone':account.get_phonenumber(), 
                               'password' : account.get_password()}).fetchone()
        self.__conn.commit()
        self.readAccount(account.getID())


    def deleteAccount(self, account_id : int):
        # global self.__conn, self.__cursor
        self.__cursor.execute("DELETE FROM Account WHERE (account_id) = (:ID)", {
            'ID' : account_id
        })
        self.__conn.commit()

# #create Account
# user1 = Account(first="Ali",last="Maamoun", username="amaamoun")
# user2 = Account(first="Ridham",last="Patel", username="rpatel")
# user3 = Account(first="Adrian",last="careno", username="acareno")

# #execute many
# users = (
#     {'first': user1.get_firstName(), 'last': user1.get_lastName(), 'username': user1.get_username() },
#     {'first': user2.get_firstName(), 'last': user2.get_lastName(), 'username': user2.get_username() },
#     {'first': user3.get_firstName(), 'last': user3.get_lastName(), 'username': user3.get_username() },
# )

# #cursor.executemany("INSERT INTO Account (first,last,username) VALUES (:first,:last,:username)", users)

# conn.commit()

# #add acc ID to account
# print(cursor.execute("SELECT FROM ACCOUNT WHERE username=:username",{'username':user1.get_username()}))
# print(cursor.fetchone())
# user1.setID()

# #user1 adds a tenant to their db
# tenant = Tenant(firstname="Joe", lastname="Man", tenantssn="234512", tenantaddress="844 tenat st", tenantphonenumber="3425552321",tenantemail="JoeMan@PARA.com")

# #insert into DB
# cursor.execute("""INSERT INTO Tenant VALUES 
#                (:acc_ID, :first, :last, :ssn, :address, :phone, :email)""",
#                {'acc_ID' : cursor.execute("SELECT FROM account WHERE acc_ID=:ID", {'ID':user1.ID})})

# #Example 1
# # cursor.execute("INSERT INTO account VALUES (?, ?, ?)", 
# #                (user1.getID(), user1.get_name(), user1.get_username()))

# # example 2 (better using dictionaries)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
# # cursor.execute("""INSERT INTO account VALUES (:first,:username)""", {'first' : user1.get_name(), 'username' : user1.get_username()})
# # cursor.execute("""INSERT INTO account VALUES (:first,:username)""", {'first' : user2.get_name(), 'username' : user2.get_username()})
# # cursor.execute("""INSERT INTO account VALUES (:first,:username)""", {'first' : user3.get_name(), 'username' : user3.get_username()})

# conn.commit()

# cursor.execute("""SELECT * FROM account WHERE first=? """, ('Ali',))

# print(cursor.fetchall())


# cursor.execute("""SELECT * FROM account WHERE username=:username """, {'username': 'rpatel'})


# #fetches the selected items and prints as a list 
# print(cursor.fetchall())

# cursor.execute("""SELECT * FROM account WHERE username= :ID """, {'ID': '3'})

# conn.close()

# #res = cursor.execute("SELECT name FROM sqlite_master")