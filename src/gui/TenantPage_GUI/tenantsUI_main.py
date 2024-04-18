from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QHBoxLayout, QMessageBox, QComboBox
)
from PyQt6.QtCore import Qt
import sys

from src.gui.TenantPage_GUI.QtTenantPage import Ui_MainWindow
from System import Tenant, Cont_Tenant

class tenantsui(QMainWindow, Ui_MainWindow):
    def __init__(self, controller_tenant : Cont_Tenant):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.cont_tenant = controller_tenant
        self.Add_Tenants(self.cont_tenant.get_tenants())#populates table with existing tenants
        First_Name =  self.LE_FirstName.text()
        Last_Name = self.LE_LastName.text()
        SSN = self.LE_SSN.text()
        Phone_Number = self.LE_PhoneNumber.text()
        Email = self.LE_Email.text()
        self.AddTenant.clicked.connect(lambda : self.__Add_Tenant(tenant=None))
        self.DeleteTenant.clicked.connect(self.Delete_Tenant)  # Connect the Delete Tenant button
        self.tableWidget.setColumnWidth(4, 600)
        self.tableWidget.setColumnWidth(2, 300)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(3, 200)

#Note for next time, Need to fill table with tenants first, then allow to add new tenants on click add.

    def Add_Tenants(self, tenants):
        """Populates the table with existing tenants from Database

        Args:
            tenants (_type_): list of tenant types
        """
        for tenant in tenants:
            # print(f"{tenant}, {type(tenant)}")
            self.__Add_Tenant(tenant)

    def __Add_Tenant(self, tenant : Tenant = None):
        """Adds a single tenant to a row in the tenant page UI
        can give a tenant object or will use the items filled in the UI rows by user

        Args:
            tenant (Tenant, optional): The tenant to be added to the row, 
            mostly used by tenants which already exist in data base to be added to table. 
            Defaults to None.
        """
        if tenant is None:
            print(f"reading from the user input")
            First_Name =  self.LE_FirstName.text()
            Last_Name = self.LE_LastName.text()
            SSN = self.LE_SSN.text()
            Phone_Number = self.LE_PhoneNumber.text()
            Email = self.LE_Email.text()
            tenant = Tenant(firstname=First_Name,lastname=Last_Name,ssn=SSN,phonenumber=Phone_Number,email=Email)
            # print(f"New Tenant Added!: {tenant}")
            self.cont_tenant.create_tenant(tenant)
        

        # Insert a new row at the end of the tableWidget
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)

        print(f"HEEERHHRHHRHREEEEE: {tenant.getID()}")

        # Add the data to the new row
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(tenant.getFirstName()))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(tenant.getLastName()))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(tenant.getSSN()))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(tenant.getPhoneNumber()))
        self.tableWidget.setItem(row_position, 4, QTableWidgetItem(tenant.getEmail()))
        self.tableWidget.setItem(row_position, 6, QTableWidgetItem(tenant.getID()))


    def Delete_Tenant(self):
        current_row = self.tableWidget.currentRow()  # Get the index of the currently selected row
        selected_row = self.tableWidget.selectionModel().selectedRows()
        print(f"ROW: {selected_row}")
        for index in selected_row:
            ten_id = self.tableWidget.model().data(self.tableWidget.model().index(index.row(), 5))
            print(f'TRY THIS{ten_id}')
            print(f"column: {index.column()}, row: {index.row()}")
            id = self.tableWidget.columnAt(6) #get the ssn from the ssn column
            print(f'TRY THIS{id}')
            print(selected_row)
            if current_row >= 0:  # Check if a row is selected (index is valid)
                self.tableWidget.removeRow(current_row)  # Remove the selected row
                self.cont_tenant.remove_tenant(ten_id)
            else:
                QMessageBox.warning(self, "Warning", "Please select a row to delete", QMessageBox.StandardButton.Ok)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Tenant_page = tenantsui()
    Tenant_page.show()
    sys.exit(app.exec())