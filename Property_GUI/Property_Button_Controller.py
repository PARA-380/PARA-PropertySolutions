# Import Property_Info class
from Property_GUI.Property_Info_Page import Property_Info

class Property_Controller:
    def __init__(self):
        self.property_info_pages = {}  # Dictionary to store Property_Info instances
        self.total_properties_created = 0  # Counter to keep track of total properties created
        self.property_numbers = []  # List to store the property numbers

    def create_property_info(self, property_number):
        # Create an instance of Property_Info for the given property number
        property_info = Property_Info(property_number=property_number)
        # Store the instance in the dictionary
        self.property_info_pages[property_number] = property_info
        # Increment the total properties created counter
        self.total_properties_created += 1

    def get_property_info(self, property_number):
        # Retrieve Property_Info instance for the given property number
        return self.property_info_pages.get(property_number)

    def delete_property_info(self, property_number):
        # Delete Property_Info instance for the given property number
        if property_number in self.property_info_pages:
            del self.property_info_pages[property_number]
            # Decrement the total properties created counter
            self.total_properties_created -= 1

    def get_total_properties_created(self):
        return self.total_properties_created

    def get_property_numbers(self):
        return self.property_numbers
    
    def save_property_count(self, count):
        self.total_properties_created = count

'''
    def save_address_controller(self, property_number, address):
        # Save the address associated with the property number
        self.property_addresses[property_number] = address

    def get_address(self, property_number):
        # Retrieve the address associated with the property number
        return self.property_addresses.get(property_number)
'''