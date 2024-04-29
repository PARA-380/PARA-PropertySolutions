from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QHBoxLayout, QMessageBox, QComboBox
)
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QDesktopServices  
import sys
import re
# from Property_Button_Controller import Property_Controller
from System import Cont_Property,Cont_Tenant, Property

# Define a class Property_info
class Property_Info(QMainWindow):
    def __init__(self, property_number, tenant_controller : Cont_Tenant, property_controller: Cont_Property):
        super().__init__()
        self.property_controller = property_controller
        self.tenant_controller = tenant_controller
        self.property_number = property_number
        # self.property_id where do we get this from? Dictionary in Property Button?
        self.property_id = self.property_controller.getPropertyID(self.property_number)
        self.resize(800, 600)
        self.setWindowTitle(f"Property {property_number} Information")

        # Initialize Property_Controller instance
        # self.controller = Property_Controller()  
        # self.controller.create_property_info(property_number)  # Create Property_Info instance in controller


        # Create a central widget
        central_widget = QWidget()  
        # Set the central widget - for main window
        self.setCentralWidget(central_widget)  

        # Main layout
        layout = QVBoxLayout() 
        central_widget.setLayout(layout)

        # Instance variable to store the address
        # self.address = ""  

        # Address Input
        address_layout = QHBoxLayout()
        layout.addLayout(address_layout)
        #self.setup_address(self.property_number)

        # Line edit for entering address
        self.address_input = QLineEdit()  
        self.address_input.setPlaceholderText("Enter Address")
        address_layout.addWidget(self.address_input)

        # Button to save address
        save_button = QPushButton("Save") 
        save_button.clicked.connect(lambda: self.save_address())
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

        # Dropdown list for selecting type
        self.type_dropdown = QComboBox()  
        self.type_dropdown.addItems(["Collect", "Pay"])
        input_layout.addWidget(self.type_dropdown)

        # Tenant dropdown list
        self.tenant_dropdown = QComboBox()  # Combo box for selecting tenant
        self.tenantNames_to_id = self.tenant_controller.get_tenant_names() #changed name from tenantNames
        self.tenant_dropdown.addItems(self.tenantNames_to_id.keys())  # Add tenant names here
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
        add_tenant_button.clicked.connect(lambda : self.add_tenant_to_table())
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
        self.property_table.setColumnCount(3)
        self.property_table.setHorizontalHeaderLabels(["Description", "Price", "Type"])
        tables_layout.addWidget(self.property_table)

        # Add initial total row
        self.add_initial_total_row()

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

            # Create QTableWidgetItem objects for the description price, and type
            description_item = QTableWidgetItem(description)
            price_item = QTableWidgetItem(price)
            
            # Set the QTableWidgetItem objects in the property table
            # Set the description item in the first column (index 0) 
            self.property_table.setItem(row_count, 0, description_item)
            # Set the price item in the second column (index 1)
            self.property_table.setItem(row_count, 1, price_item)

            # use the selected value from the single type_dropdown
            selected_type = self.type_dropdown.currentText()

            # Set the type for the new property
            type_item = QTableWidgetItem(selected_type)
            self.property_table.setItem(row_count, 2, type_item)


            # Clear the input fields after adding the property to the table
            self.clear_inputs()
        
        self.calculate_total()  # Call the calculate_total method after adding a property

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

        self.calculate_total()  # Call the calculate_total method after adding a property

    def calculate_total(self):
        total_collect = 0
        total_pay = 0

        # Iterate over each row in the property table
        for row in range(self.property_table.rowCount()):
            # Retrieve the type and price from the current row
            type_item = self.property_table.item(row, 2)
            price_item = self.property_table.item(row, 1)

            # Check if both type_item and price_item are not None
            if type_item is not None and price_item is not None:
                # Check the type and add the price accordingly
                if type_item.text() == "Collect":
                    total_collect += float(price_item.text())
                elif type_item.text() == "Pay":
                    total_pay -= float(price_item.text())

        # Set the total values in the first row of the price column
        total_price = total_collect + total_pay
        total_price_item = QTableWidgetItem(str(total_price))
        self.property_table.setItem(0, 1, total_price_item)

    def add_initial_total_row(self):
        # Add a row at the beginning of the table for the total
        self.property_table.insertRow(0)

        # Set the text for the cells in the total row
        total_item = QTableWidgetItem("Total")
        total_item.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.property_table.setItem(0, 0, total_item)

        # Set placeholders for price and type columns
        self.property_table.setItem(0, 1, QTableWidgetItem(""))
        self.property_table.setCellWidget(0, 2, QWidget())

     # Function to add tenant details to tenants table
    def add_tenant_to_table(self, tenant_name = None):
        """Adds a new tenant to the property and to the table
        Also Add the new tenant to that property with the controller

        Args:
            tenant_name (_type_, optional): The string name that will be displayed. Defaults to None.
        """
        if tenant_name == None:
            tenant_name = self.tenant_dropdown.currentText()

        # Here, retrieve other details of the tenant using the selected name,
        # and add them to the table. adding the name for now (testing purpose)

        # Check if a tenant name is selected (i.e., if it is not empty)

        #assigns tenant to property by setting its property ID and address
        if tenant_name:
            self.display_tenant_on_table(tenant_name)
            self.assign_tenant(tenant_name)
        # self.tenant_controller.add_to_property(tenant_id????,self.property_id)
        #ask controller to set property id to this tenant

    def display_tenant_on_table(self, tenant_name):
        """strictly displays a tenant on the GUI table for the property

        Args:
            tenant_name (_type_): Name to display
        """
        if tenant_name:
            # Get the current row count of the tenants table
            row_count = self.tenants_table.rowCount()

            # Increase the row count by 1 to accommodate the new tenant
            self.tenants_table.setRowCount(row_count + 1)

            # Create a QTableWidgetItem object to hold the tenant name
            name_item = QTableWidgetItem(tenant_name)

            #get tenant id from a dictionary [names -> ID]

            # Set the QTableWidgetItem object in the tenants table
            # Set the tenant name item in the first column (index 0)
            self.tenants_table.setItem(row_count, 0, name_item)

    def assign_tenant(self, tenant_name):
        """Does all the things that happen to the tenant when you add a tenant to 
        a Property. 
            *Setting the property ID in Tenant.
            *Setting the Address of Tenant
            *   
            *

        Args:
            tenant_name (_type_): The tenant_name we were working with from the dropdown.
        """
        #get property ID from dictionary [property_number -> property_id]
        tenant_id = self.tenantNames_to_id[tenant_name]
        #Sets the tenants property ID so we can find it under that ID
        self.tenant_controller.add_to_property(tenant_id,self.property_id)
        #Get the property's address and set it and update the database
        address=self.property_controller.get_property_address(self.property_id)

        self.tenant_controller.update_tenant_address(tenant_id=tenant_id, new_address=address)

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
    # Note this is mot save to database, this is just for the display purpose
    def save_address(self, address: str = None):
        """When the user saves the address, save to database and display on GUI

        Args:
            address (str, optional): Address string to set to. Defaults to None.
        """
        # Save the address associated with this property number using the controller
        if address is None:
            address = self.address_input.text()
        # self.controller.save_address_controller(self.property_number, address)
        #print(f"{property.get_address()}")
        # Display the address in the label
        self.address_label.setText(f"Address: {address}")
        #now have the Controller set the address
        self.property_controller.update_address(address,self.property_id)


    def setup_address(self, key: int = None):
        """Sets the existing address on GUI when opening the property's info

        Args:
            key (int, optional): The Property Number to translate to Property ID. Defaults to None.
        """
        address = self.property_controller.get_property_address(self.property_controller.getPropertyID(key))
        print(f"Address:     {address}")
        self.save_address(address)

    def setup_tenants(self):
        """create a list of tenants already assigned to this property
        asks the controller for list of tenants at that property
        """
        tenants = self.tenant_controller.get_tenants_at_property(self.property_id)
        print(f"tenants at property{self.property_id}: {tenants}")
        for tenant in tenants:
            self.display_tenant_on_table(tenant.getFirstName())

        pass

        

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
    
    def _set_address_label(self, address):
        self.address_label.setText(address)
        self.address_label.update()  # Update the label in the GUI
    
    def get_address_label(self):
        return self.address_label.text()
    
    def get_property_number(self):
        return self.property_number
    
