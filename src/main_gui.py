from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from Dashboard_Page import Dashboard
from Login_Page import Login_Page
from System import System

from src.Entities.Account import Account

def run():
    app = QApplication(sys.argv)
    print("***********************************")
    
    # session = System(Account(first="Ridham", last="Petal", username="123", password="4560"))
    session = System()
    #launch Login GUI
    loginWindow = Login_Page()
    
    app.exec()

    session.setControllerUserProfile()
    
    window = Dashboard(session.cont_userprofile)

    window.show()

    app.exec()



run()