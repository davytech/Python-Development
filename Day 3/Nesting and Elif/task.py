print("Welcome to Burgeon rollercoaster!")
height = int(input("What is your height in cm?\n"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?\n"))
    if age <0:
        print("You are not born yet. Go back to your mother's womb, Fetus!")
    elif age <= 5:
        print("You are way too young to ride the rollercoaster")
    elif age <= 12:
        print("Child ticket is $5.")
        bill = 5
    elif age <= 18:
        bill = 7
        print("Youth ticket is $7.")
    else:
        bill = 10
        print("Adult ticket is $10")

    want_photo = input("Do you want to take a photo? Type Y for Yes and N for No.\n")
    if want_photo == "Y":
        bill += 3
    elif want_photo == "y":
        bill += 3

    print(f"Your final bill is {bill}")

else:
    print("Sorry you have to grow taller before you can ride.")
