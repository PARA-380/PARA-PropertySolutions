class Bills:
    def __init__(self, pay: bool = None, collect: bool = None, property_ID: int = None, amount: int = None):
        self.pay = pay
        self.collect = collect
        self.propID = property_ID
        self.amount = amount

    def getAmount(self):
        return self.amount

    def set_amount(self, num: int):
        self.amount = num

    def get_propID(self):
        return self.propID

    def set_propID(self, num: int):
        self.propID = num
