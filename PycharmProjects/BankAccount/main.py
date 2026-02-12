from HatsunesSavingsAccount import SavingsAccount
from HatsunesCheckingsAccount import CheckingsAccount



savings_1 = SavingsAccount("Hatsune Miku", 5000, 500, 8312007, 393939, 4.5)
savings_2 = SavingsAccount("Hatsune Miku", 6767, 500, 2312932, 393939, 4.5)

checking_1 = CheckingsAccount("Kaito", 8989, 100, 4012007, 7, 500)
checking_2 = CheckingsAccount("Megurine Luka", 3000, 300, 484841, 7, 50)


savings_1.add_interest()
savings_2.add_interest()

checking_1.transfer(200)