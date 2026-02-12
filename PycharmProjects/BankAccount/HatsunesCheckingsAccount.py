from BankAccount import HatsuneMikuCreditUnion

class CheckingsAccount(HatsuneMikuCreditUnion):
    def __init__(self, customer_name, customer_balance, minimum_balance, account_number, routing_number, transfer_limitation):
        super().__init__(customer_name, customer_balance, minimum_balance)
        self._account_number = account_number
        self.__routing_number = routing_number
        self._transfer_limitation = transfer_limitation

    def transfer(self, amount):
        if amount > self._transfer_limitation:
            print(f"Transfer failed: Amount exceeds limit of {self._transfer_limitation}")
        elif self.current_balance - amount < self.minimum_balance:
            # Added 'f' before the string so {self.minimum_balance} renders as a number
            print(f"Transfer not complete, your minimum balance of {self.minimum_balance} must remain in the account")
        else:
            # Logic Fix: Subtract from balance, not the account number!
            self.current_balance -= amount
            print(f"Transfer successful! New Balance: {self.current_balance}")
