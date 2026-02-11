import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    ###  write the rest of the codes ###
    user_choice = input(
        "Hello and Welcome to Hatsune Miku Sandwich Shop! What size of sandwich do you want?"
        " (small/medium/large): "
    )
    if user_choice in ["small", "medium", "large"]:
        ingredients = recipes[user_choice]["ingredients"]
        cost = recipes[user_choice]["cost"]

    if sandwich_maker_instance.check_resources(ingredients):
        money = cashier_instance.process_coins()

    if cashier_instance.transaction_result(money, cost):
        sandwich_maker_instance.make_sandwich(user_choice, ingredients)
        print("Enjoy your sandwich!")
    else:
        print("Sorry, you don't have enough money!")

if __name__=="__main__":
    main()
