"""
File: Contractor_Page.py
Name: Jittapatana (Patrick) Prayoonpruk
Date: 04/12/2024
Description: Contractor page user interface
Purposes: 1. To create new contractors
          2. To delete contractors
          3. To assign tasks to contractors
"""

from PyQt6.QtWidgets import (
    QMainWindow, 
    QApplication, 
    QWidget, 
    QLineEdit, 
    QPushButton, 
    QVBoxLayout, 
    QLabel, 
    QTableWidget, 
    QTableWidgetItem, 
    QHBoxLayout, 
    QMessageBox, 
    QComboBox,
    QHeaderView
)

from PyQt6.QtCore import Qt
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QDesktopServices  
import sys

# Define a class for the Contractor Page
class Contractor_Page(QMainWindow):
    """Represents the main window for the contractor page

    This class provides the user interface for managing contractors.

    Args:
        QMainWindow (QMainWindow): The base class for the main window of the application.
    """
    def __init__(self):
        """Initialize the Contractor_Page instance.

        Initializes the user interface components, including input fields, buttons,
        and a table to display contractors' information.
        """
        super().__init__()
        self.resize(800, 600)
        self.setWindowTitle("Contractor Page")

        central_widget = QWidget()  
        self.setCentralWidget(central_widget)  

        layout = QVBoxLayout()  
        central_widget.setLayout(layout)

        input_layout = QHBoxLayout()
        layout.addLayout(input_layout)

        # Create input fields for specialization
        self.specialization_input = QLineEdit()  
        self.specialization_input.setPlaceholderText("Specialization")
        input_layout.addWidget(self.specialization_input)

        # Create input fields for first name
        self.first_name_input = QLineEdit()  
        self.first_name_input.setPlaceholderText("First Name")
        input_layout.addWidget(self.first_name_input)

        # Create input fields for last name
        self.last_name_input = QLineEdit()  
        self.last_name_input.setPlaceholderText("Last Name")
        input_layout.addWidget(self.last_name_input)

        # Create input fields for Phone Number
        self.phone_input = QLineEdit()  
        self.phone_input.setPlaceholderText("Phone Number")
        input_layout.addWidget(self.phone_input)

        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)

        # Add Contractor button
        add_button = QPushButton("Add Contractor")  
        add_button.clicked.connect(self.add_contractor_to_table)
        button_layout.addWidget(add_button)

        # Delete Selected Contractor button
        delete_button = QPushButton("Delete Selected Contractor")  
        delete_button.clicked.connect(self.delete_contractor_from_table)
        button_layout.addWidget(delete_button)

        # Create a table to display contractors' information
        self.contractors_table = QTableWidget()  
        self.contractors_table.setColumnCount(7)  
        self.contractors_table.setHorizontalHeaderLabels(["Specialization", "First Name", "Last Name", "Phone Number", "Property", "Status", "Description"])
        
        # Set the resizing mode for the last section (column) to stretch
        header = self.contractors_table.horizontalHeader()
        header.setSectionResizeMode(6, QHeaderView.ResizeMode.Stretch)

        layout.addWidget(self.contractors_table)
        layout.addWidget(self.contractors_table)

        # Button for recommended contractors
        recommended_button = QPushButton("Recommended Contractors")
        recommended_button.clicked.connect(self.open_recommended_contractors_website)
        layout.addWidget(recommended_button)

    def add_contractor_to_table(self):
        """Add a new contractor to the table

        Retrieves information from input fields and adds a new row to the contractors' table.
        Additionally, adds combo boxes for assigning tasks and status for added contractors.
        """
        # initialize variables
        specialization = self.specialization_input.text()
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        phone = self.phone_input.text()

        # Check if all fields are filled
        if specialization and first_name and last_name and phone:
            row_count = self.contractors_table.rowCount()
            self.contractors_table.setRowCount(row_count + 1)

            # Create table items for specialization, first name, last name, and phone number
            specialization_item = QTableWidgetItem(specialization)
            first_name_item = QTableWidgetItem(first_name)
            last_name_item = QTableWidgetItem(last_name)
            phone_item = QTableWidgetItem(phone)

             # Set items in the table
            self.contractors_table.setItem(row_count, 0, specialization_item)
            self.contractors_table.setItem(row_count, 1, first_name_item)
            self.contractors_table.setItem(row_count, 2, last_name_item)
            self.contractors_table.setItem(row_count, 3, phone_item)

            # Add a combo box for actions
            action_combo_box = QComboBox()
            action_combo_box.addItems(["Property 1", "Property 2", "Property 3", "Pending"])
            action_combo_box.setCurrentText("Pending")  # Set default value to "Pending"
            self.contractors_table.setCellWidget(row_count, 4, action_combo_box)

             # Add a combo box for status
            status_combo_box = QComboBox()
            status_combo_box.addItems(["In Progress", "Complete", "Pending"])
            status_combo_box.setCurrentText("Pending")  # Set default value to "Pending"
            status_combo_box.currentTextChanged.connect(self.check_notification)  # Connect the signal to the slot
            self.contractors_table.setCellWidget(row_count, 5, status_combo_box)

            self.clear_inputs()

    def delete_contractor_from_table(self):
        """Delete the selected contractor from the table.

        Retrieves the index of the currently selected row in the contractors' table
        and removes the corresponding row from the table. 
        
        If no row is selected, a warning message will be displayed.
        """
        selected_row = self.contractors_table.currentRow()

        if selected_row >= 0:
            self.contractors_table.removeRow(selected_row)
        else:
            QMessageBox.warning(self, "Warning", "No row selected.")

    # Function to clear input fields
    def clear_inputs(self):
        """Clear all input fields.

        Clears the text in the input fields for specialization, first name, last name,
        and phone number (effectively resetting them to an empty state).
        """
        self.specialization_input.clear()
        self.first_name_input.clear()
        self.last_name_input.clear()
        self.phone_input.clear()

    # Function to check notification when status changes
    # This is for testing purpose for now
    # Need to modify to send it to notification page
    def check_notification(self, status):
        """Check for notifications based on the status

        displays a notification message if the status of a task is changed to "Complete".

        Args:
            status (str): The status of the task.
        """
        if status == "Complete":
            QMessageBox.information(self, "Task Complete", "Notification: Task is complete!")

    # Function to open recommended contractors website
    def open_recommended_contractors_website(self):
        """Open the website for recommended contractors.

        Opens a web browser to the specified website URL, which contains
        information about recommended contractors for the user to access.

        """
        # Replace 'https://example.com' with the actual website URL
        website_url = "https://example.com"
        QDesktopServices.openUrl(QUrl(website_url))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    contractor_page = Contractor_Page()
    contractor_page.show()
    sys.exit(app.exec())
