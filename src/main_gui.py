from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from Dashboard_Page import Dashboard
from Login_Page import Login_Page
from System import System, db

from src.Entities.Account import Account



def run():
    
    app = QApplication(sys.argv)
    print("***********************************")


    # session = System(Account(first="Ridham", last="Petal", username="123", password="4560"))
    session = System()
    print("db call at run")
    db.addToAccounts(Account(first="Ridham", last="Petal", username="123", password="4560"))
    #launch Login GUI
    loginWindow = Login_Page(session.cont_login)
    print("login app exec")
    app.exec()

    if(loginWindow.is_login):
        session.setControllerUserProfile()
        
        window = Dashboard(session.cont_userprofile)

        window.show()

        app.exec()
    


run()