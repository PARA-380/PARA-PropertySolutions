from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from Dashboard_Page import Dashboard
from Login_Page import Login_Page
from System import System, db

from src.Entities.Account import Account
from src.Entities.Tenant import Tenant



def run():
    
    app = QApplication(sys.argv)

    session = System()
    

    #launch Login GUI
    loginWindow = Login_Page(session.cont_login)

    mainacc = session.getMainAccount()
    app.exec()

    if(loginWindow.is_login):
        session.setControllerUserProfile()
        
        window = Dashboard(session.cont_userprofile,session.cont_tenant)

        window.show()

        app.exec()
    


run()