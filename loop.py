pin="0000"
enter_pin=input("enter pin")
if enter_pin==pin:
    print("login successfully")
elif enter_pin!=pin:
    print("invalid pin attempt remain 3")
    enter_pin=input("enter pin")
    if enter_pin==pin:
        print("login successfully")
    elif enter_pin!=pin:
         print("invalid pin attempt remain 2")
         enter_pin=input("enter pin")
         if enter_pin==pin:
            print("login successfully")
         elif enter_pin!=pin:
            print("invalid pin attempt remain 1")
            enter_pin=input("enter pin")
            if enter_pin==pin:
                print("login successfully")
            else:
                print("blocked")

       

