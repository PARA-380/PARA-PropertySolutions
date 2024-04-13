from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QHBoxLayout, QMessageBox, QComboBox
)
from PyQt6.QtCore import Qt
import sys
#HelloWorld
from src.gui.UserProfile.User_Profile_GUI import Ui_MainWindow
from System import Cont_UserProfile, Account

class Userprofile(QMainWindow, Ui_MainWindow):
    def __init__(self, Cont_UserProfile : Cont_UserProfile):
        super().__init__()
        self.setupUi(self)
        self.Cont_UserProfile = Cont_UserProfile #Connects to Controller to access database
        self.DisplayInfo()
        self.pushButton.clicked.connect(self.SaveInfo) #Connect pushButton1 to DisplayInfo
        # self.pushButton.clicked.connect(self.ClearFields) #Clears the lines after saving
        self.pushButton_2.clicked.connect(self.ClearFields)  # Connect pushButton2 to ClearFields
        self.show()

    def SaveInfo(self):
        mainAcc = self.Cont_UserProfile._getMainAccount()
        # self.lineEdit.(mainAcc.get_firstName())
        username = self.lineEdit.text()
        FirstName = self.lineEdit_2.text()
        LastName = self.lineEdit_3.text()
        PhoneNumber = self.lineEdit_4.text()
        #controller work
        tempacc = Account(first=FirstName,last=LastName,username=username,phone=PhoneNumber)
        #uses the controller to update the database and the controllers main account with new info
        self.Cont_UserProfile._updateAccount(accID=mainAcc.getID(), tempAcc=tempacc)

        # FullName = FirstName + " " + LastName
        mainAcc :Account = self.Cont_UserProfile._getMainAccount()
        self.textEdit.setText(f"Username: {mainAcc.get_username()}\n"
                              f"Full Name: {mainAcc.get_firstName()} {mainAcc.get_lastName()}\n"
                              f"Phone Number: {mainAcc.get_phonenumber()}")
        
    def DisplayInfo(self):
        mainAcc = self.Cont_UserProfile._getMainAccount()
        mainAcc :Account = self.Cont_UserProfile._getMainAccount()
        self.textEdit.setText(f"Username: {mainAcc.get_username()}\n"
                              f"Full Name: {mainAcc.get_firstName()} {mainAcc.get_lastName()}\n"
                              f"Phone Number: {mainAcc.get_phonenumber()}") 

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