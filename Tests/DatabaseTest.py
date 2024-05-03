import sqlite3
import pytest
from src.Entities.Account import Account
from src.Entities.Tenant import Tenant

def init():
    """Starts up the Database and provides the connection and the cursor, which are crucial to executing.
       __cursor : is responsible for executing sql commands
       __conn   : is the current connection to a certain database file. (stored locally)
    """
    global __conn, __cursor
    # __conn = sqlite3.connect('../data/sql.db')
    __conn = sqlite3.connect('data/sql.db')
    __cursor = __conn.cursor()

def closeConnection():
    """Closes connection to the Database
    """
    global __conn, __cursor
    if __conn is not None:
        __conn.close()
        __conn = None
        __cursor = None

def cleartables():
    """Clears all Database Tables for Testing purposes
    """
    global __conn, __cursor
    #Delete Table each time run for testing purposes
    __cursor.execute("DROP TABLE IF EXISTS Account")
    __cursor.execute("DROP TABLE IF EXISTS Tenant")
    __cursor.execute("DROP TABLE IF EXISTS Property")
    __cursor.execute("DROP TABLE IF EXISTS Contractor")



def createTables():
    """Creates All Tables needed for initializing the Database
    """    
    global __conn, __cursor
        #create Table for Accounts
    __cursor.execute("""CREATE TABLE Account(  
                    acc_ID integer PRIMARY KEY,
                    first text,
                    last text,
                    username text,
                    phonenumber text,
                    password text
                )""")

    #create Table for Tenants 
    #address should link to property id
    __cursor.execute("""CREATE TABLE Tenant(  
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
    __cursor.execute("""CREATE TABLE Property(
                    prop_ID integer PRIMARY KEY AUTOINCREMENT,
                    acc_ID integer,
                    address text,
                    sqft int,
                    hometype text,
                    max_living int
                   )""")
    
    # create Table for Contractors
    __cursor.execute("""CREATE TABLE Contractor(
                    contractor_ID integer PRIMARY KEY AUTOINCREMENT,
                    acc_ID integer,
                    specialization text,
                    first text,
                    last text,
                    phone text
                   )""")
    
    __conn.commit()


def addToAccounts(account : Account):
    """Creates new row in Account Table and returns the KEY generated

    Args:
        account (Account): Account Object

    Returns:
        _type_: KEY id generated
    """
    global __conn, __cursor
    #TODO: -validation on existing username
    #
    __cursor.execute("INSERT INTO Account (first,last,username,phonenumber,password) VALUES (:first,:last,:username,:phonenumber, :password)",
                    {   
                        'first' : account.get_firstName(),
                        'last': account.get_lastName(),
                        'username': account.get_username(),
                        'phonenumber' : account.get_phonenumber(),
                        'password' : account.get_password()

                    })
    __conn.commit()
    account.setID(__cursor.lastrowid)

    #return the KEY ID
    #NOTICE: CHANGED to account FROM __cursor.lastrowid
    return account


#Reads the database and returns an object of the account
def readAccount(accID: int) -> Account:
    """Reads the Database Account Table and returns the row associated with an Account ID

    Args:
        accID (int): The Account ID to lookup as the KEY

    Returns:
        Account: an Account object with the data recieved from Database
    """
    global __conn, __cursor

    data=__cursor.execute("SELECT * FROM ACCOUNT WHERE (acc_ID) = (:acc_ID)",{
        'acc_ID' : accID
    }).fetchone()
    account = Account(first=data[1],last=data[2],username=data[3],phone=data[4],password=data[5])
    account.setID(data[0])
    
    return account


def searchAccount(username : str) -> list[Account]:
    """Searches the accounts based on matching usernames

    Args:
        username (str): Username to search for

    Returns:
        list[Account]: List of matching Account objects.
    """
    global __conn, __cursor
    users = list()
    data=__cursor.execute("SELECT * FROM ACCOUNT WHERE (username) = (:username)",{
        'username' : username
    }).fetchall() 
    
    for user in data:
        # users.append(Account(first=user[1],last=user[2],username=user[3],phone=user[4],password=user[5]).setID(user[0]))
        acc = Account(first=user[1],last=user[2],username=user[3],phone=user[4],password=user[5])
        acc.setID(user[0])
        users.append(acc)
    return users


#UPDATE METHODS

def updateAccount(account : Account):
    """Updates the Account in the Database. Copies all its contents into exisitng Account Entry in table

    Args:
        account (Account): Account to copy
    """
    global __conn, __cursor
    __cursor.execute("UPDATE Account SET (first,last,username,phonenumber,password) = (:first, :last, :username,:phone, :password) WHERE (acc_ID) = (:acc_ID)",{'first': account.get_firstName(), 'last' : account.get_lastName(), 'username' : account.get_username(), 'acc_ID' : account.getID(),'phone':account.get_phonenumber(), 'password' : account.get_password()}).fetchone()
    __conn.commit()
    readAccount(account.getID())


def deleteAccount(account_id : int):
    global __conn, __cursor
    __cursor.execute("DELETE FROM Account WHERE (account_id) = (:ID)", {
        'ID' : account_id
    })
    __conn.commit()

#create Account
user1 = Account(first="Ali",last="Maamoun", username="amaamoun")
user2 = Account(first="Ridham",last="Patel", username="rpatel")
user3 = Account(first="Adrian",last="careno", username="acareno")

#execute many
users = (
    {'first': user1.get_firstName(), 'last': user1.get_lastName(), 'username': user1.get_username() },
    {'first': user2.get_firstName(), 'last': user2.get_lastName(), 'username': user2.get_username() },
    {'first': user3.get_firstName(), 'last': user3.get_lastName(), 'username': user3.get_username() },
)

#cursor.executemany("INSERT INTO Account (first,last,username) VALUES (:first,:last,:username)", users)

conn.commit()

#add acc ID to account
print(cursor.execute("SELECT FROM ACCOUNT WHERE username=:username",{'username':user1.get_username()}))
print(cursor.fetchone())
user1.setID()

#user1 adds a tenant to their db
tenant = Tenant(firstname="Joe", lastname="Man", tenantssn="234512", tenantaddress="844 tenat st", tenantphonenumber="3425552321",tenantemail="JoeMan@PARA.com")

#insert into DB
cursor.execute("""INSERT INTO Tenant VALUES 
               (:acc_ID, :first, :last, :ssn, :address, :phone, :email)""",
               {'acc_ID' : cursor.execute("SELECT FROM account WHERE acc_ID=:ID", {'ID':user1.ID})})

#Example 1
# cursor.execute("INSERT INTO account VALUES (?, ?, ?)", 
#                (user1.getID(), user1.get_name(), user1.get_username()))

# example 2 (better using dictionaries)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
# cursor.execute("""INSERT INTO account VALUES (:first,:username)""", {'first' : user1.get_name(), 'username' : user1.get_username()})
# cursor.execute("""INSERT INTO account VALUES (:first,:username)""", {'first' : user2.get_name(), 'username' : user2.get_username()})
# cursor.execute("""INSERT INTO account VALUES (:first,:username)""", {'first' : user3.get_name(), 'username' : user3.get_username()})

conn.commit()

cursor.execute("""SELECT * FROM account WHERE first=? """, ('Ali',))

print(cursor.fetchall())


cursor.execute("""SELECT * FROM account WHERE username=:username """, {'username': 'rpatel'})


#fetches the selected items and prints as a list 
print(cursor.fetchall())

cursor.execute("""SELECT * FROM account WHERE username= :ID """, {'ID': '3'})

conn.close()

#res = cursor.execute("SELECT name FROM sqlite_master")