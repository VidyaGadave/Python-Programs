# Create a loop that prints all of the candies in the store to the terminal, with their index stored in brackets beside them.
# For example: "[0] Snickers"
# Create a second loop that runs for a set number of times determined by the variable allowance.
# For example: If allowance is equal to five, the loop should run five times.
# Each time this second loop runs, take in a user's input, preferably a number, and then add the candy with the matching index to the variable candy_cart.
# For example: If the user enters "0" as their input, "Snickers" should be added into the candy_cart list.
# Use another loop to print all of the candies selected to the terminal.


candy_list = [
    "Snickers",
    "Kit Kat",
    "Sour Patch Kids",
    "Juicy Fruit",
    "Swedish Fish",
    "Skittles",
    "Hershey Bar",
    "Starbursts",
    "M&Ms"
]

for candy in candy_list:
    print(f"{candy} the index is {candy_list.index(candy)}")

allowance = 5
candy_cart = []
choice = ""


for i in range(allowance):
    choice = int(input("Enter your index :"))
    mychoice =candy_list[choice]
    candy_cart.append(mychoice)

print(candy_cart)
