"""
File: main_gui.py
Date: 04/23/2024
main_gui serves as the main for the entire application
In order to run the application, developers must run it through main_gui.py
"""

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from Dashboard_Page import Dashboard
from Login_Page import Login_Page
from System import System, db

from src.Entities.Account import Account
from src.Entities.Tenant import Tenant


def run():
    """Represents the driver function to run the entire application
    """
    
    app = QApplication(sys.argv)

    session = System()
    

    #launch Login GUI
    loginWindow = Login_Page(session.cont_login)

    mainacc = session.getMainAccount()
    app.exec()

    if(loginWindow.is_login):
        session.setControllerUserProfile()
        
        window = Dashboard(session.cont_userprofile,session.cont_tenant, session.cont_contractor)

        window.show()

        app.exec()
    


run()