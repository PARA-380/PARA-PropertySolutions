from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QHBoxLayout, QMessageBox, QComboBox
)
from PyQt6.QtCore import Qt
import sys
import tenantsUI_Controller

from QtTenantPage import Ui_MainWindow

class tenantsui(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.AddTenant.clicked.connect(self.Add_Tenant)
        self.DeleteTenant.clicked.connect(self.Delete_Tenant)  # Connect the Delete Tenant button
        self.tableWidget.setColumnWidth(4, 600)
        self.tableWidget.setColumnWidth(2, 300)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(3, 200)

    def Add_Tenant(self):
        First_Name =  self.LE_FirstName.text()
        Last_Name = self.LE_LastName.text()
        SSN = self.LE_SSN.text()
        Phone_Number = self.LE_PhoneNumber.text()
        Email = self.LE_Email.text()

        # Insert a new row at the end of the tableWidget
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)

        # Add the data to the new row
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(First_Name))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(Last_Name))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(SSN))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(Phone_Number))
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(Email))


    def Delete_Tenant(self):
        selected_row = self.tableWidget.currentRow()  # Get the index of the currently selected row
        if selected_row >= 0:  # Check if a row is selected (index is valid)
            self.tableWidget.removeRow(selected_row)  # Remove the selected row
        else:
            QMessageBox.warning(self, "Warning", "Please select a row to delete", QMessageBox.StandardButton.Ok)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Tenant_page = tenantsui()
    Tenant_page.show()
    sys.exit(app.exec())