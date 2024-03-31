
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from Property_main import Property_Page

app = QApplication(sys.argv)

# Set the number of properties for the custom property page
property_count = 3

# Create an instance of the property page with the specified number of properties
# window = Property_Page._with_property_count(property_count)

window = Property_Page()

window.show()
app.exec()
