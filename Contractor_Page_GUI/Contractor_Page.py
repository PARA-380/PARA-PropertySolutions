from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QHBoxLayout, QMessageBox, QComboBox
)
from PyQt6.QtCore import Qt
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QDesktopServices  
import sys

# Define a class for the Contractor Page
class Contractor_Page(QMainWindow):
    def __init__(self):
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

        # Create input fields for name
        self.name_input = QLineEdit()  
        self.name_input.setPlaceholderText("Name")
        input_layout.addWidget(self.name_input)

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
        self.contractors_table.setColumnCount(5)  
        self.contractors_table.setHorizontalHeaderLabels(["Specialization", "Name", "Phone Number", "Action", "Status"])  
        layout.addWidget(self.contractors_table)

        # Button for recommended contractors
        recommended_button = QPushButton("Recommended Contractors")
        recommended_button.clicked.connect(self.open_recommended_contractors_website)
        layout.addWidget(recommended_button)

    # Function to add a contractor to the table
    def add_contractor_to_table(self):
        specialization = self.specialization_input.text()
        name = self.name_input.text()
        phone = self.phone_input.text()

         # Check if all fields are filled
        if specialization and name and phone:
            row_count = self.contractors_table.rowCount()
            self.contractors_table.setRowCount(row_count + 1)

            # Create table items for specialization, name, and phone number
            specialization_item = QTableWidgetItem(specialization)
            name_item = QTableWidgetItem(name)
            phone_item = QTableWidgetItem(phone)

             # Set items in the table
            self.contractors_table.setItem(row_count, 0, specialization_item)
            self.contractors_table.setItem(row_count, 1, name_item)
            self.contractors_table.setItem(row_count, 2, phone_item)

            # Add a combo box for actions
            action_combo_box = QComboBox()
            action_combo_box.addItems(["Task 1", "Task 2", "Task 3", "Pending"])
            action_combo_box.setCurrentText("Pending")  # Set default value to "Pending"
            self.contractors_table.setCellWidget(row_count, 3, action_combo_box)

             # Add a combo box for status
            status_combo_box = QComboBox()
            status_combo_box.addItems(["In Progress", "Complete", "Pending"])
            status_combo_box.setCurrentText("Pending")  # Set default value to "Pending"
            status_combo_box.currentTextChanged.connect(self.check_notification)  # Connect the signal to the slot
            self.contractors_table.setCellWidget(row_count, 4, status_combo_box)

            self.clear_inputs()

    # Function to delete a contractor from the table
    def delete_contractor_from_table(self):
        selected_row = self.contractors_table.currentRow()

        if selected_row >= 0:
            self.contractors_table.removeRow(selected_row)
        else:
            QMessageBox.warning(self, "Warning", "No row selected.")

    # Function to clear input fields
    def clear_inputs(self):
        self.specialization_input.clear()
        self.name_input.clear()
        self.phone_input.clear()

    # Function to check notification when status changes
    # This is for testing purpose for now
    # Need to modify to send it to notification page
    def check_notification(self, status):
        if status == "Complete":
            QMessageBox.information(self, "Task Complete", "Notification: Task is complete!")

    # Function to open recommended contractors website
    def open_recommended_contractors_website(self):
        # Replace 'https://example.com' with the actual website URL
        website_url = "https://example.com"
        QDesktopServices.openUrl(QUrl(website_url))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    contractor_page = Contractor_Page()
    contractor_page.show()
    sys.exit(app.exec())
