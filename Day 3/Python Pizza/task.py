print("Welcome to Python Pizza Deliveries!")
size = input("What size of pizza do you want? S, M or L:\n")
#For Pizza Size
bill = 0
if size == "S":
    print("Small pizza is $15")
    bill = 15
elif size == "M":
    print("Medium pizza is $20")
    bill = 20
elif size == "L":
    print("Large pizza is $25")
    bill = 25
else:
    print("You have entered and invalid size.")

#For Pepperoni
pepperoni = input("Do you want pepperoni on your pizza? Y or N:\n")
if pepperoni == "Y":
    if size == "S":
        bill +=2
        print(f"Your current bill is ${bill}")
    else:
        bill +=3
        print(f"Your current bill is ${bill}")

#For Cheese
extra_cheese = input("Do you want extra cheese? Y or N:\n")
if extra_cheese == "Y":
    bill +=1

print(f"Your final bill = ${bill}")
