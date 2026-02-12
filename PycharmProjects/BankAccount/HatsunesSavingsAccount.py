from BankAccount import HatsuneMikuCreditUnion

class SavingsAccount(HatsuneMikuCreditUnion):
    def __init__(self, customer_name, customer_balance, minimum_balance, account_number, routing_number, interest_rate):
        super().__init__(customer_name, customer_balance, minimum_balance)
        self.__account_number = account_number
        self.__routing_number = routing_number
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = (self.interest_rate * self.current_balance) / 100
        self.current_balance += interest
        print(f"Your interest is {interest}. Your new balance is {self.current_balance}")