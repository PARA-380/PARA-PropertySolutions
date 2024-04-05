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


from gui.pyqt_dashboard import Ui_DashBoard
from gui.UserProfile import Userprofile
from Property_GUI.Property_main import Property_Page
from Setting_GUI.Setting_Page_GUI import Setting_Page


class Dashboard(QMainWindow, Ui_DashBoard):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.Properties_btn.clicked.connect(self.goto_property_page)
        # pushButton = userprofile page
        self.pushButton_3.clicked.connect(self.goto_user_profile_page)
        # pushButton_2 = setting page
        self.pushButton_2.clicked.connect(self.goto_setting_page)

    def goto_property_page(self, checked):
        self.property_page = Property_Page()
        self.property_page.show()

    def goto_user_profile_page(self, checked):
        self.user_profile = Userprofile()
        self.user_profile.show()

    def goto_setting_page(self, checked):
        self.setting_page = Setting_Page()
        self.setting_page.show()