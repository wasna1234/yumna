e_pin=int(input("create pin"))
confirm_pin=int(input("enter confirmed pin"))
pin=None
if pin==e_pin:
    print("pin created succesfully")
    pin=e_pin
    enter_pin=int(input("enter pin to login"))
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
else:
   print("pin did not match")
