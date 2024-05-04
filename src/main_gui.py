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
from src.Entities.Property import Property


def run():
    """Represents the driver function to run the entire application
    """
    
    app = QApplication(sys.argv)

    session = System()
    

    #launch Login GUI
    loginWindow = Login_Page(session.cont_login)

    mainacc = session.getMainAccount()
    print(f"mainaccount: {mainacc}")
    # db.addToTenants(1,Tenant(firstname="Adrian", lastname="Carreno"))
    # db.addToTenants(2,Tenant(firstname="Ridham", lastname="Patel"))
    # db.addToTenants(1,Tenant(firstname="Ali", lastname="Maamoun"))
    # db.addToTenants(1,Tenant(firstname="Patrick", lastname="P"))
    
    print("login app exec")
    app.exec()

    if(loginWindow.is_login):
        session.setControllerUserProfile()
        # db.addToProperty(session.getMainAccount().getID(),Property(address="123 main st"))
        window = Dashboard(session.cont_userprofile,session.cont_tenant, session.cont_property, session.cont_contractor, session.cont_bill)

        window.show()

        app.exec()
    


run()