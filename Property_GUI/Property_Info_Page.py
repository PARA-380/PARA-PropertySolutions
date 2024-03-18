from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QHBoxLayout, QMessageBox, QComboBox
)
from PyQt6.QtCore import Qt
import sys

class Property_Info(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.setWindowTitle("Property Information")

        central_widget = QWidget()  # Create a central widget
        self.setCentralWidget(central_widget)  # Set the central widget

        layout = QVBoxLayout()  # Main layout
        central_widget.setLayout(layout)

        # Address Input
        address_layout = QHBoxLayout()
        layout.addLayout(address_layout)

        self.address_input = QLineEdit()
        self.address_input.setPlaceholderText("Enter Address")
        address_layout.addWidget(self.address_input)

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_address)
        address_layout.addWidget(save_button)

        # Address Label
        self.address_label = QLabel()
        layout.addWidget(self.address_label)

        # Input Widgets
        input_layout = QHBoxLayout()
        layout.addLayout(input_layout)

        self.description_input = QLineEdit()
        self.description_input.setPlaceholderText("Description")
        self.description_input.setFixedWidth(150)
        input_layout.addWidget(self.description_input)

        self.price_input = QLineEdit()
        self.price_input.setPlaceholderText("Price")
        self.price_input.setFixedWidth(100)
        input_layout.addWidget(self.price_input)

        # Tenant dropdown list
        self.tenant_dropdown = QComboBox()
        self.tenant_dropdown.addItems(["Tenant 1", "Tenant 2", "Tenant 3"])  # Add your tenant names here
        input_layout.addWidget(self.tenant_dropdown)

        # Buttons
        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)

        add_button = QPushButton("Add Description")
        add_button.clicked.connect(self.add_property_to_table)
        button_layout.addWidget(add_button)

        delete_button = QPushButton("Delete Selected Description")
        delete_button.clicked.connect(self.delete_property_from_table)
        button_layout.addWidget(delete_button)

        add_tenant_button = QPushButton("Add Tenant")
        add_tenant_button.clicked.connect(self.add_tenant_to_table)
        button_layout.addWidget(add_tenant_button)

        delete_tenant_button = QPushButton("Delete Selected Tenant")
        delete_tenant_button.clicked.connect(self.delete_tenant_from_table)
        button_layout.addWidget(delete_tenant_button)

        # Tables
        tables_layout = QHBoxLayout()
        layout.addLayout(tables_layout)

        # Property Details Table
        self.property_table = QTableWidget()
        self.property_table.setColumnCount(2)
        self.property_table.setHorizontalHeaderLabels(["Description", "Price"])
        tables_layout.addWidget(self.property_table)

        # Tenants Table
        self.tenants_table = QTableWidget()
        self.tenants_table.setColumnCount(2)
        self.tenants_table.setHorizontalHeaderLabels(["Tenant Name", "Contact"])
        tables_layout.addWidget(self.tenants_table)

        # See Pie Chart Button
        see_pie_chart_button = QPushButton("See Pie Chart")
        see_pie_chart_button.clicked.connect(self.see_pie_chart)
        layout.addWidget(see_pie_chart_button)

    def add_property_to_table(self):
        description = self.description_input.text()
        price = self.price_input.text()

        if description and price:
            row_count = self.property_table.rowCount()
            self.property_table.setRowCount(row_count + 1)

            description_item = QTableWidgetItem(description)
            price_item = QTableWidgetItem(price)

            self.property_table.setItem(row_count, 0, description_item)
            self.property_table.setItem(row_count, 1, price_item)

            self.clear_inputs()

    def delete_property_from_table(self):
        selected_row = self.property_table.currentRow()
        if selected_row >= 0:
            self.property_table.removeRow(selected_row)
        else:
            QMessageBox.warning(self, "Warning", "No row selected.")

    def add_tenant_to_table(self):
        tenant_name = self.tenant_dropdown.currentText()
        # Here you would retrieve other details of the tenant using the selected name,
        # and add them to the table. For simplicity, I'm just adding the name.
        if tenant_name:
            row_count = self.tenants_table.rowCount()
            self.tenants_table.setRowCount(row_count + 1)

            name_item = QTableWidgetItem(tenant_name)
            # You can add other details here if needed

            self.tenants_table.setItem(row_count, 0, name_item)
            # Set other details in subsequent columns if needed

    def delete_tenant_from_table(self):
        selected_row = self.tenants_table.currentRow()
        if selected_row >= 0:
            self.tenants_table.removeRow(selected_row)
        else:
            QMessageBox.warning(self, "Warning", "No row selected.")

    def clear_inputs(self):
        self.description_input.clear()
        self.price_input.clear()

    def save_address(self):
        address = self.address_input.text()
        self.address_label.setText(f"Address: {address}")

    # If have time
    def see_pie_chart(self):
        # Code to show pie chart
        pass

