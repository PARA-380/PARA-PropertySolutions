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
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        #setup controller
        self.cont_login = Cont_Login()

        # login_btn_2 = sign up button
        self.login_btn_2.clicked.connect(self.go_to_signup_page)

        # login_btn = log in button
        self.login_btn.clicked.connect(self.log_in)

    def go_to_signup_page(self):
        self.signup_page = SignUp_Page()
        self.signup_page.show()

    def log_in(self):
        # Add is sign in success def here to check
        print("login in")
        print(self.username_line_edit.text())
        print(self.password_line_edit.text())
        temp_username = self.username_line_edit.text()
        temp_password = self.password_line_edit.text()
        
        if self.cont_login.validateLogin(temp_username,temp_password):
            print(f' print if {self.cont_login.validateLogin(temp_username,temp_password)}')
            print("log in success")
            self.close()
            # self.hide()
            # dashboard = Dashboard()
            # dashboard.show()
        else:
            print("not match")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Login_Page = Login_Page()
    Login_Page.show()
    sys.exit(app.exec())