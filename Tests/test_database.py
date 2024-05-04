import pytest
import unittest
from DatabaseTest import DatabaseTest

from src.Entities.Account import Account

assert 1==1

# class Testing_Database(unittest.TestCase):
#     """Testing the database mock file
#         Will test the Account Operations
#     """
global db 
db = DatabaseTest()

def startup_db():
    db.init()

def test_update_account():
    """If update account is valid, then we expect the values given should match the contents of the database
    """
    #assume init works
    # db.init()
    #make sure database is empty for testing purposes
    db.cleartables()
    #assume creating tables works (creates Account table)
    db.createTables()
    #now create the Account and add it to the Table
    user1 = Account(first="Ali",last="Maamoun", username="amaamoun", password="secretpassword", phone=1233413080)
    db.addToAccounts(user1) #returns back the same account object. it should have been assigned an account ID
    #make edits to user1
    user1.set_firstName(first="Updated")
    user1.set_lastName(last="Account")
    db.updateAccount(user1)
    #assume reading account by id works properly
    updated_user = db.readAccount(user1.getID())
    assert updated_user.get_firstName() == user1.get_firstName()
    #test fake account (Nonetype)
    fakeaccount = None
    assert unittest.TestCase.assertRaises(db.addToAccounts(fakeaccount),TypeError)


#create Account
def test_add_to_account():
    """When we create an account, we expect to get the same results back displayed in the database
    create account returns an id we can find the account back in the table. We can construct this into an object
    and these two objects should be identical.
    """
    #assume init works
    # db.init()
    #make sure database is empty for testing purposes
    db.cleartables()
    #assume creating tables works (creates Account table)
    db.createTables()
    #now create the Account and add it to the Table
    user1 = Account(first="Ali",last="Maamoun", username="amaamoun", password="secretpassword", phone=1233413080)
    user2 = Account(first="Ridham",last="Patel", username="rpatel", password="valorantpassword", phone=2921013322)
    user3 = Account(first="Adrian",last="careno", username="acareno", password="password", phone=3920001123)
    fakeaccount = None
    account1 = db.addToAccounts(user1) #returns back the same account object. it should have been assigned an account ID
    account2 = db.addToAccounts(user2) #returns back the same account object. it should have been assigned an account ID
    account3 = db.addToAccounts(user3) #returns back the same account object. it should have been assigned an account ID
    assert account1.getID() == 1
    assert account2.getID() == 2
    assert account3.getID() == 3
    assert unittest.TestCase.assertRaises(db.addToAccounts(fakeaccount),TypeError)
    #we need to read the table and make sure everything is the same as the account above
    #assume read account works
    read_account1 = db.readAccount(1)
    assert read_account1.get_firstName() == account1.get_firstName()
    assert read_account1.getID() == user1.getID()
    # assert read_account1 == user1



# def start_testing():
#     Testing_Database.startup_db()

# def test_add_to_account():
#     Testing_Database.test_add_to_account()


# if __name__ == "__main__":
#     start_testing()

#     test_add_to_account()
    
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
    #             (:acc_ID, :first, :last, :ssn, :address, :phone, :email)""",
    #             {'acc_ID' : cursor.execute("SELECT FROM account WHERE acc_ID=:ID", {'ID':user1.ID})})

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