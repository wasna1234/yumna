# # # import arrow
# # # print(arrow.now())

# # # import arrow as w
# # # print(w.utcnow())


# # def number():
# #       y=5
# #       z=4
# #       print(y+z)
      
# # number()



# def par( l,w):
#     par=l+w+l+w
#     print("the parameter",par)

# par(44,33)

set_pin=input("set pin")

count_pin=0
for d in set_pin:
    count_pin+=1

if count_pin !=4:
    print("pin must have 4 digits")

else: 
    set_pin=int(set_pin)
    att=3
    condition=True

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