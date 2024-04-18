from typing import List
from System import db, Tenant


class Cont_Tenant:
    def __init__(self, accID):
        self.accID = accID
        self.tenants = list(db.readTenants(accID))
        for ten in self.tenants:
            print(f"self.tenants : {type(ten)}")

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
            if tenant.get_id() == tenant_id:
                return tenant
        print("Tenant not found")
        return None
    
    def get_tenants(self):
        return self.tenants
    
    def update_tenant(self):
        pass

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

    def remove_tenant(self, tenant_id: int):
        self.tenants = [tenant for tenant in self.tenants if tenant.getID() == tenant_id]
        db.deleteTenant(tenant_id)

    def print_tenants(self):
        for tenant in self.tenants:
            print(tenant)
