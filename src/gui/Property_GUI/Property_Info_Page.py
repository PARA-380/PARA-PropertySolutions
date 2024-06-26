"""
File: Property_main.py
Name: Jittapatana (Patrick) Prayoonpruk
Date: 04/05/2024
Description: Property main page user interface
Purposes: 1. To add new tenants into the property
          2. To add property information including address and bills
          3. To see the total earning according to the bills
"""
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QHBoxLayout, QMessageBox, QComboBox
)
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QDesktopServices, QFont 
import sys
import re
import matplotlib.pyplot as plt
# from Property_Button_Controller import Property_Controller
from System import Cont_Property,Cont_Tenant, Cont_Bill, Property, Bill, Tenant

# Define a class Property_info
class Property_Info(QMainWindow):
    """Represents the user interface for the property main page

    Args:
        QMainWindow: The base class for the main window widget.
    """
        
    def __init__(self, property_number, tenant_controller : Cont_Tenant, property_controller: Cont_Property, bill_controller : Cont_Bill):
        """Initializes the Property_Info object.

        Args:
            property_number (int): The unique identifier for the property.
        """
        super().__init__()
        self.property_controller = property_controller
        self.tenant_controller = tenant_controller
        self.bill_controller = bill_controller
        self.property_number = property_number
        # self.property_id where do we get this from? Dictionary in Property Button?
        self.property_id = self.property_controller.getPropertyID(self.property_number)
        # self.bill_controller.change_property(self.property_id)
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
        self.input_layout = QHBoxLayout()
        layout.addLayout(self.input_layout)

        # Line edit for entering property description
        self.description_input = QLineEdit()  
        self.description_input.setPlaceholderText("Description")
        self.description_input.setFixedWidth(150)
        self.input_layout.addWidget(self.description_input)

        # Line edit for entering property price
        self.price_input = QLineEdit()  
        self.price_input.setPlaceholderText("Price")
        self.price_input.setFixedWidth(100)
        self.input_layout.addWidget(self.price_input)

        # Dropdown list for selecting type
        self.type_dropdown = QComboBox()  
        self.type_dropdown.addItems(["Collect", "Pay"])
        self.input_layout.addWidget(self.type_dropdown)

        # Tenant dropdown list
        self.tenant_dropdown = QComboBox()  # Combo box for selecting tenant
        self.tenantNames_to_id = self.tenant_controller.get_tenant_names() #changed name from tenantNames
        self.tenant_dropdown.addItems(self.tenantNames_to_id.keys())  # Add tenant names here
        self.input_layout.addWidget(self.tenant_dropdown)

        # Buttons
        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)

        # Button to add property description to table
        add_button = QPushButton("Add Description")  
        add_button.clicked.connect(lambda : self.add_property_to_table())
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
        self.property_table.setColumnCount(4)
        self.property_table.setHorizontalHeaderLabels(["Item ID", "Description", "Price", "Type"])
        tables_layout.addWidget(self.property_table)

        # Add initial total row
        self.add_initial_total_row()

        # Tenants Table (right)
        self.tenants_table = QTableWidget()  # Table to display tenant details
        self.tenants_table.setColumnCount(4)
        self.tenants_table.setHorizontalHeaderLabels(["Tenant ID","First Name", "Last Name", "Contact"])
        tables_layout.addWidget(self.tenants_table)

        # See Pie Chart Button
        see_pie_chart_button = QPushButton("See Pie Chart")  # Button to see pie chart
        see_pie_chart_button.clicked.connect(self.see_pie_chart)
        layout.addWidget(see_pie_chart_button)

        # Line edit for inputting the link
        # self.link_input = QLineEdit(self)
        # self.link_input.setPlaceholderText("Enter link here")
        # self.input_layout.addWidget(self.link_input)
        self.setup_link()

        # Button to open the link
        self.open_link_button = QPushButton("See Images", self)
        self.open_link_button.clicked.connect(lambda: self.open_link_button_clicked())
        button_layout.addWidget(self.open_link_button)

        self.row_count = 1

    def setup_on_open(self):
        """all the necessary things to be done when opening this property info.
        Note: still in scope as long as property main is open. Many things
        to need to be aware of.
        """
        self.setup_address(self.property_number)
        self.change_bill_scope()
        self.setup_bills()
        self.calculate_total()

    def create_bill(self, description : str, type : str, price : int):
        """

        Args:
            description (str): _description_
            type (str): _description_
            price (int): _description_

        Returns:
            bill_id: id of bill added.
        """
        print(f"bill create: {description} {type} {price}")
        return self.bill_controller.create_bill(description=description, type=type, amount=price)

    # Function to add property details to property table
    def add_property_to_table(self, bill : Bill = None):
        """Adds property details to the property table.
        """

        #take user input
        if bill is None:
            description = self.description_input.text()
            price = self.price_input.text()
            # 
            try:
                price_float = float(price)
            except ValueError:
                # If the conversion fails (e.g., if price contains non-numeric characters),
                # display a warning message and return from the function
                QMessageBox.warning(self, "Warning", "Price must be a valid number.")
                return
            # use the selected value from the single type_dropdown
            selected_type = str(self.type_dropdown.currentText())
            print(f"BillType: {type(selected_type)}")
            item_id = self.create_bill(description=description,type=selected_type,price=price)
            # item_id = self.bill_controller.find_bill_id(description, price)
        else:
            # print(f"BILL: {type(bill.get_type())}")
            description = bill.getDescription()
            price = bill.getAmount()
            item_id = bill.get_bill_id()
            print(f"price: {price}")
            selected_type = bill.get_type()

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
            self.row_count = self.property_table.rowCount()
            print("row_count: ", self.row_count)
            # Increment the row count to accommodate the new property
            self.property_table.setRowCount(self.row_count + 1)

            # Create QTableWidgetItem objects for the description price, and type
            description_item = QTableWidgetItem(description)
            price_item = QTableWidgetItem(str(price))
            id_item = QTableWidgetItem(str(item_id))
            
            self.property_table.setItem(self.row_count, 0, id_item)
            # Set the QTableWidgetItem objects in the property table
            # Set the description item in the first column (index 0) 
            self.property_table.setItem(self.row_count, 1, description_item)
            # Set the price item in the second column (index 1)
            self.property_table.setItem(self.row_count, 2, price_item)

            # use the selected value from the single type_dropdown
            # selected_type = self.type_dropdown.currentText()

            # Set the type for the new property
            type_item = QTableWidgetItem(selected_type)
            self.property_table.setItem(self.row_count, 3, type_item)


            # Clear the input fields after adding the property to the table
            self.clear_inputs()
        
        self.calculate_total()  # Call the calculate_total method after adding a property

    # def clear_table(self, table, start=0):


    # Function to delete selected property from property table
    def delete_property_from_table(self):
        """Deletes selected property from the property table.
        """
        # Get the index of the currently selected row in the property table
        current_row = self.property_table.currentRow()
        selected_row = self.property_table.selectionModel().selectedRows()
        for index in selected_row:
            item_id = self.property_table.model().data(self.property_table.model().index(index.row(), 0))
            # Check if a row is selected (i.e., if selected_row is not negative)
            if current_row >= 0:
                # If a row is selected, remove it from the property table
                self.property_table.removeRow(current_row)
                self.bill_controller.delete_bill(int(item_id))
            else:
                # If no row is selected (selected_row is negative), display a warning message
                QMessageBox.warning(self, "Warning", "No row selected.")

        self.calculate_total()  # Call the calculate_total method after adding a property

    def calculate_total(self):
        """Calculates the total earning according to the property bills.

        The bills can either be "collect" or "pay"
        """
        total_collect = 0
        total_pay = 0

        # Iterate over each row in the property table
        for row in range(self.property_table.rowCount()):
            # Retrieve the type and price from the current row
            type_item = self.property_table.item(row, 3)
            price_item = self.property_table.item(row, 2)
            # print(f"DEBUG: {type_item}")
            # print(f"DEBUG: {price_item}")

            # Check if both type_item and price_item are not None
            if type_item is not None and price_item is not None:
                # Check the type and add the price accordingly
                if type_item.text().lower() == "collect":
                    total_collect += float(price_item.text())
                elif type_item.text().lower() == "pay":
                    total_pay -= float(price_item.text())

        # Set the total values in the first row of the price column
        total_price = total_collect + total_pay
        total_price_item = QTableWidgetItem(str(total_price))
        self.property_table.setItem(0, 2, total_price_item)

    def reset_table_row_count(self, new_row_count):
        """Resets the row count of the property table."""
        self.property_table.setRowCount(new_row_count)

    def add_initial_total_row(self):
        """Adds an initial total row to the property details table.

        This method inserts a new row at the beginning of the property details table to display the total earnings.
        The total row contains the text "Total" in the description column and placeholders for the price and type columns.
        """
        # Add a row at the beginning of the table for the total
        self.property_table.insertRow(0)

        # Set the text for the cells in the total row
        total_item = QTableWidgetItem("Total")
        # total_item.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        total_item.setTextAlignment(Qt.AlignmentFlag.AlignVCenter)
        total_item.setFont(QFont("Times",weight = 15))
        self.property_table.setItem(0, 1, total_item)

        # Set placeholders for price and type columns
        self.property_table.setItem(0, 2, QTableWidgetItem(""))
        self.property_table.setCellWidget(0, 3, QWidget())

     # Function to add tenant details to tenants table
    def add_tenant_to_table(self, tenant_name = None):
        """Adds a new tenant to the property and to the table
        Also Add the new tenant to that property with the controller

        Args:
            tenant_name (_type_, optional): The string name that will be displayed. Defaults to None.
        """
        # user input
        if tenant_name == None:
            tenant_name = self.tenant_dropdown.currentText()
            tenant_full_name = tenant_name.split()
            tenant_first_name = tenant_full_name[0].strip()
            tenant_last_name = tenant_full_name[1].strip()
            #self.tenant_controller.print_tenants()
            tenant_id = self.tenant_controller.find_tenant_id(tenant_first_name, tenant_last_name)
            tenant_contact = self.tenant_controller.find_tenant_contact(tenant_first_name, tenant_last_name)

        # Here, retrieve other details of the tenant using the selected name,
        # and add them to the table. adding the name for now (testing purpose)

        # Check if a tenant name is selected (i.e., if it is not empty)

        #assigns tenant to property by setting its property ID and address
        if tenant_name:
            tenant_id = self.tenant_controller.find_tenant_id(tenant_first_name, tenant_last_name)
            tenant_contact = self.tenant_controller.find_tenant_contact(tenant_first_name, tenant_last_name)
            self.display_tenant_on_table(tenant_id, tenant_first_name, tenant_last_name, tenant_contact)
            self.assign_tenant(tenant_name)
        # self.tenant_controller.add_to_property(tenant_id????,self.property_id)
        #ask controller to set property id to this tenant

    def display_tenant_on_table(self, tenant_id, tenant_first_name, tenant_last_name, tenant_contact):
        """strictly displays a tenant on the GUI table for the property

        Args:
            tenant_name (_type_): Name to display
        """
        if tenant_first_name and tenant_last_name:
            # Get the current row count of the tenants table
            row_count = self.tenants_table.rowCount()

            # Increase the row count by 1 to accommodate the new tenant
            self.tenants_table.setRowCount(row_count + 1)

            # Create a QTableWidgetItem object to hold the tenant name
            tenant_id_item = QTableWidgetItem(str(tenant_id))
            first_name_item = QTableWidgetItem(tenant_first_name)
            last_name_item = QTableWidgetItem(tenant_last_name)
            contact_item = QTableWidgetItem(str(tenant_contact))

            #get tenant id from a dictionary [names -> ID]

            # Set the QTableWidgetItem object in the tenants table
            # Set the tenant name item in the first column (index 0)
            self.tenants_table.setItem(row_count, 0, tenant_id_item)
            self.tenants_table.setItem(row_count, 1, first_name_item)
            self.tenants_table.setItem(row_count, 2, last_name_item)
            self.tenants_table.setItem(row_count, 3, contact_item)

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
        """Deletes selected tenant from the tenants table.
        """
        # Get the index of the currently selected row in the tenants table
        current_row = self.tenants_table.currentRow()
        selected_row = self.tenants_table.selectionModel().selectedRows()

        for index in selected_row:
            tenant_first_name = self.tenants_table.model().data(self.tenants_table.model().index(index.row(), 1))
            tenant_last_name = self.tenants_table.model().data(self.tenants_table.model().index(index.row(), 2))

        # The rest logic is the same as delete_property_from_table
        if current_row >= 0:
            # self.tenants_table.removeRow(current_row)
            tenant_id = self.tenant_controller.find_tenant_id(tenant_first_name, tenant_last_name)
            self.tenant_controller.unassign_tenant_from_property(tenant_id)
            print("tenant_id found: ", tenant_id)
            self.tenants_table.removeRow(current_row)  # Remove the selected row

        else:
            QMessageBox.warning(self, "Warning", "No row selected.")

    # Function to clear input fields
    def clear_inputs(self):
        """Clears the input fields.

        Clears the input fields, including description and price, and reset it to the empty state
        """
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

    def setup_link(self):
        """on initial startup of property page, set the link to an existing link or prompt user to enter one.
        """
        self.link_input = QLineEdit(self)
        self.check_link_exists()
        # Line edit for inputting the link
        self.input_layout.addWidget(self.link_input)

    def check_link_exists(self):
        """if link exists, display it. Otherwise prompt user to enter one.
        """
        link = self.property_controller.get_property_link_images(self.property_id)
        if link == None:
            self.link_input.setPlaceholderText("Enter link here")
        else:
            print(f"Link: {link}")
            self.link_input.setText(link)
            # self.open_link_button_clicked(link)

    def save_link(self):
        """ask controller to save the link
        """
        link = self.link_input.text()
        self.property_controller.update_link_images(link, self.property_id)

    # Function to open the link when the see images is clicked
    def open_link_button_clicked(self, link: str = None):
        """Opens the link when the "See Images" button is clicked.
        """
        if link is None:
            link = self.link_input.text()
            print('link: ', link)
            self.property_controller.update_link_images(link, self.property_id)
        else:
            self.check_link_exists()

        # self.link_input.setText(link)

        # Regular expression to validate the link format
        link_pattern = re.compile(r'https?://\S+')  # Simple pattern to match URLs starting with http:// or https://

        if link_pattern.fullmatch(link):
            # Open the link in the default web browser
            QDesktopServices.openUrl(QUrl(link))
        else:
            # Show a warning if the link is invalid
            QMessageBox.warning(self, "Invalid Link", "Please enter a valid link.")
    

    def setup_tenants(self):
        """create a list of tenants already assigned to this property
        asks the controller for list of tenants at that property
        """
        tenants = self.tenant_controller.get_tenants_at_property(self.property_id)
        print(f"tenants at property{self.property_id}: {tenants}")
        for tenant in tenants:
            self.display_tenant_on_table(tenant.getID(), tenant.getFirstName(), tenant.getLastName(), tenant.getPhoneNumber())

    
    def change_bill_scope(self):
        print(f"Changed Property! {self.property_id}")
        self.bill_controller.change_property(self.property_id)

    def clear_bills(self):
        #may need to clear bills table then resetup
        for row in range(1, self.property_table.rowCount()):
            self.property_table.removeRow(row)
            print(f"Removed row: {row}")
        print(f"Cleaning up!")
        self.row_count = self.reset_table_row_count(1)

    def setup_bills(self):
        #go through all bills of this property and display them
        #CLEAR THE TABLE FIRST
        self.clear_bills()
        print(f"setting up!")
        bills = self.bill_controller.get_bills()
        for bill in bills.values():
            print(f"setting up: {(bill.description)}")
            self.add_property_to_table(bill)
            #self.calculate_total()

    def see_pie_chart(self):
        """Display a pie chart

        Data structures: list
        """
        # Extract descriptions and prices from the property table
        descriptions = []
        prices = []
        for row in range(1, self.property_table.rowCount()):
            description_item = self.property_table.item(row, 1)
            price_item = self.property_table.item(row, 2)
            if description_item and price_item:
                descriptions.append(description_item.text())
                prices.append(float(price_item.text()))

        # Plot pie chart if there are data points
        if descriptions and prices:
            # Plot
            plt.figure(figsize=(8, 8))
            plt.pie(prices, labels=descriptions, autopct='%1.1f%%', startangle=140)
            plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            plt.title('Pie Chart')
            plt.show()
        else:
            QMessageBox.warning(self, "Warning", "No data available to plot pie chart.")

    
    def set_address_label(self, address):
        """Sets the address label.

        Args:
            address (str): The address to be set in the label.
        """
        self.address_label.setText(address)
        self.address_label.update()  # Update the label in the GUI
    
    def get_address_label(self):
        """Gets the text from the address label.

        Returns:
            str: The text displayed in the address label.
        """
        return self.address_label.text()
    
    def get_property_number(self):
        """Gets the property number.

        Returns:
            int: The property number associated with this Property_Info object.
        """
        return self.property_number
    
