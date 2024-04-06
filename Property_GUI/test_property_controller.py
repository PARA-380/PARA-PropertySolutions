from Property_GUI.Property_Button_Controller import Property_Controller
from Property_GUI.Property_Info_Page import Property_Info

import sys
from PyQt6.QtWidgets import QApplication

def main():
    # Create a QApplication instance
    app = QApplication(sys.argv)

    # Create an instance of the Property_Controller class
    property_controller = Property_Controller()

    # Create an instance of the Property_Info class with sample property information
    property_info = Property_Info(property_number=1)
    

    # Save the property information to the database
    property_controller.save_new_property_db(property_info)

    # Execute the application's event loop
    # sys.exit(app.exec())

if __name__ == "__main__":
    main()