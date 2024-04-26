from System import db, Contractor

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
        self.tenants.append(contractor)

    def get_contractors(self):
        self.update_contractors()
        return self.contractors
    
    def update_contractors(self):
        self.tenants = list(db.readContractors(self.accID))
