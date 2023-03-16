import random

choice = "Y"

print("Lets play Rock Scissor and Paper game")

options = ["R","S","P"]

computer_choice = random.choice(options)

while choice=='Y':
    user_choice = input("Please enter your choice- R S P ")

    if user_choice!= "R" and user_choice!="S" and user_choice!="P" :
        print("Wrong input")
    else:
        if(user_choice==computer_choice):
            print("Draw")
        elif (user_choice=="R" and computer_choice=="S") or (user_choice=="S" and computer_choice=="P") or (user_choice=="P" and computer_choice=="R"):
            print("User wins")
        elif (user_choice=="S" and computer_choice=="R") or (user_choice=="P" and computer_choice=="S") or (user_choice=="R" and computer_choice=="P"):
            print("Computer wins")
        else:
            ("Error")

    choice = input("Enter Y to continue or anything else :")