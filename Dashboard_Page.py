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
'''
print("*************")
print(os.getcwd())
print("**************")
sys.path.append("gui")
sys.path.append("Property_GUI")'
'''
# C:\Users\richa\Desktop\Github Project\PARA-PropertySolutions\gui
#print(sys.path.append("gui\Property_GUI"))
#import Property_GUI.Property_Button_Controller

from gui.pyqt_dashboard import Ui_DashBoard
# from test_page import test_page
from gui.UserProfile import Userprofile
from Property_GUI.Property_main import Property_Page
# from Property_GUI.Property_Button_Controller import Property_Controller

class Dashboard(QMainWindow, Ui_DashBoard):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.Properties_btn.clicked.connect(self.goto_property_page)
        # pushButton = userprofile page
        self.pushButton_3.clicked.connect(self.goto_user_profile_page)

    def goto_property_page(self, checked):
        self.property_page = Property_Page()
        self.property_page.show()

    def goto_user_profile_page(self, checked):
        self.user_profile = Userprofile()
        self.user_profile.show()
