# from Lease import Lease
# remove above # after added Lease Class
# add lease variable in "__init__" function


class Tenant:
    # tenantName = None

    def __init__(self, firstname: str = "", lastname: str = "", ssn: str = "", address: str = "",
                 phonenumber: str = "",
                 email: str = ""):
        self.tenantID = None
        self.tenantFirstName = firstname
        self.tenantLastName = lastname
        self.tenantSSN = ssn
        self.tenantAddress = address
        self.tenantPhoneNumber = phonenumber
        self.tenantEmail = email
        # self.lease = Lease
        # self.dashboard

    def __repr__(self):
        return f"Tenant ID: {self.tenantID} - {self.tenantFirstName} {self.tenantLastName} lives at {self.tenantAddress}"
    
    def set_id(self,ID):
        self.tenantID = ID

    def get_id(self):
        return self.tenantID

    def setAddress(self, newAddress: str = None):
        self.tenantAddress = newAddress

    def set_first_name(self, name: str = None):
        self.tenantFirstName = name

    def set_last_name(self, name: str = None):
        self.tenantLastName = name

    def set_ssn(self, newSSN: str = None):
        self.tenantSSN = newSSN

    def set_phone_number(self, phoneNumber: str = None):
        self.tenantPhoneNumber = phoneNumber

    def set_email(self, email: str = None):
        self.tenantEmail = email

    def get_first_name(self):
        return self.tenantFirstName

    def get_last_name(self):
        return self.tenantLastName

    def get_name(self):
        return self.tenantFirstName + " " + self.tenantLastName

    def get_email(self):
        return self.tenantEmail

    def get_ssn(self):
        return self.tenantSSN

    def get_address(self):
        return self.tenantAddress

    def get_phone_number(self):
        return self.tenantPhoneNumber

    def to_dict(self):
        return {"Name": self.tenantFirstName + " " + self.tenantLastName, "SSN": self.tenantSSN,
                "Address": self.tenantAddress, "Phone Number": self.tenantPhoneNumber, "Email": self.tenantEmail}