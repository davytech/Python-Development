print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[Burgeon]
*******************************************************************************
''')

print("Welcome to Burgeon Treasure Island.")
print("Your mission is to find the treasure.")
name = input("What's your name? ")
permission = input(f"{name}, are you ready to play? Type y for Yes or n for No. ")

if permission == "y":
    print(f"Let's get started, {name}!")

    # For Right or Left
    Right_or_Left = input("You're at a crossroad. Where would you like to go. Type 'right' or 'left' ")

    if Right_or_Left == "left":
        print("Brill! You made the right choice.")
        #For Swim or Wait
        swim_or_wait = input(f"{name}, would you like to swim or wait? ")
        if swim_or_wait == "swim":
            print("Alright, agba Swimmer. I hail you ooo. :-)")
            colour = input("Now, you have gotten to the island! "
            "There is a house with 3 doors: red, green, and yellow. "
            "Which one will you enter? ")
            if colour == "yellow":
                print("Congratulations, you won! ")
            elif colour == "red":
                print("You've gotten burnt by fire. Game over!")
            elif colour == "green":
                print("You were eaten by a tiger. You don die. LOL. Game over.")
            else:
                print("You choose a door that doesn't exist. Game over.")
        else:
            print(f"You have waited and died of hunger. Learn to take risks sometimes, {name}. Game over.")
    else:
        print(f"Ohh, {name}! Not all things that sounds good are good. You have fallen into a hole. Game over.")

else:
    print("Alright, you no wan play. No wahala. Take care!")
