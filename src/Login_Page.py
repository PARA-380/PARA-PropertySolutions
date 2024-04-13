from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication
)

import sys

from src.gui.Login_Page_GUI.pyqt_Login_Page import Ui_Form
from src.gui.Login_Page_GUI.Signup_Page import SignUp_Page
from src.Dashboard_Page import Dashboard

class Login_Page(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

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
        if self.username_line_edit.text() == "1" and self.password_line_edit.text() == "2":
            print("log in success")
            self.hide()
            dashboard = Dashboard()
            dashboard.show()
    
    def get_username(self):
        return self.username_line_edit.text()
    
    def get_password(self):
        return self.password_line_edit.text()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Login_Page = Login_Page()
    Login_Page.show()
    sys.exit(app.exec())