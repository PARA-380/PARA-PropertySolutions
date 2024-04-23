"""
File: Property_main.py
Name: Jittapatana (Patrick) Prayoonpruk
Date: 04/05/2024
Description: Property main page user interface
Purposes: 1. To create new properties
          2. To access existed properties
          3. To delete properties
"""
import sys
from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QApplication, QHBoxLayout, QMessageBox
from .Property_Button_Controller import Property_Controller

from System import Cont_Property, Cont_Tenant


class Property_Page(QMainWindow):
    def __init__(self, cont_property : Cont_Property, cont_tenant : Cont_Tenant):
        super().__init__()
        # Set window title and size
        self.setWindowTitle("Property Page")
        self.setMinimumSize(300, 200)


        #Controllers
        self.Cont_Property = cont_property
        self.Cont_Tenant = cont_tenant

        print(f"{self.Cont_Property.getProperties()}")

        # Create a central widget to hold the layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Create a vertical layout for the central widget
        self.vertical_layout = QVBoxLayout(self.central_widget)

        # List to keep track of created button pairs
        self.buttons = []

        # Initialize set to track used property numbers
        self.used_property_numbers = set()  
        # self.property_ids = {}
    
        # Initialize Property_Controller instance
        self.property_info_controller = Property_Controller(self.Cont_Property,self.Cont_Tenant)

        # Create property buttons based on the total number of properties created
        total_properties_created = self.property_info_controller.get_total_properties_created()
        for _ in range(total_properties_created):
            self._create_property()

        # Get property numbers from controller
        property_numbers = self.property_info_controller.get_property_numbers()

        # Create property buttons based on the total number of properties created
        for property_number in property_numbers:
            self._create_property(property_number)

        self.is_setup = False
        # Create a button for adding properties
        self.add_property_layout = QHBoxLayout()  # Layout for "Add a property" button
        self.create_button = QPushButton('Add a property', self)
        self.create_button.clicked.connect(lambda:  self._create_property())
        self.add_property_layout.addWidget(self.create_button)
        self.vertical_layout.addLayout(self.add_property_layout)

        #setup the property numbers associated to which property ID
        self.setup_properties(self.Cont_Property.getProperties())

    def setup_properties(self,properties):
        for property in properties:
            self.is_setup = True
            property_number = self._get_next_available_property_number()
            self.Cont_Property.addPropertyID(property_number,property.get_property_id())
            self._create_property(property_number)
        print(f"Property Numbers{self.Cont_Property.property_IDs}")


    def _create_property(self, property_number = None):
        """_summary_
        """ 
        if not self.is_setup:
            property_number = self._get_next_available_property_number()
            newPropertyID = self.Cont_Property.createProperty()
            self.Cont_Property.addPropertyID(property_number, newPropertyID)
        self.is_setup = False
        self.used_property_numbers.add(property_number)  # Add the property number to the set of used property numbers
        self.property_info_controller.create_property_info(property_number)

        # Layout for each property button and delete button
        property_layout = QHBoxLayout()  
        property_button = QPushButton(f'Property {property_number}', self)
        property_button.clicked.connect(self._open_property_info)
        # Dynamic Properties library from PyQt
        property_button.setProperty("property_number", property_number)
        property_layout.addWidget(property_button)

        delete_button = QPushButton('Delete', self)
        delete_button.clicked.connect(lambda _, num=property_number: self._delete_property(num))
        property_layout.addWidget(delete_button)

        self.vertical_layout.addLayout(property_layout)

    def _open_property_info(self):

        property_number = self.sender().property("property_number")

        # Retrieve Property_Info instance from PropertyInfoController
        property_info = self.property_info_controller.get_property_info(property_number)
        property_info.setup_address(property_number)

        if property_info:
            property_info.setWindowTitle(f"Property {property_number} Information")
            property_info.show()

    def _delete_property(self, property_number):

        self.used_property_numbers.remove(property_number)  # Remove the deleted property number from the set of used property numbers


        # Create a QMessageBox for confirmation
        reply = QMessageBox.question(self, 'Confirm Deletion', f"Are you sure you want to delete Property {property_number}?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            # If the user confirms deletion, proceed with deletion
            self.property_info_controller.delete_property_info(property_number)
            # Find and remove the layout containing the property and delete buttons
            for i in reversed(range(self.vertical_layout.count())):
                layout_item = self.vertical_layout.itemAt(i)
                if isinstance(layout_item, QHBoxLayout):
                    property_button = layout_item.itemAt(0).widget()
                    if property_button.property("property_number") == property_number:
                        while layout_item.count():
                            item = layout_item.takeAt(0)
                            widget = item.widget()
                            if widget:
                                widget.deleteLater()
                        self.vertical_layout.removeItem(layout_item)
                        break

    def _get_next_available_property_number(self):
        property_number = 1
        while property_number in self.used_property_numbers:
            property_number += 1
        return property_number
    
    def get_property_id(self, property_number):
        return self.property_IDs[property_number]

'''
def main():
    app = QApplication(sys.argv)
    window = Property_Page()


    # Set the count of properties created for testing purposes
    count = 3
    window.property_info_controller.save_property_count(count)

    # Create properties based on the count set
    for _ in range(count):
        window._create_property()

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
'''