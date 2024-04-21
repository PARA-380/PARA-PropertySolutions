from typing import List
from System import db, Tenant


class Cont_Tenant:
    """Controller Class for Tenants to connect Tenant Operations to Database and GUI.
    """
    def __init__(self, accID):
        """Constructs a Tenant Controller based on the current Tenant Table in Database

        Args:
            accID (_type_): A given account ID for the current Session. 
        """
        self.accID = accID
        self.tenants = list(db.readTenants(accID))
        DEBUG = True
        for ten in self.tenants:
            if DEBUG:
                #print(f"self.tenants : {ten}")
                DEBUG = False

    def create_tenant(self, tenant: Tenant):
        """Creates a new tenant to the Database

        Args:
            tenant (Tenant): Given Tenant Object to copy details to Database
        """
        # Here, you can add any validation or preprocessing needed before creating the Tenant
        new_tenant = tenant
        db.addToTenants(self.accID, new_tenant)
        self.add_tenant(new_tenant)
        # TODO: add database logic

    def add_tenant(self, tenant: Tenant):
        """Adds the tenant to the Controller's list of Tenant Objects

        Args:
            tenant (Tenant): Given Tenant to add
        """
        self.tenants.append(tenant)

    def find_tenant_by_id(self, account_id: int, tenant_id: int):
        """Finds the Tenant in its list from the given Tenant ID.

        Args:
            account_id (int): Given Account ID if we need to look up the Database Again.
            tenant_id (int): The Database Tenant ID to look for.

        Returns:
            _type_: Returns the Tenant if Found or None if not found.
        """
        for tenant in self.tenants:
            if tenant.get_id() == tenant_id:
                return tenant
        print("Tenant not found")
        return None
    
    def get_tenants(self):
        self.update_tenants()
        return self.tenants
    
    def update_tenants(self):
        self.tenants = list(db.readTenants(self.accID))

    def update_tenant_first_name(self, account_id: int, tenant_first_name: str, tenant_id: int):
        tenant = self.find_tenant_by_id(1, tenant_id)
        if tenant:
            tenant.set_first_name(tenant_first_name)
            db.update_tenant(tenant)

    def update_tenant_name(self, account_id: int, tenant_last_name: str, tenant_id: int):
        tenant = self.find_tenant_by_id(1, tenant_id)
        if tenant:
            tenant.set_last_name(tenant_last_name)
            db.update_tenant(tenant)

    def update_ssn(self, account_id: int, tenant_id: int, tenant_ssn: str):
        tenant = self.find_tenant_by_id(1, tenant_id)
        if tenant:
            tenant.set_ssn(tenant_ssn)
            db.update_tenant(tenant)

    def update_phone_number(self, account_id: int, tenant_id: int, phone_number: str):
        tenant = self.find_tenant_by_id(1, tenant_id)
        if tenant:
            tenant.set_phone_number(phone_number)
            db.update_tenant(tenant)

    def update_tenant_address(self, account_id: int, tenant_id: int, new_address: str):
        tenant = self.find_tenant_by_id(1,tenant_id)
        if tenant:
            tenant.setAddress(new_address)
            db.update_tenant(tenant)

    def update_tenant_email(self, account_id: int, tenant_id: int, email: str):
        tenant = self.find_tenant_by_id(1, tenant_id)
        if tenant:
            tenant.set_email(email)
            db.update_tenant(tenant)

    def remove_tenant(self, ten_id:int):
        for tenant in self.tenants:
            if tenant.getID() == ten_id:
                print("DELETED TENANT")
                self.tenants.remove(tenant)
        db.deleteTenant(ten_id)

    def print_tenants(self):
        for tenant in self.tenants:
            print(tenant)
