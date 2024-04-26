

class Contractor:
    def __init__(self, ID : int = None, specialization: str = "", firstname: str = "", lastname: str = "", phonenumber: str = "",):
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
        return self.contractor_firstname
    
    def get_last_name(self):
        return self.contractor_lastname
    
    def get_specialization(self):
        return self.contractor_specialization
    
    def get_phone_number(self):
        return self.contractor_phone
    
    def get_contractor_id(self):
        return self.contractor_id