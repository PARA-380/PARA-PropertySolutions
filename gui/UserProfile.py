from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QHBoxLayout, QMessageBox, QComboBox
)
from PyQt6.QtCore import Qt
import sys

from User_Profile import Ui_MainWindow

class Userprofile(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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

        self.textEdit.setText(f"Username: {username}\n"
                              f"Full Name: {FullName}\n"
                              f"Phone Number: {PhoneNumber}")

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