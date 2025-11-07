import Pizza_order


if __name__  == "__main__":
   start = Pizza_order.PizzaOrder()
   start.greeting()
   while True:
        start.input_order()
        user_input = input(":")
        if user_input == "1":
            start.menu()
            start.add_to_order()

        if user_input == "2":
            start.show_bill()
        elif user_input.lower() == "exit" or user_input.lower() == "quit" or user_input.lower() == "3":
            quit()
        else:
            continue
        
        

