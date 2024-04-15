from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from Dashboard_Page import Dashboard
from Login_Page import Login_Page
from System import System, db

from src.Entities.Account import Account
from src.Entities.Tenant import Tenant



def run():
    
    app = QApplication(sys.argv)
    print("***********************************")


    # session = System(Account(first="Ridham", last="Petal", username="123", password="4560"))
    session = System()
    print("db call at run")
    # db.addToAccounts(Account(first="Ridham", last="Petal", username="123", password="4560"))
    

    #launch Login GUI
    loginWindow = Login_Page(session.cont_login)

    mainacc = session.getMainAccount()
    print(f"mainaccount: {mainacc}")
    db.addToTenants(1,Tenant(firstname="Adrian", lastname="Carreno"))
    db.addToTenants(2,Tenant(firstname="Ridham", lastname="Patel"))
    db.addToTenants(1,Tenant(firstname="Ali", lastname="Maamoun"))
    db.addToTenants(1,Tenant(firstname="Patrick", lastname="P"))
    print("login app exec")
    app.exec()

    if(loginWindow.is_login):
        session.setControllerUserProfile()
        
        window = Dashboard(session.cont_userprofile)

        window.show()

        app.exec()
    


run()