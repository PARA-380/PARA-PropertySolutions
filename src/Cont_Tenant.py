"""
File: Cont_Tenant.py
Name: Adrian Carreno, Ali Maamoun
Date: 04/23/24
Description: Controller for Tenant class
Purposes: Controller Class for Tenants to connect Tenant Operations to Database and GUI.
"""

from typing import List
from System import db, Tenant


class Cont_Tenant:
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
            if tenant.getID() == tenant_id:
                return tenant
        print("Tenant not found")
        return None
    
    def get_tenants(self):
        """
        Calls function update_tenants() to update tenants and returns them
        @return:
        """
        self.update_tenants()
        return self.tenants
    
    def get_tenant_names(self):
        names = dict()
        for tenant in self.tenants:
            names[tenant.getFirstName() +" "+ tenant.getLastName()] = tenant.getID()
        print(names)
        return names
    
    def get_tenants_at_property(self, propertyID):
        """given a property ID, find the tenants that live there and return a list

        Args:
            propertyID (_type_): db Property ID to filter by

        Returns:
            _type_: list of tenants at the property
        """
        tenants_at_property = []
        for tenant in self.tenants:
            if tenant.get_property_id() == propertyID:
                tenants_at_property.append(tenant)
        return tenants_at_property

    
    def update_tenants(self):
        """
        Calls on the database to update list of tenants
        @return:
        """
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
        """
        Finds the tenant by ID and updates the first name
        @param account_id:
        @param tenant_first_name:
        @param tenant_id:
        @return:
        """
        tenant = self.find_tenant_by_id(1, tenant_id)
        if tenant:
            tenant.set_first_name(tenant_first_name)
            db.updateTenant(tenant)

    def update_tenant_name(self, account_id: int, tenant_last_name: str, tenant_id: int):
        """
        Finds the tenant by ID and updates the last name
        @param account_id:
        @param tenant_last_name:
        @param tenant_id:
        @return:
        """
        tenant = self.find_tenant_by_id(1, tenant_id)
        if tenant:
            tenant.set_last_name(tenant_last_name)
            db.updateTenant(tenant)

    def update_ssn(self, account_id: int, tenant_id: int, tenant_ssn: str):
        """
        Finds the tenant by ID and updates the SSN
        @param account_id:
        @param tenant_id:
        @param tenant_ssn:
        @return:
        """
        tenant = self.find_tenant_by_id(1, tenant_id)
        if tenant:
            tenant.set_ssn(tenant_ssn)
            db.updateTenant(tenant)

    def update_phone_number(self, account_id: int, tenant_id: int, phone_number: str):
        """
        Finds the tenant by ID and updates the phone number
        @param account_id:
        @param tenant_id:
        @param phone_number:
        @return:
        """
        tenant = self.find_tenant_by_id(1, tenant_id)
        if tenant:
            tenant.set_phone_number(phone_number)
            db.updateTenant(tenant)

    def update_tenant_address(self, account_id: int, tenant_id: int, new_address: str):
        """
        Finds the tenant by ID and updates the address
        @param account_id:
        @param tenant_id:
        @param new_address:
        @return:
        """
        tenant = self.find_tenant_by_id(1,tenant_id)
        if tenant:
            tenant.setAddress(new_address)
            db.updateTenant(tenant)

    def update_tenant_email(self, account_id: int, tenant_id: int, email: str):
        """
        Finds the tenant by ID and updates the email
        @param account_id:
        @param tenant_id:
        @param email:
        @return:
        """
        tenant = self.find_tenant_by_id(1, tenant_id)
        if tenant:
            tenant.set_email(email)
            db.updateTenant(tenant)

    def remove_tenant(self, ten_id:int):
        """
        Finds the tenant by ID and removes them from the list of tenants
        @param ten_id:
        @return:
        """
        for tenant in self.tenants:
            if tenant.getID() == ten_id:
                print("DELETED TENANT")
                self.tenants.remove(tenant)
        db.deleteTenant(ten_id)

    def print_tenants(self):
        """
        prints from the list of tenants one by one
        @return:
        """
        for tenant in self.tenants:
            print(tenant)
