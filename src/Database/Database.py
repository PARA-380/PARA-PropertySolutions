""" Module Name: Database
    Date: 02/14/2024 - 4/21/2024
    Name: Ali Maamoun
    A static file which makes calls to a single database file 
    regarding a number of Tables important to the project.
    Uses sqlite3 to manage sql code in python. Purpose is to 
    make dealing with database as easy as Database.addtoTenants(TenantObj)

"""
import sqlite3
# from Account import Account
# from Tenant import Tenant
from System import Account, Tenant, Property, Contractor, Bill

__conn : sqlite3.Connection = None
__cursor : sqlite3.Cursor = None


def init():
    """Starts up the Database and provides the connection and the cursor, which are crucial to executing.
       __cursor : is responsible for executing sql commands
       __conn   : is the current connection to a certain database file. (stored locally)
    """
    global __conn, __cursor
    #__conn = sqlite3.connect('../data/sql.db')
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
    __cursor.execute("DROP TABLE IF EXISTS Bill")
    print("Dropped Tables")

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
                    max_living int,
                    link_images text
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
    print("Created Contractor Table")

    # create Table for Bills
    __cursor.execute("""CREATE TABLE Bill(
                    bill_ID INTEGER PRIMARY KEY,
                    acc_ID integer,
                    prop_ID integer,
                    amount int,
                    type text,
                    description text
                   )""")
    
    print("Created Bill table")
    __conn.commit()
    
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


def addToTenants(accID : int, tenant : Tenant):
    """Inserts into Tenant Table a tenant associated to an account

    Args:
        account (Account): object of the account we want to add a tenant to
        tenant (Tenant): object of the tenant we are adding to the account

    Returns:
        _type_: Returns the ID associated to the Tenant. Must be set to Tenant Object
    """
    global __conn, __cursor

    __cursor.execute("INSERT INTO Tenant (acc_ID, prop_ID, first, last, ssn, address, phone, email) VALUES (:acc_ID,:prop_ID, :first, :last, :ssn, :address, :phone, :email)",
                     {
                         'acc_ID' : accID,
                         'prop_ID' : tenant.get_property_id(),
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

def addToProperty(accID : int, property : Property):
    """Adds a new Property Object into the Database by copying its contents and linking its IDs to other tables
    Args:
        accID (int): The account associated with this property
        property (Property): Property Object to copy contents from

    Returns:
        _type_: Returns the Unique ID in that table.
    """
    global __conn, __cursor

    __cursor.execute("INSERT INTO Property (acc_ID, address, link_images) VALUES (:acc_ID, :address, :link_images)",
                     {
                         'acc_ID' : accID,
                         'address' : property.get_address(),
                         'link_images' : property.get_link_images()
                     }
                     )
    
    __conn.commit()
    property.set_property_id(__cursor.lastrowid)

    return __cursor.lastrowid   


def addToBill(accID : int, bill : Bill):
    global __conn, __cursor

    __cursor.execute("INSERT INTO Bill (acc_ID, prop_ID, amount, type, description) VALUES (:acc_ID, :prop_ID, :amount, :type, :description)",
                     {
                         'acc_ID' : accID,
                         'prop_ID' : bill.get_propID(),
                         'amount' : bill.getAmount(),
                         'type' : bill.get_type(),
                         'description' : bill.getDescription()
                     }
                     )
    
    __conn.commit()
    bill.set_bill_id(__cursor.lastrowid)

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




def readTenants(accID:int) -> list[Tenant]:
    """Read DataBase Tenant Table

    Args:
        accID (int): Key of the Account to lookup tenants

    Returns:
        Tenants: A Dictionary of Tenant objects based on KEY ID : Tenant pairs
    """
    global __conn, __cursor
    #temporary dictionary to return list of tenant objects
    tenants = list()
    #use cursor to execute SELECT sql code. fetchall fields returned from condition for tenants associated with account id
    data=__cursor.execute("SELECT * FROM Tenant WHERE (acc_ID) = (:acc_ID)",{
        'acc_ID' : accID
    }).fetchall() #returns a list of tenant data, need to turn into Tenant Objects Dict
    #if data is None, then there was no tenants with associated account id
    if data is None:
        print(f"No data was returned from request on read Tenants on Account Number {accID}")
        return None
    print(f"Read Tenants Data: {data}")

    #parse through tenant data and create tenant objects
    for tenData in data:
        tenant = Tenant(acc_id=tenData[1],prop_id=tenData[2],firstname=tenData[3],lastname=tenData[4],ssn=tenData[5],address=tenData[6],phonenumber=tenData[7],email=tenData[8])
        #use DB generated Key as Tenants' ID
        tenant.setID(tenData[0])
        # print(f"tenant {tenData[0]}, {tenant}")
        #
        tenants.append(tenant) 
    #return list of tenants associated to accID account
    # print(f"tenants: {tenants}")
    return tenants

def readProperty(accID:int) -> list[Property]:
    global __conn, __cursor
    properties = list()
    data = __cursor.execute("SELECT * FROM Property WHERE (acc_ID) = (:acc_ID)",{
        'acc_ID' : accID
    }).fetchall()
    if data is None:
        print(f"No data was returned from request on read Properties on Account Number {accID}")
        return None
    print(f"Data: {data}")

    for propData in data:
        temp_property = Property(accID=accID,address=propData[2],link_images=propData[6])
        temp_property.set_property_id(propData[0])
        properties.append(temp_property)

    return properties



def readBills(propID:int) -> dict[int,Bill]:
    global __conn, __cursor
    #temporary dictionary to return list of tenant objects
    bills = {}
    #use cursor to execute SELECT sql code. fetchall fields returned from condition for tenants associated with account id
    data=__cursor.execute("SELECT * FROM Bill WHERE (prop_ID) = (:prop_ID)",{
        'prop_ID' : propID
    }).fetchall() #returns a list of tenant data, need to turn into Tenant Objects Dict
    #if data is None, then there was no tenants with associated account id
    if data is None:
        print(f"No data was returned from request on read Bills on property {propID}")
        return None
    print(f"Read Bills Data: {data}")

    #parse through bill data and create bill objects
    for billData in data:
        bill = Bill(account_id=billData[1], property_ID=billData[2], amount= billData[3], bill_type=billData[4], description=billData[5] )
        bill.set_bill_id(billData[0])
        bills[bill.get_bill_id()] = bill 
        print(f"{bill}")

    return bills

# def readBills_Account(accID:int) -> dict[int,dict[int,Bill]]:
#     global __conn, __cursor
#     #temporary dictionary to return list of tenant objects
#     bills = dict[int,dict[int,Bill]] #[[prop_id] -> [bill_id -> bill]]
#     #use cursor to execute SELECT sql code. fetchall fields returned from condition for tenants associated with account id
#     data=__cursor.execute("SELECT * FROM Bill WHERE (acc_ID) = (:acc_ID)",{
#         'acc_ID' : accID
#     }).fetchall() #returns a list of tenant data, need to turn into Tenant Objects Dict
#     #if data is None, then there was no tenants with associated account id
#     if data is None:
#         print(f"No data was returned from request on read Bills from account {accID}")
#         return None
#     print(f"Read Bills Data: {data}")

#     #parse through bill data and create bill objects
#     property_bills = dict[int,Bill]
    
#     for billData in data:
#         bill = Bill()
#         bill.set_bill_id(billData[0])
#         property_bills[billData[0]] = bill
        
#         bills[bill.get_bill_id()] = bill 
#         bills[billData[2]] = property_bills[billData[0]]

#     return bills



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

def updateTenant(tenant :Tenant):
    """Updates a selected Tenant by ID

    Args:
        tenant (Tenant): tenant to update
    """
    global __conn, __cursor
    __cursor.execute("UPDATE Tenant SET (prop_ID, first,last,ssn,address,phone,email) = (:prop_ID, :first, :last, :ssn, :address, :phone, :email) WHERE (ten_ID) = (:ten_ID)",
                     {'prop_ID' : tenant.get_property_id(),'first': tenant.getFirstName(), 'last' : tenant.getLastName(), 'ssn' : tenant.getSSN(), 'address' : tenant.getAddress(), 'phone' : tenant.getPhoneNumber(), 'email' : tenant.getEmail(), 'ten_ID' : tenant.getID()})
    __conn.commit()

def updateProperty(property : Property):
    """updates a selected Property by ID

    Args:
        property (Property): property to update
    """
    global __conn, __cursor
    __cursor.execute(
        "UPDATE Property SET (acc_ID, address, link_images) = (:acc_ID, :address, :link_images) WHERE (prop_ID) = (:prop_ID)",
        {'acc_ID': property.get_account_id(), 'prop_ID': property.get_property_id(), 'address': property.get_address(), 'link_images': property.get_link_images()})
    __conn.commit()

def updateBill(bill : Bill):
    global __conn, __cursor
    __cursor.execute(
        "UPDATE Bill SET (acc_ID, prop_ID, type, amount) = (:acc_ID, :prop_id, :type, :amount) WHERE (bill_ID) = (:bill_ID)",
        {'acc_ID': bill.get_acc_id(), 'prop_ID': bill.get_propID(), 'type': bill.get_type(), 'amount' : bill.getAmount()})
    __conn.commit()


#DELETE METHODS

def deleteTenant(ten_id : int):
    """Removes a Tenant Row from the Tenant Table in Database by searching by Unique ID.

    Args:
        ten_id (int): The Unique ID to search for.
    """
    global __conn, __cursor
    __cursor.execute("DELETE FROM Tenant WHERE (Ten_id) = (:ID)", {
        'ID' : ten_id
    })
    __conn.commit()


def readContractors(accID: int) -> list[Contractor]:
    """Reads the Contractor Table from the Database and returns a list of Contractor objects.

    Returns:
        list[Contractor]: List of Contractor objects.
    """
    global __conn, __cursor
    contractors = list()

    data = __cursor.execute("SELECT * FROM Contractor WHERE (acc_ID) = (:acc_ID)",{
        'acc_ID' : accID
    }).fetchall()

    if data is None:
        print(f"No data was returned from request on read Contractors on Account Number {accID}")
        return None

    for contractor_data in data:
        contractor = Contractor(
            accID=contractor_data[1],
            specialization=contractor_data[2],
            firstname=contractor_data[3],
            lastname=contractor_data[4],
            phonenumber=contractor_data[5]
        )
        contractor.set_id(contractor_data[0])
        contractors.append(contractor)

    return contractors

def addToContractors(accID: int, contractor : Contractor):
    """Adds a contractor to contractor table assigning it to an account at the same time.

    Args:
        accID (int): account which added a contractor
        contractor (Contractor): _description_

    Returns:
        _type_: _description_
    """
    global __conn, __cursor

    __cursor.execute("INSERT INTO Contractor (acc_ID, specialization, first, last, phone) VALUES (:acc_ID, :specialization, :first, :last, :phone)",
                     {
                         'acc_ID' : accID,
                         'specialization' : contractor.get_specialization(),
                         'first' : contractor.get_first_name(),
                         'last' : contractor.get_last_name(),
                         'phone' : contractor.get_phone_number()
                     })
    
    __conn.commit()
    contractor.set_id(__cursor.lastrowid)
    return __cursor.lastrowid

def deleteContractor(contractor_id : int):
    """Deletes a contractor from the table

    Args:
        contractor_id (int): ID to search for and delete contractor associated to it
    """
    global __conn, __cursor
    __cursor.execute("DELETE FROM Contractor WHERE (contractor_id) = (:ID)", {
        'ID' : contractor_id
    })
    __conn.commit()
    
def deleteProperty(prop_id : int):
    """Deletes a Property from the property table

    Args:
        prop_id (int): ID to search for and delete property associated to it.
    """
    global __conn, __cursor
    __cursor.execute("DELETE FROM Property WHERE (prop_id) = (:ID)", {
        'ID' : prop_id
    })
    __conn.commit()

def deleteBill(bill_id : int):
    global __conn, __cursor
    __cursor.execute("DELETE FROM Bill WHERE (bill_id) = (:ID)", {
        'ID' : bill_id
    })
    __conn.commit()

def main():
    addToProperty(1,Property(accID=1))

if __name__ == "__main__":
    main()
