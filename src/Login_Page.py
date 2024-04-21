"""
File: Login_Page.py
Name: Jittapatana (Patrick) Prayoonpruk
Date: 04/15/2024
Description: Login page user interface
Purposes: To provide the users to log in to their accounts
"""
from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication
)

import sys

from src.gui.Login_Page_GUI.pyqt_Login_Page import Ui_Form
from src.gui.Login_Page_GUI.Signup_Page import SignUp_Page
from src.Dashboard_Page import Dashboard

from src.Cont_Login import Cont_Login

class Login_Page(QMainWindow, Ui_Form):
    """Represents the login page for user authentication

    Args:
        QMainWindow (QMainWindow): The base class for the main window of the application.
        Ui_Form (Ui_Form): The user interface form with the assist of Qt Designer.
    """
    def __init__(self, cont_login: Cont_Login):
        """Initialize the Login_Page instance

        Args:
            cont_login (Cont_Login): An instance of the Cont_Login class responsible for account management.
        """
        super().__init__()
        self.setupUi(self)
        self.show()

        self.is_login = False

        #setup controller
        self.cont_login = cont_login

        # login_btn_2 = sign up button
        self.login_btn_2.clicked.connect(self.go_to_signup_page)

        # login_btn = log in button
        self.login_btn.clicked.connect(self.log_in)

    def go_to_signup_page(self):
        """Navigate to the sign-up page for new user registration.
        """
        self.signup_page = SignUp_Page(self.cont_login)
        self.signup_page.show()

    def log_in(self):
        """Process the log in action.

        check for user validation whether the log in is successful or not
        """
        temp_username = self.username_line_edit.text()
        temp_password = self.password_line_edit.text()
        
        if self.cont_login.validateLogin(temp_username,temp_password):
            print("log in success")
            self.close()
            self.is_login = True
        else:
            print("not match")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Login_Page = Login_Page()
    Login_Page.show()
    sys.exit(app.exec())