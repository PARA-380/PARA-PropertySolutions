"""
File: Contractor.py
Name: Jittapatana Prayoonpruk
Date: 04/27/24
Description: Handles Contractor attributes
Purposes: Creates a basis for a Contractor and its attributes.  Attributes get handled by its controller.
"""

class Contractor:
    def __init__(self, accID : int = None, ID : int = None, specialization: str = "", firstname: str = "", lastname: str = "", phonenumber: str = "",):
        self.accID = accID
        self.contractor_id = ID
        self.contractor_specialization = specialization
        self.contractor_firstname = firstname
        self.contractor_lastname = lastname
        self.contractor_phone = phonenumber

    def __repr__(self):
        return f"""contractor ID: {self.contractor_id} \n
        {self.contractor_firstname} {self.contractor_lastname} \n
        phone-number: {self.contractor_phone} \n"""

    def get_first_name(self):
        """get contractor's first name

        Returns:
            string: contractor's first name
        """
        return self.contractor_firstname
    
    def get_last_name(self):
        """get contractor's last name

        Returns:
            string: contractor's last name
        """
        return self.contractor_lastname
    
    def get_specialization(self):
        """get contractor's specialization

        Returns:
            string: contractor's specialization
        """
        return self.contractor_specialization
    
    def get_phone_number(self):
        """get contractor's phone number

        Returns:
            string: contractor's phone number
        """
        return self.contractor_phone
    
    def get_contractor_id(self):
        """get contractor's ID

        Returns:
            int: contractor's ID
        """
        return self.contractor_id
    
    def set_id(self, id):
        """set contractor's ID

        Args:
            id (int): contractor's ID
        """
        self.contractor_id = id