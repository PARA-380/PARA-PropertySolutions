from typing import List
from Tenant import Tenant
import Database as db


class TenantController:
    def __init__(self):
        self.tenants: List[Tenant] = []

    def create_tenant(self, firstname: str, lastname: str, tenantssn: str, tenantaddress: str,
                      tenantphonenumber: str, tenantemail: str):
        # Here, you can add any validation or preprocessing needed before creating the Tenant
        new_tenant = Tenant(firstname, lastname, tenantssn, tenantaddress, tenantphonenumber, tenantemail)
        db.addToTenants(1, new_tenant)
        self.add_tenant(new_tenant)
        # TODO: add database logic

    def add_tenant(self, tenant: Tenant):
        self.tenants.append(tenant)

    def find_tenant_by_id(self, tenant_id: int):
        for tenant in self.tenants:
            if tenant.get_id() == tenant_id:
                return tenant
        print("Tenant not found")
        return None

    def update_tenant_first_name(self, tenant_first_name: str, tenant_id: int):
        tenant = self.find_tenant_by_id(tenant_id)
        if tenant:
            tenant.set_first_name(tenant_first_name)
            db.update_tenant(tenant)

    def update_tenant_name(self, tenant_last_name: str, tenant_id: int):
        tenant = self.find_tenant_by_id(tenant_id)
        if tenant:
            tenant.set_last_name(tenant_last_name)
            db.update_tenant(tenant)

    def update_ssn(self, tenant_id: int, tenant_ssn: str):
        tenant = self.find_tenant_by_id(tenant_id)
        if tenant:
            tenant.set_ssn(tenant_ssn)
            db.update_tenant(tenant)

    def update_phone_number(self, tenant_id: int, phone_number: str):
        tenant = self.find_tenant_by_id(tenant_id)
        if tenant:
            tenant.set_phone_number(phone_number)
            db.update_tenant(tenant)

    def update_tenant_address(self, tenant_id: int, new_address: str):
        tenant = self.find_tenant_by_id(tenant_id)
        if tenant:
            tenant.setAddress(new_address)
            db.update_tenant(tenant)

    def update_tenant_email(self, tenant_id: int, email: str):
        tenant = self.find_tenant_by_id(tenant_id)
        if tenant:
            tenant.set_email(email)
            db.update_tenant(tenant)

    def remove_tenant(self, tenant_id: int):
        self.tenants = [tenant for tenant in self.tenants if tenant.get_id() != tenant_id]

    def print_tenants(self):
        for tenant in self.tenants:
            print(tenant)