# from Lease import Lease
# remove above # after added Lease Class
# add lease variable in "__init__" function


class Tenant:
    # tenantName = None

    def __init__(self, ten_ID : int = None, firstname: str = "", lastname: str = "", ssn: str = "", address: str = "",
                 phonenumber: str = "",
                 email: str = ""):
        self.tenantID = ten_ID
        self.accountID = None
        self.propertyID = None
        self.tenantFirstName = firstname
        self.tenantLastName = lastname
        self.tenantSSN = ssn
        self.tenantAddress = address
        self.tenantPhoneNumber = phonenumber
        self.tenantEmail = email
        # self.lease = Lease
        # self.dashboard

    def __repr__(self):
        return f"""Tenant ID: {self.tenantID} \n 
        {self.tenantFirstName} {self.tenantLastName} \n 
        Address: {self.tenantAddress}\n
        Account: {self.accountID}\n
        SSN: {self.tenantSSN}\n
        Email: {self.tenantEmail}\n
        Phone: {self.tenantPhoneNumber}\n"""
    
    def setID(self,ID):
        self.tenantID = ID

    def getID(self):
        return self.tenantID
    
    def get_account_id(self):
        return self.accountID
    
    def _set_account_id(self, accID):
        self.accountID = accID

    def set_property_id(self, prop_id):
        self.propertyID = prop_id

    def get_property_id(self):
        return self.propertyID

    def setAddress(self, newAddress: str = None):
        self.tenantAddress = newAddress

    def setFirstName(self, name: str = None):
        self.tenantFirstName = name

    def setLastName(self, name: str = None):
        self.tenantLastName = name

    def setSSN(self, newSSN: str = None):
        self.tenantSSN = newSSN

    def setPhoneNumber(self, phoneNumber: str = None):
        self.tenantPhoneNumber = phoneNumber

    def setEmail(self, email: str = None):
        self.tenantEmail = email

    def saveData(self):
        #TODO: Overwrite to Database
        pass

    def getFirstName(self):
        return self.tenantFirstName

    def getLastName(self):
        return self.tenantLastName

    def getName(self):
        return self.tenantFirstName + " " + self.tenantLastName

    def getEmail(self):
        return self.tenantEmail

    def getSSN(self):
        return self.tenantSSN

    def getAddress(self):
        return self.tenantAddress

    def getPhoneNumber(self):
        return self.tenantPhoneNumber

    def to_dict(self):
        return {"Name": self.tenantFirstName + " " + self.tenantLastName, "SSN": self.tenantSSN,
                "Address": self.tenantAddress, "Phone Number": self.tenantPhoneNumber, "Eamil": self.tenantEmail}

# tenant = Tenant("Ridham", "123-45-6789", "Home Address", "(012) 345 - 6789", "ridham.patel@email.com")
# tenant.toJSON()
