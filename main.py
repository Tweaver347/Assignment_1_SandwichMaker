### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item, amount in ingredients.items():
            if ingredients[item] > self.machine_resources[item]:
                print(f"Sorry, there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")
        large_dollars = int(input("how many large dollars?: ")) * 1.00
        half_dollars = int(input("how many half dollars?: ")) * 0.50
        quarters = int(input("how many quarters?: ")) * 0.25
        nickels = int(input("how many nickels?: ")) * 0.05
        return large_dollars + half_dollars + quarters + nickels

    def transaction_result(self, coins, cost):
            """Return True when the payment is accepted, or False if money is insufficient.
               Hint: use the output of process_coins() function for cost input"""
            if coins >= cost:
                change = round(coins - cost, 2)
                if change > 0:
                    print(f"Here is ${change} in change.")
                return True
            else:
                print("Sorry, that’s not enough money. Money refunded.")
                return False

    def make_sandwich(self, sandwich_size, order_ingredients):
            """Deduct the required ingredients from the resources.
               Hint: no output"""
            for item, amount in order_ingredients.items():
                self.machine_resources[item] -= amount
            print(f"{sandwich_size} sandwich is ready. Bon appetit!")

def report(self):
    """Prints the current resources available in the machine."""
    print(f"Bread: {self.machine_resources['bread']} slice(s)")
    print(f"Ham: {self.machine_resources['ham']} slice(s)")
    print(f"Cheese: {self.machine_resources['cheese']} ounce(s)\n")


### Make an instance of SandwichMachine class and write the rest of the codes ###
machine = SandwichMachine(resources)

is_on = True

while is_on:
    choice = input("What would you like? (small/medium/large/off/report): ").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        report(machine)
    elif choice in recipes:
        sandwich = recipes[choice]
        if machine.check_resources(sandwich['ingredients']):
            payment = machine.process_coins()
            if machine.transaction_result(payment, sandwich['cost']):
                machine.make_sandwich(choice, sandwich['ingredients'])

                if choice == "off":
                    is_on = False
                elif choice == "report":
                    report(machine)
                elif choice in recipes:
                    sandwich = recipes[choice]