from System import Bill, db


# NEED DATABASE FUNCTIONS

class Cont_Bill:
    def __init__(self, acc_id, prop_id):
        self.account_id = acc_id
        self.property_id = prop_id
        self.bills : dict[int,Bill] #dictionary of bills for one property
        if prop_id is not None:
            self.update_bills(prop_id)

    def create_bill(self, description : str, type : str, amount : int):
        new_bill = Bill(account_id=self.account_id, property_ID=self.property_id, description= description, amount = amount, bill_type=type)
        print(f"billtype in here: {new_bill.get_type()}")
        db.addToBill(self.property_id, new_bill)
        self.add_bill(new_bill.get_bill_id(), new_bill)

    def add_bill(self, bill_id, bill):
        self.bills.update({bill_id : bill})

    def remove_bill(self, bill_id):
        """Removes a bill from the dictionary by its ID

        Args:
            bill_id (_type_): ID to remove

        Returns:
            _type_: Returns the popped bill
        """
        return self.bills.pop(bill_id)
    
    def delete_bill(self, bill_id):
        db.deleteBill(bill_id)
        self.remove_bill(bill_id)

    def pay_bill(self, amount):
        self.amount -= amount

    def collect_bill(self, amount):
        self.amount += amount

    def get_bills(self) -> dict[int,Bill]:
        self.update_bills()
        return self.bills
    
    def change_property(self, prop_id):
        """changes the scope of which property controller is looking at.
        """
        #set new property ID
        self.property_id = prop_id
        #update bills
        self.update_bills()

    def update_bills(self):
        self.bills = db.readBills(self.property_id)

    def find_bill_id(self, description, amount):
        for bill_instance in self.bills.values():
            if bill_instance.getDescription() == description and bill_instance.getAmount():
                return bill_instance.billID()