class SandwichMaker:
    def __init__(self, resources):
        self.resources = resources

    def check_resources(self, order_ingredients):
        # Logic to check if there are enough resources for the sandwich
        for item in order_ingredients:
            if order_ingredients[item] > self.resources[item]:
                print(f"Sorry, not enough {item}.")
                return False
        return True

    def make_sandwich(self, sandwich_name, order_ingredients):
        # Logic to deduct the ingredients from resources and make the sandwich
        if self.check_resources(order_ingredients):
            for item in order_ingredients:
                self.resources[item] -= order_ingredients[item]
            print(f"{sandwich_name} is ready!")
        else:
            print("Cannot make the sandwich.")
