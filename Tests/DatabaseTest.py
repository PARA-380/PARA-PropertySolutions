import sqlite3
from Account import Account
from Tenant import Tenant

conn = sqlite3.connect('data/sql.db')

cursor = conn.cursor()

#Delete Table each time run for testing purposes
cursor.execute("DROP TABLE IF EXISTS Account")
cursor.execute("DROP TABLE IF EXISTS Tenant")
cursor.execute("DROP TABLE IF EXISTS Property")


#create Table for Accounts
cursor.execute("""CREATE TABLE Account(  
                acc_ID integer PRIMARY KEY,
                first text,
                last text,
                username text
               )""")

#create Table for Tenants 
#address should link to property id
cursor.execute("""CREATE TABLE Tenant(  
                Ten_ID integer NOT NULL PRIMARY KEY AUTOINCREMENT,
                acc_ID integer,
                first text,
                last text,
                ssn text,
                address text,
                phone text,
                email text
               )""")

conn.commit()

#create Table for Property 
#address should link to property id
# cursor.execute("""CREATE TABLE Property( 
#                 property_ID integer NOT NULL PRIMARY KEY AUTOINCREMENT,
#                 Ten_ID integer,
#                 acc_ID integer,
#                )""")

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