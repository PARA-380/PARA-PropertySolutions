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
        new_contractor = contractor
        db.addToContractors(self.accID, new_contractor)
        self.add_contractor(new_contractor)

    def add_contractor(self, contractor: Contractor):
        self.contractors.append(contractor)

    def get_contractors(self) -> list[Contractor]:
        self.update_contractors()
        return self.contractors
    
    def update_contractors(self):
        self.contractors = db.readContractors(self.accID)

    def remove_contractor(self, contractor_id:int):
        for contractor in self.contractors:
            if contractor.get_contractor_id() == contractor_id:
                print("DELETED CONTRACTOR")
                self.contractors.remove(contractor)
        db.deleteContractor(contractor_id)