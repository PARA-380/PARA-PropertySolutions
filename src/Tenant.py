# from Lease import Lease
# remove above # after added Lease Class
# add lease variable in "__init__" function


class Tenant:
    # tenantName = None

    def __init__(self, ID: int = None, firstname: str = "", lastname: str = "", tenantssn: str = "",
                 tenantaddress: str = "",
                 tenantphonenumber: str = "",
                 tenantemail: str = ""):
        self.ID = ID
        self.tenantFirstName = firstname
        self.tenantLastName = lastname
        self.tenantSSN = tenantssn
        self.tenantAddress = tenantaddress
        self.tenantPhoneNumber = tenantphonenumber
        self.tenantEmail = tenantemail
        # self.lease = Lease
        # self.dashboard

    def __repr__(self):
        return f"{self.__dict__}"

    def get_ID(self):
        return self.ID

    def set_ID(self, newID):
        self.ID = newID

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