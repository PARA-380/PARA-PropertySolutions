import sys
import os
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from pyqt_dashboard import Ui_DashBoard
from test_page import test_page
from UserProfile import Userprofile

class Dashboard(QMainWindow, Ui_DashBoard):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.Properties_btn.clicked.connect(self.goto_property_page)
        # pushButton = userprofile page
        self.pushButton_3.clicked.connect(self.goto_user_profile_page)

    def goto_property_page(self, checked):
        self.anotherw = test_page()
        self.anotherw.show()

    def goto_user_profile_page(self, checked):
        self.user_profile = Userprofile()
        self.user_profile.show()
