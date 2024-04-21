"""
File: Setting_Page_GUI.py
Name: Jittapatana (Patrick) Prayoonpruk
Date: 04/12/2024
Description: Setting page user interface
Purposes: 1. To delete an account permanently
          2. To provide contact for IT and other supports
"""
import sys
from PyQt6.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout, QLabel, QMessageBox

class Setting_Page(QDialog):
    """Represents the settings page for IT support information

    Provides options for deleting the user account permanently.

    Args:
        QDialog (QDialog): The base class for dialog windows in PyQt6.
    """
    def __init__(self):
        """Initialize the Setting_Page instance
        """
        super().__init__()
        self.setWindowTitle("Settings")
        
        # Create widgets
        self.delete_button = QPushButton("Delete Account")
        self.delete_button.clicked.connect(self.show_delete_warning)
        
        self.contact_label = QLabel("Help & Support: Please contact PARA.PropertySolution@gmail.com")
        
        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.delete_button)
        layout.addWidget(self.contact_label)
        
        self.setLayout(layout)
    
    def show_delete_warning(self):
        """Display a warning message box for confirming account deletion.
        """
        # Show a warning message box
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Delete Account")
        msg_box.setText("Are you sure you want to delete your account?")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg_box.setDefaultButton(QMessageBox.StandardButton.No)
        
        # Execute the message box and check the result
        result = msg_box.exec()
        if result == QMessageBox.StandardButton.Yes:
            self.delete_account()
    
    def delete_account(self):
        """Delete the user account permanently
        """
        # Implement delete account functionality here
        print("Account deleted successfully!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Setting_Page()
    dialog.exec()
    sys.exit(app.exec())
