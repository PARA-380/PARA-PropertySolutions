from System import Bills


# NEED DATABASE FUNCTIONS

class Cont_Bills:
    def __init__(self, property_id):
        self.propID = property_id
        self.bills = list(db.readBills(property_id))
        DEBUG = True
        for bill in self.bills:
            if DEBUG:
                # print(f"self.tenants : {ten}")
                DEBUG = False

    def create_bill(self, prop_ID, bill: Bills):
        new_bill = bill
        db.addToBills(self.propID, new_bill)
        #self.add_bill(new_bill)

    def pay_bill(self, amount):
        self.amount -= amount

    def collect_bill(self, amount):
        self.amount += amount

    def get_contractors(self) -> list[Bills]:
        self.update_bills()
        return self.bills

    def update_bills(self):
        self.bills = db.readBills(self.propID)