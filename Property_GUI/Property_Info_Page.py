from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QHBoxLayout, QMessageBox, QComboBox
)
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QDesktopServices  
import sys
import re

# Define a class Property_info
class Property_Info(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.setWindowTitle("Property Information")

        # Create a central widget
        central_widget = QWidget()  
        # Set the central widget - for main window
        self.setCentralWidget(central_widget)  

        layout = QVBoxLayout()  # Main layout
        central_widget.setLayout(layout)

        # Address Input
        address_layout = QHBoxLayout()
        layout.addLayout(address_layout)

        # Line edit for entering address
        self.address_input = QLineEdit()  
        self.address_input.setPlaceholderText("Enter Address")
        address_layout.addWidget(self.address_input)

        # Button to save address
        save_button = QPushButton("Save") 
        save_button.clicked.connect(self.save_address)
        address_layout.addWidget(save_button)

        # Address Label
        self.address_label = QLabel()  # Label to display address
        layout.addWidget(self.address_label)

        # Input Widgets 
        input_layout = QHBoxLayout()
        layout.addLayout(input_layout)

        # Line edit for entering property description
        self.description_input = QLineEdit()  
        self.description_input.setPlaceholderText("Description")
        self.description_input.setFixedWidth(150)
        input_layout.addWidget(self.description_input)

        # Line edit for entering property price
        self.price_input = QLineEdit()  
        self.price_input.setPlaceholderText("Price")
        self.price_input.setFixedWidth(100)
        input_layout.addWidget(self.price_input)

        # Tenant dropdown list
        self.tenant_dropdown = QComboBox()  # Combo box for selecting tenant
        self.tenant_dropdown.addItems(["Tenant 1", "Tenant 2", "Tenant 3"])  # Add tenant names here
        input_layout.addWidget(self.tenant_dropdown)

        # Buttons
        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)

        # Button to add property description to table
        add_button = QPushButton("Add Description")  
        add_button.clicked.connect(self.add_property_to_table)
        button_layout.addWidget(add_button)

        # Button to delete selected property description from table
        delete_button = QPushButton("Delete Selected Description")  
        delete_button.clicked.connect(self.delete_property_from_table)
        button_layout.addWidget(delete_button)

        # Button to add tenant to table
        add_tenant_button = QPushButton("Add Tenant")  
        add_tenant_button.clicked.connect(self.add_tenant_to_table)
        button_layout.addWidget(add_tenant_button)

        # Button to delete selected tenant from table
        delete_tenant_button = QPushButton("Delete Selected Tenant")  
        delete_tenant_button.clicked.connect(self.delete_tenant_from_table)
        button_layout.addWidget(delete_tenant_button)

        # Tables
        tables_layout = QHBoxLayout()
        layout.addLayout(tables_layout)

        # Property Details Table (left)
        self.property_table = QTableWidget()  # Table to display property details
        self.property_table.setColumnCount(2)
        self.property_table.setHorizontalHeaderLabels(["Description", "Price"])
        tables_layout.addWidget(self.property_table)

        # Tenants Table (right)
        self.tenants_table = QTableWidget()  # Table to display tenant details
        self.tenants_table.setColumnCount(2)
        self.tenants_table.setHorizontalHeaderLabels(["Tenant Name", "Contact"])
        tables_layout.addWidget(self.tenants_table)

        # See Pie Chart Button
        see_pie_chart_button = QPushButton("See Pie Chart")  # Button to see pie chart
        see_pie_chart_button.clicked.connect(self.see_pie_chart)
        layout.addWidget(see_pie_chart_button)

        # Line edit for inputting the link
        self.link_input = QLineEdit(self)
        self.link_input.setPlaceholderText("Enter link here")
        input_layout.addWidget(self.link_input)

        # Button to open the link
        self.open_link_button = QPushButton("See Images", self)
        self.open_link_button.clicked.connect(self.open_link_button_clicked)
        button_layout.addWidget(self.open_link_button)

    # Function to add property details to property table
    def add_property_to_table(self):

        description = self.description_input.text()
        price = self.price_input.text()

        # Check if both description and price are not empty
        if description and price:
            # Check if price is a valid number
            # By, attempt to convert price to float
            try:
                price_float = float(price)
            except ValueError:
                # If the conversion fails (e.g., if price contains non-numeric characters),
                # display a warning message and return from the function
                QMessageBox.warning(self, "Warning", "Price must be a valid number.")
                return
            
            # If the conversion is successful, continue to add the property to the table
            # Get the current row count of the property table
            row_count = self.property_table.rowCount()
            # Increment the row count to accommodate the new property
            self.property_table.setRowCount(row_count + 1)

            # Create QTableWidgetItem objects for the description and price
            description_item = QTableWidgetItem(description)
            price_item = QTableWidgetItem(price)

            # Set the QTableWidgetItem objects in the property table
            # Set the description item in the first column (index 0) 
            self.property_table.setItem(row_count, 0, description_item)
            # Set the price item in the second column (index 1)
            self.property_table.setItem(row_count, 1, price_item)

            # Clear the input fields after adding the property to the table
            self.clear_inputs()

    # Function to delete selected property from property table
    def delete_property_from_table(self):
        # Get the index of the currently selected row in the property table
        selected_row = self.property_table.currentRow()

        # Check if a row is selected (i.e., if selected_row is not negative)
        if selected_row >= 0:
            # If a row is selected, remove it from the property table
            self.property_table.removeRow(selected_row)
        else:
            # If no row is selected (selected_row is negative), display a warning message
            QMessageBox.warning(self, "Warning", "No row selected.")

     # Function to add tenant details to tenants table
    def add_tenant_to_table(self):
        tenant_name = self.tenant_dropdown.currentText()

        # Here, retrieve other details of the tenant using the selected name,
        # and add them to the table. adding the name for now (testing purpose)

        # Check if a tenant name is selected (i.e., if it is not empty)
        if tenant_name:
            # Get the current row count of the tenants table
            row_count = self.tenants_table.rowCount()

            # Increase the row count by 1 to accommodate the new tenant
            self.tenants_table.setRowCount(row_count + 1)

            # Create a QTableWidgetItem object to hold the tenant name
            name_item = QTableWidgetItem(tenant_name)

            # Set the QTableWidgetItem object in the tenants table
            # Set the tenant name item in the first column (index 0)
            self.tenants_table.setItem(row_count, 0, name_item)

    # Function to delete selected tenant from tenants table
    def delete_tenant_from_table(self):
        # Get the index of the currently selected row in the tenants table
        selected_row = self.tenants_table.currentRow()

        # The rest logic is the same as delete_property_from_table
        if selected_row >= 0:
            self.tenants_table.removeRow(selected_row)
        else:
            QMessageBox.warning(self, "Warning", "No row selected.")

    # Function to clear input fields
    def clear_inputs(self):
        self.description_input.clear()
        self.price_input.clear()

    # Function to save address input and display it in address label
    def save_address(self):
        address = self.address_input.text()
        self.address_label.setText(f"Address: {address}")

    # If have time
    def see_pie_chart(self):
        # Function to display pie chart
        pass

    # Function to open the link when the see images is clicked
    def open_link_button_clicked(self):
        link = self.link_input.text()

        # Regular expression to validate the link format
        link_pattern = re.compile(r'https?://\S+')  # Simple pattern to match URLs starting with http:// or https://

        if link_pattern.fullmatch(link):
            # Open the link in the default web browser
            QDesktopServices.openUrl(QUrl(link))
        else:
            # Show a warning if the link is invalid
            QMessageBox.warning(self, "Invalid Link", "Please enter a valid link.")

