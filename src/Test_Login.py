import unittest
from unittest.mock import MagicMock, call
from src.Login_Page import Login_Page
from src.Cont_Login import Cont_Login
from PyQt6.QtWidgets import QApplication

class TestLogIn(unittest.TestCase):
    def setUp(self):
        # Create a QApplication instance before setting up the GUI elements
        self.app = QApplication([])
        # Create an instance of YourClass
        self.instance = Login_Page(Cont_Login)
        # Mock the dependencies
        self.instance.username_line_edit = MagicMock()
        self.instance.password_line_edit = MagicMock()
        self.instance.cont_login = MagicMock()
        # Mock the close method
        self.instance.close = MagicMock()

    def tearDown(self):
        # Clean up the QApplication instance after each test
        self.app.deleteLater()

    def test_log_in_success(self):
        # Configure mock objects to return desired values
        self.instance.username_line_edit.text.return_value = "username"
        self.instance.password_line_edit.text.return_value = "password"
        self.instance.cont_login.validateLogin.return_value = True

        # Call the method to be tested
        self.instance.log_in()

        # Check if log in was successful
        self.assertTrue(self.instance.is_login)
        # Check if close method should have been called (as it's part of success scenario)
        self.instance.close.assert_called_once()

    def test_log_in_failure(self):
        # Configure mock objects to return desired values
        self.instance.username_line_edit.text.return_value = "username"
        self.instance.password_line_edit.text.return_value = "password"
        self.instance.cont_login.validateLogin.return_value = False

        # Call the method to be tested
        self.instance.log_in()

        # Check if log in failed
        self.assertFalse(self.instance.is_login)
        # Check if close method should not have been called (as it's part of success scenario)
        self.instance.close.assert_not_called()

if __name__ == '__main__':
    unittest.main()
