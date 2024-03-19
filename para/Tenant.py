from Entity import Entity


# from Lease import Lease
# remove above # after added Lease Class
# add lease variable in "__init__" function


class Tenant(Entity):
    # tenantName = None

    def __init__(self, tenantname: str = None, tenantssn: str = None, tenantaddress: str = None,
                 tenantphonenumber: str = None,
                 tenantemail: str = None):
        self.tenantName = tenantname
        self.tenantSSN = tenantssn
        self.tenantAddress = tenantaddress
        self.tenantPhoneNumber = tenantphonenumber
        self.tenantEmail = tenantemail
        # self.lease = Lease
        # self.dashboard

    def setAddress(self, newAddress: str = None):
        self.tenantAddress = newAddress

    def setName(self, name: str = None):
        self.tenantName = name

    def setSSN(self, newSSN: str = None):
        self.tenantSSN = newSSN

    def setPhoneNumber(self, phoneNumber: str = None):
        self.tenantPhoneNumber = phoneNumber

    def setEmail(self, email: str = None):
        self.tenantEmail = email

    def getName(self):
        return self.tenantName

    def getEmail(self):
        return self.tenantEmail

    def getSSN(self):
        return self.tenantSSN

    def getAddress(self):
        return self.tenantAddress

    def getPhoneNumber(self):
        return self.tenantPhoneNumber


tenant = Tenant("Ridham", "123-45-6789", "Home Address", "(012) 345 - 6789", "ridham.patel@email.com")
tenant.toJSON()
