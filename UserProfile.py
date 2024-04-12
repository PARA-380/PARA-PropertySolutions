from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QHBoxLayout, QMessageBox, QComboBox
)
from PyQt6.QtCore import Qt
import sys
#HelloWorld
from User_Profile import Ui_MainWindow
from Cont_UserProfile import Cont_UserProfile, Account

class Userprofile(QMainWindow, Ui_MainWindow):
    def __init__(self): #Cont_UserProfile : Cont_UserProfile
        super().__init__()
        self.setupUi(self)
        self.Cont_UserProfile = Cont_UserProfile #Connects to Controller to access database

        self.pushButton.clicked.connect(self.DisplayInfo) #Connect pushButton1 to DisplayInfo
        self.pushButton.clicked.connect(self.ClearFields) #Clears the lines after saving
        self.pushButton_2.clicked.connect(self.ClearFields)  # Connect pushButton2 to ClearFields
        self.show()




    def DisplayInfo(self):
        username = self.lineEdit.text()
        FirstName = self.lineEdit_2.text()
        LastName = self.lineEdit_3.text()
        PhoneNumber = self.lineEdit_4.text()
        FullName = FirstName + " " + LastName
        account :Account = self.Cont_UserProfile.getMainAccount()
        self.textEdit.setText(f"Username: {account.get_username()}\n"
                              f"Full Name: {account.get_firstName()}\n"
                              f"Phone Number: {account.get_phonenumber()}")

    def ClearFields(self):
        self.lineEdit.clear()  # Clear username field
        self.lineEdit_2.clear()  # Clear first name field
        self.lineEdit_3.clear()  # Clear last name field
        self.lineEdit_4.clear()  # Clear phone number field



if __name__ == "__main__":
    app = QApplication(sys.argv)
    UserProfile_page = Userprofile()
    UserProfile_page.show()
    sys.exit(app.exec())