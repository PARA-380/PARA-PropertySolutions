"""
File: Noti_Page_GUI.py
Name: Jittapatana (Patrick) Prayoonpruk
Date: 04/12/2024
Description: Notification Page user interface
Purposes: To see the notification regarding the maintenance
"""
import sys
from PyQt6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QTableWidget, 
    QTableWidgetItem, 
    QVBoxLayout, 
    QWidget, 
    QHeaderView, 
    QPushButton, 
    QHBoxLayout,
    QMessageBox)

class Notification_Page(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Notifications")

        # Set window size
        self.resize(600, 400)

        # Create central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Create delete button
        self.delete_button = QPushButton("Delete Selected Row")
        self.delete_button.clicked.connect(self.delete_selected_row)

        # Create layout for the delete button
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.delete_button)
    
        
        # Create table widget
        self.notification_table = QTableWidget()
        self.notification_table.setColumnCount(2)  # Two columns: Number of notifications and Description
        
        # Set table headers
        self.notification_table.setHorizontalHeaderLabels(["No", "Description"])
        # Set header to stretch for the description column
        header = self.notification_table.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        
        # Populate table with sample data (replace this with your actual notification data)
        self.populate_notifications()
        # Set layout
        layout = QVBoxLayout()

        # Add the delete button to the layout
        layout.addLayout(button_layout)

        # Add the table widget to the layout
        layout.addWidget(self.notification_table)

        self.central_widget.setLayout(layout)
        self.central_widget.setLayout(layout)
        
    
    def populate_notifications(self):
        # Sample notification data for testing purpose
        notifications = [
            {"count": 3, "description": "New messages received"},
            {"count": 1, "description": "Property 1: task coding is complete by Patrick"},
            {"count": 0, "description": "Property 2 : Task chilling is complete by Person"}
        ]
        
        # Set row count in the table
        self.notification_table.setRowCount(len(notifications))
        
        # Populate table with data
        for row, notification in enumerate(notifications):
            count_item = QTableWidgetItem(str(notification["count"]))
            description_item = QTableWidgetItem(notification["description"])
            self.notification_table.setItem(row, 0, count_item)
            self.notification_table.setItem(row, 1, description_item)

    def delete_selected_row(self):
            selected_row = self.notification_table.currentRow()
            if selected_row >= 0:
                confirmation = QMessageBox.question(self, "Confirm Deletion", "Are you sure you want to delete this notification?",
                                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                if confirmation == QMessageBox.StandardButton.Yes:
                    self.notification_table.removeRow(selected_row)
            else:
                QMessageBox.information(self, "No Row Selected", "Please select a row to delete.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    notification_window = Notification_Page()
    notification_window.show()
    sys.exit(app.exec())
