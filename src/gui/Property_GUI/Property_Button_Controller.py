"""
File: Property_Button_Controller.py
Name: Jittapatana (Patrick) Prayoonpruk
Date: 04/07/2024
Description: The controller that communicates between Property_main and Property_info
Purposes: To keep track of how many property the user has created
          To create a property info page according to the property button
Data Structure: List and Dictionary
"""

# Import Property_Info class
from .Property_Info_Page import Property_Info
from System import Cont_Property, Cont_Tenant

class Property_Controller:
    """Property_Controller class manages communication between Property_main and Property_info.

    Attributes:
        property_info_pages (dict): A dictionary to store Property_Info instances, with property numbers as keys.
        total_properties_created (int): A counter to keep track of the total properties created.
        property_numbers (list): A list to store the property numbers.
    """
    def __init__(self, cont_property: Cont_Property, cont_tenant : Cont_Tenant):
        self.property_info_pages = {}  # Dictionary to store Property_Info instances
        self.total_properties_created = 0  # Counter to keep track of total properties created
        self.property_numbers = []  # List to store the property numbers
        self.Cont_Property = cont_property
        self.Cont_Tenant = cont_tenant

    def create_property_info(self, property_number):
        """Creates a Property_Info instance for the given property number and stores it in the dictionary.

        Args:
            property_number (int): The unique identifier for the property.
        """
        print(f"CREATED PROPERTY {property_number}")

        # Create an instance of Property_Info for the given property number
        property_info = Property_Info(property_number=property_number,tenant_controller=self.Cont_Tenant, property_controller=self.Cont_Property)
        # Store the instance in the dictionary
        self.property_info_pages[property_number] = property_info
        # Increment the total properties created counter
        self.total_properties_created += 1

        #do some one-time setup stuff
        property_info.setup_tenants()

    def get_property_info(self, property_number):
        """Retrieves the Property_Info instance for the given property number.

        Args:
            property_number (int): The unique identifier for the property.

        Returns:
            Property_Info or None: The Property_Info instance associated with the property number, or None if not found.
        """
        # Retrieve Property_Info instance for the given property number
        info_page = self.property_info_pages.get(property_number)
        # info_page.setup_address(property_number)
        return info_page

    def delete_property_info(self, property_number):
        """Deletes the Property_Info instance for the given property number from the dictionary.

        Args:
            property_number (int): The unique identifier for the property.
        """
        # Delete Property_Info instance for the given property number
        if property_number in self.property_info_pages:
            del self.property_info_pages[property_number]
            # Decrement the total properties created counter
            self.total_properties_created -= 1
        self.Cont_Property.deleteProperty(property_number)

    def get_total_properties_created(self):
        """Retrieves the total number of properties created.

        Returns:
            int: The total number of properties created.
        """
        return self.total_properties_created

    def get_property_numbers(self):
        """Retrieves the list of property numbers.

        Returns:
            list: The list of property numbers.
        """
        return self.property_numbers
    
    def save_property_count(self, count):
        """Saves the total number of properties created.

        Args:
            count (int): The total number of properties created.
        """
        self.total_properties_created = count

    def save_new_property(self, property_info):
        """Saves the newly created property information to the database.

        Args:
            property_info (Property_Info): The Property_Info instance containing the property information.

        Returns:
            int: The property number.
        """
        # Retrieve property information from the Property_Info instance
        property_number = property_info.get_property_number()
        print("property_id: ", property_number)
        address = property_info.get_address_label()
        # Save property information to the database
        property_number = self.save_property_info_to_database(property_number, address)

        return property_number
    
    def save_property_info_to_database(self, property_number, address):
        """Saves the property information to the database.

        Args:
            property_number (int): The unique identifier for the property.
            address (str): The address of the property.

        Returns:
            int: The property number.
        """
        # need to implement saving property information to the database here
        # For demonstration purposes, let's just print the property information
        print("Saving Property to Database:")
        print("Property Number:", property_number)
        print("Address:", address)

        # need to replace this with actual database interaction code
        # Example:
        # property_id = addToProperty(property_number, address)

        # For demonstration purposes, returning the same property number
        return property_number