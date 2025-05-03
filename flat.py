class Bill:
    """
    Objects that containes data about a bill such as total amount and
    period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatemate:
    """
    Create a flatemate person who loves in the falt and pays a share
    for the bill
    """
    def __init__(self, name,day_in_house):
        self.name = name
        self.day_in_house = day_in_house


    def pays(self, bill,flamate2):
        weight=self.day_in_house/(self.day_in_house+flamate2.day_in_house)
        to_pay=weight*bill.amount
        return to_pay
