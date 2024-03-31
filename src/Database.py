import sqlite3
# from Account import Account
# from Tenant import Tenant
from System import Account, Tenant, Property

__conn : sqlite3.Connection = None
__cursor : sqlite3.Cursor = None

def init():
    global __conn, __cursor
    __conn = sqlite3.connect('data/sql.db')
    __cursor = __conn.cursor()

def closeConnection():
    global __conn, __cursor
    if __conn is not None:
        __conn.close()
        __conn = None
        __cursor = None

def cleartables():
    global __conn, __cursor
    #Delete Table each time run for testing purposes
    __cursor.execute("DROP TABLE IF EXISTS Account")
    __cursor.execute("DROP TABLE IF EXISTS Tenant")
    __cursor.execute("DROP TABLE IF EXISTS Property")

def createTables():
    global __conn, __cursor
        #create Table for Accounts
    __cursor.execute("""CREATE TABLE Account(  
                    acc_ID integer PRIMARY KEY,
                    first text,
                    last text,
                    username text
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
                    property_ID integer NOT NULL PRIMARY KEY AUTOINCREMENT,
                    Ten_ID integer,
                    acc_ID integer,
                    address text
                   )""")
    
def readTables():
    pass

#need to understand how account creation will work with front end. What are the minimum values needed to create an account?
#name,username,password?
def addToAccounts(account : Account):
    global __conn, __cursor
    #TODO: -validation on existing username
    #
    __cursor.execute("INSERT INTO Account (first,last,username) VALUES (:first,:last,:username)", 
                    {   
                        'first' : account.get_firstName(),
                        'last': account.get_lastName(),
                        'username': account.get_username()
                    })
    __conn.commit()

    #return the KEY ID
    return __cursor.lastrowid


def addToTenants(account : Account, tenant : Tenant):
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

    return __cursor.lastrowid

#Returns the ID of Property : need to set object propID to this return value
# def addToProperty(account : Account, tenant : Tenant, property : Property):
#     global __conn, __cursor

#     __cursor.execute("INSERT INTO Property (ten_ID, acc_ID, address) VALUES (:acc_ID, :first, :last, :ssn, :address, :phone, :email)",
#                      {
#                          'ten_ID' : tenant.getID(),
#                          'acc_ID' : account.getID(),
#                          'address' : property.getAddress()
#                      }
#                      )
    
#     __conn.commit()

#     return __cursor.lastrowid   

def editAccount(account : Account):
    pass

def editTenant(tenant : Tenant):
    pass

#Reads the database and returns an object of the account
def readAccount(accID) -> Account:
    global __conn, __cursor

    data=__cursor.execute("SELECT * FROM ACCOUNT WHERE (acc_ID) = (:acc_ID)",{
        'acc_ID' : accID
    }).fetchone() 
    print(f"Data: {data}")
    account = Account(first=data[1],last=data[2],username=data[3])
    account.setID(data[0])
    
    return account

def readTenants(accID,tenID=None) -> Tenant:
    global __conn, __cursor
    tenants:dict = {}
    data=__cursor.execute("SELECT * FROM Tenant WHERE (acc_ID) = (:acc_ID)",{
        'acc_ID' : accID
    }).fetchall() #returns a list of tenant data, need to turn into Tenant Objects Dict
    if data is None:
        print(f"No data was returned from request on read Tenants on Account Number {accID}")
        return None
    print(f"Data: {data}")
    for tenData in data:
        tenant = Tenant(firstname=tenData[1],lastname=tenData[2])
        tenant.setID(tenData[0])
        print(f"tenant {tenData[0]}, {tenant}")
        tenants[tenData[0]] = tenant

    return tenants