"""
File: Signup_Page.py
Name: Jittapatana (Patrick) Prayoonpruk
Date: 04/19/2024
Description: Sign up page user interface
Purposes: To create a new account in order to sign in into the application
"""
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

from src.Cont_Login import Cont_Login

class SignUp_Page(QWidget):
    """Represents the sign-up page for new users

    Provides a user interface for users to create a new account by entering
    their email address, password, and confirming the password.

    Args:
        QWidget (QWidget): The base class for UI object in PyQt6
    """
    def __init__(self, cont_login : Cont_Login):
        """Initialize the SignUp_Page instance.

        Args:
            cont_login (Cont_Login): An instance of the Cont_Login class, which handles 
                the connection between user interface, entity class, and System (database).
        """
        super().__init__()
        self.setWindowTitle("Sign Up")
        self.setGeometry(200, 200, 300, 200)

        self.Cont_Login = cont_login

        self.email_label = QLabel("Email:")
        self.email_edit = QLineEdit()
        self.password_label = QLabel("Password:")
        self.password_edit = QLineEdit()
        # setEchomode: Blackdots
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.confirm_password_label = QLabel("Confirm Password:")
        self.confirm_password_edit = QLineEdit()
        self.confirm_password_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.sign_up_button = QPushButton("Sign Up")
        self.sign_up_button.clicked.connect(self.sign_up)

        layout = QVBoxLayout()
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_edit)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_edit)
        layout.addWidget(self.confirm_password_label)
        layout.addWidget(self.confirm_password_edit)
        layout.addWidget(self.sign_up_button)

        self.setLayout(layout)

    def sign_up(self):
        """Process the sign-up action

        Retrieves the email address, password, and confirmed password from the input fields.
        Checks if the entered password matches the confirmed password.
        Closes the sign-up page after successful sign-up.
        """
        email = self.email_edit.text()
        password = self.password_edit.text()
        confirm_password = self.confirm_password_edit.text()

        if password != confirm_password:
            QMessageBox.warning(self, "Error", "Passwords do not match.")
            return

        # add code to store the email and password to the database.
        # Print them for testing purpose
        print("Email:", email)
        print("Password:", password)
        print("Sign up successful.")
        self.Cont_Login.createAccount(username=email,password=password)

        # Close the sign-up page after successful sign-up
        self.close() 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SignUp_Page()
    window.show()
    sys.exit(app.exec())