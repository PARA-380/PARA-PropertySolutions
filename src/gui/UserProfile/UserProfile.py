"""
File: UserProfile.py
Name: Ridham Patel
Date: 04/02/2024
Description: User Prifle page user interface
Purposes: 1. To edit information connected to the current user.
          2. To display information
"""
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QHBoxLayout, QMessageBox, QComboBox
)
from PyQt6.QtCore import Qt
import sys
#HelloWorld
from src.gui.UserProfile.User_Profile_GUI import Ui_MainWindow
from System import Cont_UserProfile, Account

class Userprofile(QMainWindow, Ui_MainWindow):
    """Represents the UserProfile interface for the application.

    Args:
        QMainWindow (QMainWindow):  The base class for the main window of the application.
        Ui_MainWindow (Ui_MainWindow): The user interface class for the UserProfile with the assist of QtDesigner.
    """
    def __init__(self, Cont_UserProfile : Cont_UserProfile):
        """Initializes the UserProfile instance.

        Args:
            Cont_UserProfile (Cont_UserProfile):  An instance of Cont_UserProfile, 
                which handles user profile-related functionalities.
        """
        super().__init__()
        self.setupUi(self)

        self.Cont_UserProfile = Cont_UserProfile #Connects to Controller to access database
        print(self.Cont_UserProfile.mainAccount)
        self.DisplayInfo()
        self.pushButton.clicked.connect(self.SaveInfo) #Connect pushButton1 to DisplayInfo
        # self.pushButton.clicked.connect(self.ClearFields) #Clears the lines after saving
        self.pushButton_2.clicked.connect(self.ClearFields)  # Connect pushButton2 to ClearFields

        self.lineEdit.setText(self.Cont_UserProfile.getMainAccount().get_username())
        self.lineEdit_2.setText(self.Cont_UserProfile.getMainAccount().get_firstName())
        self.lineEdit_3.setText(self.Cont_UserProfile.getMainAccount().get_lastName())
        self.lineEdit_4.setText(self.Cont_UserProfile.getMainAccount().get_phonenumber())

        self.show()

    def SaveInfo(self):
        """Saves the information about the user entered into the line edits.
        """
        mainAcc = self.Cont_UserProfile.getMainAccount()
        # self.lineEdit.(mainAcc.get_firstName())
        username = self.lineEdit.text()
        FirstName = self.lineEdit_2.text()
        LastName = self.lineEdit_3.text()
        PhoneNumber = self.lineEdit_4.text()
        #controller work
        tempacc = Account(first=FirstName,last=LastName,username=username,phone=PhoneNumber)
        #uses the controller to update the database and the controllers main account with new info
        self.Cont_UserProfile.updateAccount(accID=mainAcc.getID(), tempAcc=tempacc)

        # FullName = FirstName + " " + LastName
        mainAcc :Account = self.Cont_UserProfile.getMainAccount()
        self.textEdit.setText(f"Username: {mainAcc.get_username()}\n"
                              f"Full Name: {mainAcc.get_firstName()} {mainAcc.get_lastName()}\n"
                              f"Phone Number: {mainAcc.get_phonenumber()}")
        
    def DisplayInfo(self):
        """Display information about the account from the database.
        """
        mainAcc = self.Cont_UserProfile.getMainAccount()
        #mainAcc :Account = self.Cont_UserProfile.getMainAccount()
        self.textEdit.setText(f"Username: {mainAcc.get_username()}\n"
                              f"Full Name: {mainAcc.get_firstName()} {mainAcc.get_lastName()}\n"
                              f"Phone Number: {mainAcc.get_phonenumber()}") 

    def ClearFields(self):
        """Clears the information entered into the line edits.
        """
        self.lineEdit.clear()  # Clear username field
        self.lineEdit_2.clear()  # Clear first name field
        self.lineEdit_3.clear()  # Clear last name field
        self.lineEdit_4.clear()  # Clear phone number field



if __name__ == "__main__":
    """Runs the application.
    """
    app = QApplication(sys.argv)
    UserProfile_page = Userprofile()
    UserProfile_page.show()
    sys.exit(app.exec())