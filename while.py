set_pin=int(input("set pin"))
condition=True
att=3

while condition:
    enter_pin=int(input("enter pin"))
    if enter_pin==set_pin:
        print("correct pin")
        condition=False

    else:
        print("incorrect pin",att,"attempts remaining")
        if att==0:
            print("blocked")
            condition=False
    att-=1        