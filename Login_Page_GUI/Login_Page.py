from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication
)

import sys

from pyqt_Login_Page import Ui_Form
from Signup_Page import SignUp_Page

class Login_Page(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        # login_btn_2 = sign up button
        self.login_btn_2.clicked.connect(self.go_to_signup_page)

    def go_to_signup_page(self):
        self.signup_page = SignUp_Page()
        self.signup_page.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Login_Page = Login_Page()
    Login_Page.show()
    sys.exit(app.exec())