from typing import List
from System import db, Tenant


class Cont_Tenant:
    def __init__(self, accID):
        self.accID = accID
        self.tenants = list(db.readTenants(accID))
        DEBUG = True
        for ten in self.tenants:
            if DEBUG:
                print(f"self.tenants : {ten}")
                DEBUG = False

    def create_tenant(self, tenant: Tenant):
        # Here, you can add any validation or preprocessing needed before creating the Tenant
        new_tenant = tenant
        db.addToTenants(self.accID, new_tenant)
        self.add_tenant(new_tenant)
        # TODO: add database logic

    def add_tenant(self, tenant: Tenant):
        self.tenants.append(tenant)

    def find_tenant_by_id(self, account_id: int, tenant_id: int):
        for tenant in self.tenants:
            if tenant.getID() == tenant_id:
                return tenant
        print("Tenant not found")
        return None
    
    def get_tenants(self):
        self.update_tenants()
        return self.tenants
    
    def get_tenant_names(self):
        names = dict()
        for tenant in self.tenants:
            names[tenant.getFirstName() +" "+ tenant.getLastName()] = tenant.getID()
        print(names)
        return names
    
    def update_tenants(self):
        self.tenants = list(db.readTenants(self.accID))

    def add_to_property(self, tenID, propID):
        """adds the property ID, address to the tenant

        Args:
            tenID (_type_): _description_
            propID (_type_): _description_
        """
        #find the tenant with id
        tenant = self.find_tenant_by_id(self.accID,tenID)
        #set tenant object's prop id
        tenant.set_property_id(propID)

        #ask database to update with tenantid
        db.updateTenant(tenant)
        
        


    def update_tenant_first_name(self, account_id: int, tenant_first_name: str, tenant_id: int):
        tenant = self.find_tenant_by_id(1, tenant_id)
        if tenant:
            tenant.set_first_name(tenant_first_name)
            db.updateTenant(tenant)

    def update_tenant_name(self, account_id: int, tenant_last_name: str, tenant_id: int):
        tenant = self.find_tenant_by_id(1, tenant_id)
        if tenant:
            tenant.set_last_name(tenant_last_name)
            db.updateTenant(tenant)

    def update_ssn(self, account_id: int, tenant_id: int, tenant_ssn: str):
        tenant = self.find_tenant_by_id(1, tenant_id)
        if tenant:
            tenant.set_ssn(tenant_ssn)
            db.updateTenant(tenant)

    def update_phone_number(self, account_id: int, tenant_id: int, phone_number: str):
        tenant = self.find_tenant_by_id(1, tenant_id)
        if tenant:
            tenant.set_phone_number(phone_number)
            db.updateTenant(tenant)

    def update_tenant_address(self, account_id: int = 1, tenant_id: int = None, new_address: str = ""):
        tenant = self.find_tenant_by_id(1,tenant_id)
        if tenant:
            tenant.setAddress(new_address)
            db.updateTenant(tenant)

    def update_tenant_email(self, account_id: int, tenant_id: int, email: str):
        tenant = self.find_tenant_by_id(1, tenant_id)
        if tenant:
            tenant.set_email(email)
            db.updateTenant(tenant)

    def remove_tenant(self, ten_id:int):
        for tenant in self.tenants:
            if tenant.getID() == ten_id:
                print("DELETED TENANT")
                self.tenants.remove(tenant)
        db.deleteTenant(ten_id)

    def print_tenants(self):
        for tenant in self.tenants:
            print(tenant)
