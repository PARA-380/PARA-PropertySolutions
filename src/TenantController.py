from Tenant import Tenant

class TenantController:
    def __init__(self):
        self.tenants: List[Tenant] = []

    def create_tenant(self, ID: int, firstname: str, lastname: str, tenantssn: str, tenantaddress: str,
                      tenantphonenumber: str, tenantemail: str):
        # Here, you can add any validation or preprocessing needed before creating the Tenant
        new_tenant = Tenant(ID, firstname, lastname, tenantssn, tenantaddress, tenantphonenumber, tenantemail)
        self.add_tenant(new_tenant)
        # TODO: add database logic

    def add_tenant(self, tenant: Tenant):
        self.tenants.append(tenant)

    def find_tenant_by_id(self, tenant_id: int):
        for tenant in self.tenants:
            if tenant.get_ID() == tenant_id:
                return tenant
        return None

    def update_tenant_first_name(self, tenant_first_name: str, tenant_id: int):
        tenant = self.find_tenant_by_id(tenant_id)
        if tenant:
            tenant.set_first_name(tenant_first_name)
        else:
            print("Tenant not found")

    def update_tenant_name(self, tenant_last_name: str, tenant_id: int):
        tenant = self.find_tenant_by_id(tenant_id)
        if tenant:
            tenant.set_last_name(tenant_last_name)
        else:
            print("Tenant not found")

    def update_ssn(self, tenant_id: int, tenant_ssn: str):
        tenant = self.find_tenant_by_id(tenant_id)
        if tenant:
            tenant.set_ssn(tenant_ssn)
        else:
            print("Tenant not found")

    def update_phone_number(self, tenant_id: int, phone_number: str):
        tenant = self.find_tenant_by_id(tenant_id)
        if tenant:
            tenant.set_phone_number(phone_number)
        else:
            print("Tenant not found")

    def update_tenant_address(self, tenant_id: int, new_address: str):
        tenant = self.find_tenant_by_id(tenant_id)
        if tenant:
            tenant.setAddress(new_address)
            # Update database or persistence layer here
        else:
            print("Tenant not found")

    def update_tenant_email(self, tenant_id: int, email: str):
        tenant = self.find_tenant_by_id(tenant_id)
        if tenant:
            tenant.set_email(email)

    def remove_tenant(self, tenant_id: int):
        self.tenants = [tenant for tenant in self.tenants if tenant.get_ID() != tenant_id]

    def print_tenants(self):
        for tenant in self.tenants:
            print(tenant)