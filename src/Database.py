import sqlite3
from Account import Account

__conn : sqlite3.Connection = None
__cursor : sqlite3.Cursor = None

def init():
    global __conn, __cursor
    __conn = sqlite3.connect('data/sql.db')
    __cursor = __conn.cursor()

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

    #create Table for Property 
    #address should link to property id
    # cursor.execute("""CREATE TABLE Property( 
    #                 property_ID integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    #                 Ten_ID integer,
    #                 acc_ID integer,
    #                )""")

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
