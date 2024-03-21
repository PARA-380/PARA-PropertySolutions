import sys
from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QApplication, QHBoxLayout, QMessageBox
from Property_Info_Page import Property_Info

# Define a class for the property page
class Property_Page(QMainWindow):
    def __init__(self):
        super().__init__()
        # Set window title and size
        self.setWindowTitle("Property Page")
        self.setMinimumSize(300, 200)
        
        # Create a central widget to hold the layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        # Create a vertical layout for the central widget
        self.vertical_layout = QVBoxLayout(self.central_widget)
        
        # List to keep track of created button pairs
        self.buttons = []

        # Create a button for adding properties
        self.create_button = QPushButton('Add a property', self)
        self.create_button.clicked.connect(self.create_button_clicked)
        self.vertical_layout.addWidget(self.create_button)

    # Function to handle the "Add a property" button click event
    def create_button_clicked(self):
        # Layout to contain property button and delete button
        property_layout = QHBoxLayout()
        
        # Create a property button with a label (+ 1 its len to increment number of property)
        property_button = QPushButton(f'Property {len(self.buttons) + 1}', self)

        # Call property Info Page
        property_button.clicked.connect(self.open_property_info)
        
        # Create a delete button
        delete_button = QPushButton('Delete', self)
        # Connect the delete button to the deleteProperty function
        delete_button.clicked.connect(lambda _, layout=property_layout: self.delete_property(layout))
        
        # Add property button and delete button to the layout
        property_layout.addWidget(property_button)
        property_layout.addWidget(delete_button)
        
        # Add the layout to the list of buttons
        self.buttons.append(property_layout)
        
        # Add the layout to the vertical layout of the central widget
        self.vertical_layout.addLayout(property_layout)

        # Update the labels of existing property buttons to ensure uniqueness
        for index, layout in enumerate(self.buttons):
            # enumerate: iterate over a sequence (such as a list, tuple, or string) while also keeping track of the index of each item.
            # Iterate over the list of property layouts along with their index
            # This allows us to access each layout and its corresponding index in the list

            # Get the property button widget from the layout
            # Since the property button is the first item in the layout, use index 0 to access it
            property_button = layout.itemAt(0).widget()

            # Update the text of the property button to ensure uniqueness
            # Use the current index incremented by 1 to represent the new property number
            # This ensures that each property button has a unique label reflecting its updated number
            property_button.setText(f'Property {index + 1}')

    # Function to handle deletion of a property
    def delete_property(self, layout):
        # Get the property button from the layout
        property_button = layout.itemAt(0).widget()
        # Get the text of the property button
        property_text = property_button.text()
        
        # Show a confirmation dialog
        # set the default button for the message box to be No. If the user closes the dialog without selecting an option, 
        # this default option will be chosen.
        reply = QMessageBox.question(self, 'Confirm Deletion', f"Are you sure you want to delete {property_text}?", 
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        
        # If the user confirms deletion, remove the layout and its widgets
        if reply == QMessageBox.StandardButton.Yes:
             # Loop through the items in the layout in reverse order
             # Reversing the order of the loop is necessary to ensure proper removal of widgets from the layout 
            for i in reversed(range(layout.count())):
                # Retrieve the widget at index i in the layout
                widget = layout.itemAt(i).widget()
                # Remove the widget from the layout
                layout.removeWidget(widget)
                # Delete the widget to free up memory
                widget.deleteLater()
            # Remove the layout itself from the list of button layouts
            self.buttons.remove(layout)

    # Function to open the property info page (connect with property info class)
    def open_property_info(self):
        sender_button = self.sender()  # Get the button that triggered the signal
        property_number = int(sender_button.text().split()[-1])
        # Create and show the property info window
        self.property_info_window = Property_Info()
        self.property_info_window.show()


