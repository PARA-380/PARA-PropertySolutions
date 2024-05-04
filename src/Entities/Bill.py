class Bill:
    """A bill is assigned to a house and has a positive or negative value
    """
    def __init__(self,billID : int = None, account_id: int = None, property_ID: int = None, 
                 description : str = None,  bill_type : str = None, amount: int = None):
        #ID's
        self.billID = billID
        self.acc_ID = account_id
        self.propID = property_ID
        #attributes
        self.description : str= description
        self.bill_type : str= bill_type
        self.amount : int = amount

    #ID Get/Set
    def set_bill_id(self, billID):
        self.billID = billID

    def get_bill_id(self):
        return self.billID
    
    def get_acc_id(self):
        return self.acc_ID
    
    def set_acc_id(self, accID):
        self.acc_ID=accID

    def get_propID(self):
        return self.propID

    def set_propID(self, num: int):
        self.propID = num

    #Attribute Get/Set
    def getDescription(self):
        return self.description
    
    def setDescription(self, description):
        self.description = description

    def getAmount(self):
        return self.amount

    def set_amount(self, num: int):
        self.amount = num

    def get_type(self):
        print(f"bill type here: {type(self.bill_type)}")
        if self.bill_type.lower() == "collect":
            return "collect"
        elif self.bill_type.lower() == "pay":
            return "pay"
        else:
            print(f"invalid type")
            return None
        
    def set_type(self, type):
        if type == "collect":
            self.bill_type = "collect"
        elif type == "pay":
            self.bill_type = "pay"
        else:
            print(f"invalid type")
            self.bill_type = None
        
