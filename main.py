if __name__  == "__main__":
   while True:
       print("Welcome to the pizza!")
       user_input = input("Would you like to have a  pizza ? : ")

       if user_input == "yes":
           print("\n\nSure, I would gladly take your order than. \nWhich pizza would you like? \n1. Menu  \n2. Total Bill 3. Exit")
           continue

       match user_input.lower():
           case ("yes"):
                print("\n\nSure, I would gadly take your order than. \nWhich pizza would you like? \n1. Menu  \n2. Total Bill 3. Exit")
                continue
           case "exit":
                print("Thank you for your time. \nGoodbye!")
                break