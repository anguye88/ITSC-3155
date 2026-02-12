class HatsuneMikuCreditUnion:
    bank_title = "Hatsune Miku Credit Union"
    def __init__(self, customer_name, customer_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = customer_balance
        self.minimum_balance = minimum_balance


    def customer_info_information(self):
        print("Welcome to ", self.bank_title, "!")
        print("Your name is: ", self.customer_name)
        print("Current balance: ", self.current_balance)
        print("Minimum balance: ", self.minimum_balance)

    def deposit(self, amount):
                self.current_balance += amount

    def withdraw(self, amount):
                if self.current_balance - amount < self.minimum_balance:
                    print("You cannot withdraw", amount, "Please have at least have a minimal balance of", self.minimum_balance)
                else:
                    self.current_balance -= amount
                    print("Withdrawal has completed." , "You now have: ", self.current_balance)


customer_1 = HatsuneMikuCreditUnion("Hatsune Miku", 6700, 670)
customer_2 = HatsuneMikuCreditUnion("Kasane Teto", 400, 370)

customer_1.customer_info_information()
customer_1.withdraw(400)
customer_2.customer_info_information()
customer_2.withdraw(400)




