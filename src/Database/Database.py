import sqlite3
# from Account import Account
# from Tenant import Tenant
from System import Account, Tenant, Property

__conn : sqlite3.Connection = None
__cursor : sqlite3.Cursor = None

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
                    first text,
                    last text,
                    ssn text,
                    address text,
                    phone text,
                    email text
                )""")

    __conn.commit()

    # create Table for Property 
    # address should link to property id
    __cursor.execute("""CREATE TABLE Property(
                    property_ID integer PRIMARY KEY AUTOINCREMENT,
                    Ten_ID integer,
                    acc_ID integer,
                    address text
                   )""")
    
def readTables():
    pass

#need to understand how account creation will work with front end. What are the minimum values needed to create an account?
#name,username,password?
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


def addToTenants(account : Account, tenant : Tenant):
    """Inserts into Tenant Table a tenant associated to an account

    Args:
        account (Account): object of the account we want to add a tenant to
        tenant (Tenant): object of the tenant we are adding to the account

    Returns:
        _type_: Returns the ID associated to the Tenant. Must be set to Tenant Object
    """
    global __conn, __cursor

    __cursor.execute("INSERT INTO Tenant (acc_ID, first, last, ssn, address, phone, email) VALUES (:acc_ID, :first, :last, :ssn, :address, :phone, :email)",
                     {
                         'acc_ID' : account.getID(),
                         'first' : tenant.getFirstName(),
                         'last' : tenant.getLastName(),
                         'ssn' : tenant.getSSN(),
                         'address' : tenant.getAddress(),
                         'phone' : tenant.getPhoneNumber(),
                         'email' : tenant.getEmail(),
                     }
                     )
    
    __conn.commit()
    tenant.setID(__cursor.lastrowid)
    return __cursor.lastrowid

#Returns the ID of Property : need to set object propID to this return value
def addToProperty(accID : int , tenID : int, property : Property):

    global __conn, __cursor

    __cursor.execute("INSERT INTO Property (ten_ID, acc_ID, address) VALUES (:acc_ID, :ten_ID, :address)",
                     {
                         'ten_ID' : tenID,
                         'acc_ID' : accID,
                         'address' : property.getAddress()
                     }
                     )
    
    __conn.commit()

    return __cursor.lastrowid   

def editAccount(account : Account):
    pass

def editTenant(tenant : Tenant):
    pass

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
    print(f"Data: {data}")
    account = Account(first=data[1],last=data[2],username=data[3],phone=data[4],password=data[5])
    account.setID(data[0])
    
    return account

def searchAccount(username : str) -> list[Account]:
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
    print(f'type: {type(users)}, user: {users}')
    return users




def readTenants(accID:int) -> Tenant:
    """Read DataBase Tenant Table

    Args:
        accID (int): Key of the Account to lookup tenants

    Returns:
        Tenants: A Dictionary of Tenant objects based on KEY ID : Tenant pairs
    """
    global __conn, __cursor
    #temporary dictionary to return list of tenant objects
    tenants:dict = {}
    #use cursor to execute SELECT sql code. fetchall fields returned from condition for tenants associated with account id
    data=__cursor.execute("SELECT * FROM Tenant WHERE (acc_ID) = (:acc_ID)",{
        'acc_ID' : accID
    }).fetchall() #returns a list of tenant data, need to turn into Tenant Objects Dict
    #if data is None, then there was no tenants with associated account id
    if data is None:
        print(f"No data was returned from request on read Tenants on Account Number {accID}")
        return None
    print(f"Data: {data}")

    #parse through tenant data and create tenant objects
    for tenData in data:
        tenant = Tenant(firstname=tenData[1],lastname=tenData[2],address=tenData[5])
        #use DB generated Key as Tenants' ID
        tenant.setID(tenData[0])
        print(f"tenant {tenData[0]}, {tenant}")
        #dictionary key to tenant pair value. 'tenID' : "tenantObject"
        tenants[tenData[0]] = tenant
    #return list of tenants associated to accID account
    return tenants


#UPDATE METHODS

def updateAccount(account : Account):
    global __conn, __cursor
    __cursor.execute("UPDATE Account SET (first,last,username,phonenumber,password) = (:first, :last, :username,:phone, :password) WHERE (acc_ID) = (:acc_ID)",{'first': account.get_firstName(), 'last' : account.get_lastName(), 'username' : account.get_username(), 'acc_ID' : account.getID(),'phone':account.get_phonenumber(), 'password' : account.get_password()}).fetchone()
    __conn.commit()
    readAccount(account.getID())