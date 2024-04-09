from Entities.Tenant import Tenant


class Property:
    def __init__(self, property_id: int = None, accID : int  = None, address: str = None, tenants: dict = {}, sqft: str = None, home_type: str = None,
                 max_living: int = None):
        self.property_id = property_id
        self.account_id = accID
        self.address = address
        self.tenants = tenants
        self.sqft = sqft
        self.home_type = home_type
        self.max_living = max_living

    def get_property_id(self):
        return self.property_id

    def set_property_id(self, newId):
        self.property_id = newId

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_sqft(self):
        return self.sqft

    def set_sqft(self, sqft):
        self.sqft = sqft

    def get_home_type(self):
        return self.home_type

    def set_home_type(self, home):
        self.home_type = home

    def get_max_living(self):
        return self.max_living

    def set_max_living(self, num):
        self.max_living = num

    def add_tenant_to_property(self, tenant: Tenant):
        self.tenants.update({tenant.get_ID(): tenant})

    def remove_tenant_from_property(self, key:int):
        self.tenants.pop(key)


def main() -> None:
    pass


if __name__ == "__main__":
    pass
