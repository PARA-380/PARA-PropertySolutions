import sys
# Import your database module
import src
from src import Database



class TenantsUI:
    def __init__(self):
        # Initialize your UI components here
        self.table = None  # Placeholder for your table widget

        # Call the database initialization function
        src.Database.init()

        # Call the function to read data from the database and populate the table
        self.populate_table()

    def populate_table(self):
        # Call the function from database.py to read data from the database
        data = Database.readTenants()  # Modify this according to your database schema

        # Populate your table widget with the retrieved data
        if data:
            for tenant_id, tenant_data in data.items():
                # Assuming Tenant class has a method to convert to a row of data
                row_data = tenant_data.to_dict()
                # Add each row of data to your table
                self.table.add_row(row_data)
