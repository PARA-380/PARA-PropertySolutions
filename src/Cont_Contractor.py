"""
File: Cont_Contractor.py
Name: Jittapatana Prayoonpruk
Date: 04/27/24
Description: Controller for Contractor class
Purposes: Controller Class for Contractor Page to connect Contractor Operations to Database and GUI.
Sets the correct ID for contractors as well as handling function such as add/delete contractors.
"""
from System import db, Contractor
from typing import List

class Cont_Contractor:
    def __init__(self, accID):
        self.accID = accID
        self.contractors = list(db.readContractors(accID))
        DEBUG = True
        for ten in self.contractors:
            if DEBUG:
                #print(f"self.tenants : {ten}")
                DEBUG = False

    def create_contractor(self, contractor: Contractor):
        """create new contractor and connect to the database

        Args:
            contractor (Contractor): contractor object
        """
        new_contractor = contractor
        db.addToContractors(self.accID, new_contractor)
        self.add_contractor(new_contractor)

    def add_contractor(self, contractor: Contractor):
        """add contractor to the list of contractors

        Args:
            contractor (Contractor): contractor object
        """
        self.contractors.append(contractor)

    def get_contractors(self) -> list[Contractor]:
        """get list of contractors

        Returns:
            list[Contractor]: list of contractor objects
        """
        self.update_contractors()
        return self.contractors
    
    def update_contractors(self):
        """update contractor to teh database
        """
        self.contractors = db.readContractors(self.accID)

    def remove_contractor(self, contractor_id:int):
        """remove contractor, by its ID, from the list
        delete the contractor from the database

        Args:
            contractor_id (int): contractor_id (key to remove)
        """
        for contractor in self.contractors:
            if contractor.get_contractor_id() == contractor_id:
                print("DELETED CONTRACTOR")
                self.contractors.remove(contractor)
        db.deleteContractor(contractor_id)