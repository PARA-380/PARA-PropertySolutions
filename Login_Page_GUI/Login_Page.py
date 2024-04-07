from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication
)

import sys

from pyqt_Login_Page import Ui_Form

class Login_Page(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Login_Page = Login_Page()
    Login_Page.show()
    sys.exit(app.exec())