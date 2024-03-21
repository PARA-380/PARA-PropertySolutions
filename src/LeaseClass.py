class Lease:
    def __init__(self, price: int = None, start_date: str = None, end_date: str = None, address: str = None,
                 security_deposit: int = None):
        self.price = price
        self.start_date = start_date
        self.end_date = end_date
        self.address = address
        self.security_deposit = security_deposit

    def set_price(self, new_price):
        self.price = new_price

    def set_start_date(self, date):
        self.start_date = date

    def set_end_date(self, date):
        self.end_date = date

    def set_address(self, address):
        self.address = address

    def set_security_deposit(self, deposit):
        self.security_deposit = deposit

    def get_price(self):
        return self.price

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def get_address(self):
        return self.address

    def get_security_deposit(self):
        return self.security_deposit
