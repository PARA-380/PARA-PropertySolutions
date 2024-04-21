# Import Property_Info class
from .Property_Info_Page import Property_Info

from System import Cont_Property, Cont_Tenant

class Property_Controller:
    def __init__(self, controller_property : Cont_Property, controller_tenant : Cont_Tenant):
        self.property_info_pages = {}  # Dictionary to store Property_Info instances
        self.total_properties_created = 0  # Counter to keep track of total properties created
        self.property_db_id = {}  # List to store the property numbers
        

        #DB Controllers
        self.Cont_Property = controller_property
        self.Cont_Tenant = controller_tenant
        
        #sets existing properties to GUI
        self.read_existing_properties()

    def read_existing_properties(self):
        properties = self.Cont_Property.getProperties()
        for property in properties:
            self.property_db_id[self.total_properties_created + 1] = property.get_property_id()
            self.total_properties_created += 1


    def create_property_info(self, property_number):
        # Create an instance of Property_Info for the given property number
        propertyID = self.property_db_id[property_number]
        property_info = Property_Info(property_number=property_number, property_ID=propertyID, controller_tenant=self.Cont_Tenant, controller_property=self.Cont_Property)
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
        return self.property_db_id
    
    def save_property_count(self, count):
        self.total_properties_created = count

    def save_new_property(self, property_info):
        # Retrieve property information from the Property_Info instance
        property_id = property_info.get_property_number()
        print("property_id: ", property_id)
        address = property_info.get_address_label()
        # Save property information to the database
        property_id = self.save_property_info_to_database(property_id, address)

        return property_id
    
    def save_property_info_to_database(self, property_number, address):
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