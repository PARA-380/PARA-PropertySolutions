"""
Bill.py
Name: Adrian Carreno
Date: 05/17/24
Description: Handles Bill attributes
Purposes: Creates a basis for a Bill and its attributes. Attributes get handled by its controller.
"""
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
        """set the bill id

        Args:
            billID (int): bill ID
        """
        self.billID = billID

    def get_bill_id(self):
        """get the bill ID

        Returns:
            _int: bill ID
        """
        return self.billID
    
    def get_acc_id(self):
        """get account ID

        Returns:
            int: account ID
        """
        return self.acc_ID
    
    def set_acc_id(self, accID):
        """set account ID

        Args:
            accID (int): passing account ID
        """
        self.acc_ID=accID

    def get_propID(self):
        """get property ID

        Returns:
            int: Property ID
        """
        return self.propID

    def set_propID(self, num: int):
        """set property ID

        Args:
            num (int): number to indicate property ID
        """
        self.propID = num

    #Attribute Get/Set
    def getDescription(self):
        """get Description of the bill

        Returns:
            string: description of the bill 
        """
        return self.description
    
    def setDescription(self, description):
        """set Description of the bill

        Args:
            description (string): description
        """
        self.description = description

    def getAmount(self):
        """get amount of the bill

        Returns:
            int: amount of the bill
        """
        return self.amount

    def set_amount(self, num: int):
        """set amount of the bill

        Args:
            num (int): number indicates the amount
        """
        self.amount = num

    def get_type(self):
        """get type of the bill (pay or collet)

        Returns:
            string: "collect", "pay", or None
        """
        print(f"bill type here: {type(self.bill_type)}")
        if self.bill_type.lower() == "collect":
            return "collect"
        elif self.bill_type.lower() == "pay":
            return "pay"
        else:
            print(f"invalid type")
            return None
        
    def set_type(self, type):
        """set type of the bill (pay or collet)

        Args:
            type (string): type of the bill (pay or collet)
        """
        if type == "collect":
            self.bill_type = "collect"
        elif type == "pay":
            self.bill_type = "pay"
        else:
            print(f"invalid type")
            self.bill_type = None
        
