import unittest
from PyQt6.QtWidgets import QApplication, QPushButton, QMessageBox, QHBoxLayout, QVBoxLayout

# Import the testing class 
from src.gui.Property_GUI.Property_main import Property_Page

class Test_Property_Main(unittest.TestCase):

    def setUp(self):
        """Set up the test fixture."""
        self.app = QApplication([])
        self.window = Property_Page()

    def tearDown(self):
        """Tear down the test fixture."""
        self.window.close()

    def test_create_property(self):
        """Test creating a new property."""
        initial_count = self.window.property_info_controller.get_total_properties_created()
        
        # Simulate button click
        create_button = self.window.create_button
        create_button.click()
        
        new_count = self.window.property_info_controller.get_total_properties_created()
        
        # Check if the count increased by one
        self.assertEqual(new_count, initial_count + 1)

    def test_delete_property(self):
        """Test deleting a property."""
        # Add a property to delete
        self.window.create_property()
        initial_count = self.window.property_info_controller.get_total_properties_created()
        
        # Find the delete button of the property
        delete_button = None
        for index in range(self.window.vertical_layout.count()):
            layout_item = self.window.vertical_layout.itemAt(index)
            if layout_item and isinstance(layout_item, QHBoxLayout):
                delete_button_item = layout_item.itemAt(1)  # Assuming delete button is at index 1
                if delete_button_item:
                    delete_button = delete_button_item.widget()
                    break
        
        if delete_button:
            # Delete the property
            self.window.delete_property(1)  # Assuming the property number is 1
            
            new_count = self.window.property_info_controller.get_total_properties_created()
            
            # Check if the count decreased by one
            self.assertEqual(new_count, initial_count - 1)
        else:
            self.fail("Delete button not found.")

if __name__ == "__main__":
    unittest.main()