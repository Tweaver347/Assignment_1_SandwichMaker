from data import resources, recipes
from sandwich_maker import SandwichMaker
from cashier import Cashier

def main():
    sandwich_maker = SandwichMaker(resources)
    cashier = Cashier()

    is_on = True
    while is_on:
        choice = input("What would you like? (ham_sandwich): ")
        if choice == "off":
            is_on = False
        elif choice in recipes:
            sandwich = recipes[choice]
            if sandwich_maker.check_resources(sandwich):
                payment = cashier.process_coins()
                if cashier.transaction_result(payment, 5.0):  # Assuming cost of a sandwich is $5
                    sandwich_maker.make_sandwich(choice, sandwich)

if __name__ == "__main__":
    main()
