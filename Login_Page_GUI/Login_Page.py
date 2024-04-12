from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication
)

import sys

from Login_Page_GUI.pyqt_Login_Page import Ui_Form
from Login_Page_GUI.Signup_Page import SignUp_Page

class Login_Page(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # login_btn_2 = sign up button
        self.login_btn_2.clicked.connect(self.go_to_signup_page)

        # login_btn = sign in button
        self.login_btn.clicked.connect(self.sing_in)

    def go_to_signup_page(self):
        self.signup_page = SignUp_Page()
        self.signup_page.show()

    def sing_in(self):
        # Add is sign in success def here to check
        self.close()
        print(self.username_line_edit.text())
        print(self.password_line_edit.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Login_Page = Login_Page()
    Login_Page.show()
    sys.exit(app.exec())