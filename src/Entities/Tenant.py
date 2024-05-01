"""
File: Tenant.py
Name: Adrian Carreno, Ali Maamoun
Date: 04/23/24
Description: Handles Tenant attributes
Purposes: Creates a basis for a Tenant and its attributes.  Attributes get handled by its controller.
Tenant will reside in Account's Property.
"""


# from Lease import Lease
# remove above # after added Lease Class
# add lease variable in "__init__" function


class Tenant:
    # tenantName = None

    def __init__(self, ten_ID : int = None, acc_id : int = None, prop_id : int = None, firstname: str = "", lastname: str = "", ssn: str = "", address: str = "",
                 phonenumber: str = "",
                 email: str = ""):
        """
        Defines parameters for Tenant Class
        @param ID:
        @param firstname:
        @param lastname:
        @param ssn:
        @param address:
        @param phonenumber:
        @param email:
        """
        self.tenantID = ten_ID
        self.accountID = acc_id
        self.propertyID = prop_id
        self.tenantFirstName = firstname
        self.tenantLastName = lastname
        self.tenantSSN = ssn
        self.tenantAddress = address
        self.tenantPhoneNumber = phonenumber
        self.tenantEmail = email
        # self.lease = Lease
        # self.dashboard

    def __repr__(self):
        """
        Specifies how class will be printed
        @return:
        """
        return f"""Tenant ID: {self.tenantID} \n 
        {self.tenantFirstName} {self.tenantLastName} \n 
        Address: {self.propertyID}: {self.tenantAddress}\n
        Account: {self.accountID}\n
        SSN: {self.tenantSSN}\n
        Email: {self.tenantEmail}\n
        Phone: {self.tenantPhoneNumber}\n"""
    
    def setID(self,ID):
        """
        Sets Tenant ID
        @param ID:
        @return:
        """
        self.tenantID = ID

    def getID(self):
        """
        Returns Tenant ID
        @return:
        """
        return self.tenantID
    
    def get_account_id(self):
        """
        Gets the Account ID that is associated with the tenant
        @return:
        """
        return self.accountID
    
    def _set_account_id(self, accID):
        """
        Sets the Account ID that is associated with the tenant
        @param accID:
        @return:
        """
        self.accountID = accID

    def set_property_id(self, prop_id):
        self.propertyID = prop_id

    def get_property_id(self):
        return self.propertyID

    def setAddress(self, newAddress: str = None):
        """
        Associates Property address with tenant
        @param newAddress:
        @return:
        """
        self.tenantAddress = newAddress

    def setFirstName(self, name: str = None):
        """
        Sets First name of the tenant
        @param name:
        @return:
        """
        self.tenantFirstName = name

    def setLastName(self, name: str = None):
        """
        Sets Last Name of the Tenant
        @param name:
        @return:
        """
        self.tenantLastName = name

    def setSSN(self, newSSN: str = None):
        """
        Sets the Tenant's Social Security Numebr
        @param newSSN:
        @return:
        """
        self.tenantSSN = newSSN

    def setPhoneNumber(self, phoneNumber: str = None):
        """
        Sets Tenant's Phone Number
        @param phoneNumber:
        @return:
        """
        self.tenantPhoneNumber = phoneNumber

    def setEmail(self, email: str = None):
        """
        Sets Tenant's Email
        @param email:
        @return:
        """
        self.tenantEmail = email

    def saveData(self):
        #TODO: Overwrite to Database
        pass

    def getFirstName(self):
        """
        Returns the Tenant's First Name
        @return:
        """
        return self.tenantFirstName

    def getLastName(self):
        """
        Returns the Tenant's Last Name
        @return:
        """
        return self.tenantLastName

    def getName(self):
        """
        Returns both of the Tenants First and Last Name
        @return:
        """
        return self.tenantFirstName + " " + self.tenantLastName

    def getEmail(self):
        """
        Returns the Tenant's Email
        @return:
        """
        return self.tenantEmail

    def getSSN(self):
        """
        Returns the Tenants Social Security Number
        @return:
        """
        return self.tenantSSN

    def getAddress(self):
        """
        Gets the Property address that is associated with the tenant
        @return:
        """
        return self.tenantAddress

    def getPhoneNumber(self):
        """
        Returns the Tenant's Phone Number
        @return:
        """
        return self.tenantPhoneNumber

    def to_dict(self):
        """
        Returns Print statement for Tenant class
        @return:
        """
        return {"Name": self.tenantFirstName + " " + self.tenantLastName, "SSN": self.tenantSSN,
                "Address": self.tenantAddress, "Phone Number": self.tenantPhoneNumber, "Eamil": self.tenantEmail}
