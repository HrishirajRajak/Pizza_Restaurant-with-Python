class PizzaOrder:
    bill = 0.0
    pizza_choice = ""
    def __init__(self):
        return None

    def greeting(self):
        print("Welcome to the Pizza Restaurant!")

    def input_order(self):
        print("\n\nSure, I would gladly take your order than. \nWhich pizza would you like? \n1. Menu  \n2. Total Bill \n3. Exit")

    def menu(self):
        print("\n\nHere is our menu: \n1. Margherita \n2. Pepperoni \n3. BBQ Chicken \n4. Veggie \n5. Hawaiian\n")
        self.pizza_choice = input("\nPlease choose the pizza you want to order: ")
        self.add_to_order()

    def add_to_order(self):
        prices = {
            "Margherita": 9.99,
            "Pepperoni": 10.99,
            "BBQ Chicken": 10.99,
            "Veggie": 7.99,
            "Hawaiian": 12.99
        }

        if self.pizza_choice in prices:
            self.bill += prices[self.pizza_choice]
            print(f"{self.pizza_choice} added to your order. Current bill: ${self.bill:.2f}")
        else:
            print("Invalid choice. Please select a valid pizza from the menu.")
            self.menu()

    def show_bill(self):
        print(f"Your total bill is: ${self.bill:.2f}")