import sys
from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QApplication, QDialog, QLabel
from new_win_test import NewWindow

class Property_Page(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(300, 200)

        self.central_widget = QWidget()  # Central widget to hold the layout
        self.setCentralWidget(self.central_widget)

        self.vertical_layout = QVBoxLayout(self.central_widget)  # Vertical layout

        self.create_button = QPushButton('Create a button', self)
        self.create_button.clicked.connect(self.createButtonClicked)
        self.vertical_layout.addWidget(self.create_button)

        self.delete_button = QPushButton('Delete selected button', self)
        self.delete_button.clicked.connect(self.deleteButtonClicked)
        self.vertical_layout.addWidget(self.delete_button)

        self.buttons = []  # List to keep track of created buttons
        self.selected_button = None  # Track the currently selected button

        self.button_count = 0  # Track the count of created buttons

    def createButtonClicked(self):
        print('Clicked')
        self.button_count += 1  # Increment button count
        # Find the next available property number
        existing_properties = [int(button.text().split()[-1]) for button in self.buttons]
        next_property_number = 1
        while next_property_number in existing_properties:
            next_property_number += 1
        
        new_button = QPushButton(f'Property {next_property_number}', self)  # Set button text
        new_button.clicked.connect(lambda _, btn=new_button: self.selectButton(btn))
        new_button.clicked.connect(self.openNewWindow)  # Connect to open new window
        self.buttons.append(new_button)  # Add new button to the list
        self.vertical_layout.addWidget(new_button)  # Add new button to the layout
        new_button.show()

    def deleteButtonClicked(self):
        if self.selected_button is not None:
            self.buttons.remove(self.selected_button)
            self.selected_button.deleteLater()
            self.selected_button = None

    def selectButton(self, button):
        if self.selected_button is not None:
            self.selected_button.setStyleSheet("")  # Reset style of previously selected button
        self.selected_button = button
        button.setStyleSheet("background-color: grey")  # Highlight selected button

    def openNewWindow(self):
        if self.selected_button is not None:
            property_number = int(self.selected_button.text().split()[-1])
            new_window = NewWindow(property_number)
            new_window.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = Property_Page()
    mainWin.show()
    sys.exit(app.exec())
