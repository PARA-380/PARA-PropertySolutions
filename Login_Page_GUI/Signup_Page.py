import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class SignUp_Page(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sign Up")
        self.setGeometry(200, 200, 300, 200)

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
        email = self.email_edit.text()
        password = self.password_edit.text()
        confirm_password = self.confirm_password_edit.text()

        if password != confirm_password:
            QMessageBox.warning(self, "Error", "Passwords do not match.")
            return

        # add code to store the email and password, for example in a database.
        # Print them for testing purpose
        print("Email:", email)
        print("Password:", password)
        print("Sign up successful.")

        # Close the sign-up page after successful sign-up
        self.close() 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SignUp_Page()
    window.show()
    sys.exit(app.exec())