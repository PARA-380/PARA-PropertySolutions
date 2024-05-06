"""
File: Property.py
Name: Adrian Carreno, Ali Maamoun
Date: 04/23/24
Description: Handles Property attributes
Purposes: Creates a basis for a property and its attributes.  Attributes get handled by its controller.
Property is owned by an Account which holds tenants.
"""

from .Tenant import Tenant


class Property:
    def __init__(self, property_id: int = None, accID : int  = None, address: str = "", tenants: dict = {}, sqft: str = "", home_type: str = "",
                 max_living: int = None, link_images: str = None):
        """
        Defines Property variables
        @param property_id:
        @param accID:
        @param address:
        @param tenants:
        @param sqft:
        @param home_type:
        @param max_living:
        """
        self.property_id = property_id
        self.account_id = accID
        self.address = address
        self.tenants = tenants
        self.sqft = sqft
        self.home_type = home_type
        self.max_living = max_living
        self.link_images = link_images

    def __repr__(self):
        return f"{self.property_id}, {self.address}"

    def get_account_id(self):
        return self.account_id

    def get_property_id(self):
        """
        Returns Property ID
        @return:
        """
        return self.property_id

    def set_property_id(self, newId):
        """
        Sets Property ID
        @param newId:
        @return:
        """
        self.property_id = newId

    def get_address(self):
        """
        Returns Property Address
        @return:
        """
        return self.address

    def set_address(self, address):
        """
        Sets Address
        @param address:
        @return:
        """
        self.address = address

    def get_sqft(self):
        """
        Returns the Square Footage of the Property
        @return:
        """
        return self.sqft

    def set_sqft(self, sqft):
        """
        Sets the Square Footage for the Property
        @param sqft:
        @return:
        """
        self.sqft = sqft

    def get_home_type(self):
        """
        Returns Home Type of the Property (House, Apartment, Condo, etc...)
        @return:
        """
        return self.home_type

    def set_home_type(self, home):
        """
        Sets Home Type of the Property (House, Apartment, Condo, etc...)
        @param home:
        @return:
        """
        self.home_type = home

    def get_max_living(self):
        """
        Returns the Number of people that can live in the Property
        @return:
        """
        return self.max_living

    def set_max_living(self, num):
        """
        Sets the Number of people that can live in the Property
        @param num:
        @return:
        """
        self.max_living = num

    def get_tenants(self):
        return self.tenants
    
    def add_tenant_to_property(self, tenant: Tenant):
        """
        Adds Tenants to specified property
        @param tenant:
        @return:
        """
        self.tenants.update({tenant.get_ID(): tenant})

    def remove_tenant_from_property(self, key:int):
        """
        Removes tenants from specified property
        @param key:
        @return:
        """
        self.tenants.pop(key)

    def get_link_images(self):
        return self.link_images
    
    def set_link_images(self, link):
        self.link_images = link


def main() -> None:
    pass


if __name__ == "__main__":
    pass
