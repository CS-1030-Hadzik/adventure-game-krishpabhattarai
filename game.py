"""
Docstring:
Adventure Game
Author: Krishpa Bhattarai
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
"""

##Welcome message and introduction
print("Welcome to the Adevnture Game!")
print('Your journey begins here...')

#Ask for the player's name
player_name = input("What is your name, adventurer? ")

#Concate nate strings to create a personalized messsage
print("Welcome, " + player_name + "! Your journey begins now.")

# Use an f-string to display the same message in a more readable way
print(f"Welcome, {player_name}! Your journey begins now.")

# Describe the starting area
starting_area = """
You find yourself in a dark forest.
The sound of rustling leaves fills the air.
A faint paths lies ahead, leading deeper into the 
unknown...
"""
print(starting_area)

# Ask the players for their first decision
decision = input("Do you wish to take the path?  (yes or no): ").lower()

# Invalid response loop until they give a valid
while decision not in ["yes", "no"]:
     print("Invalid choice. Please type 'yes' or 'no'.")
     # option for the user to make a new decision
     decision = input("Do you wish to take the path (yes or no): ").lower()

#Respond based on the player's decision
if decision == "yes":
    print(f"Brave choice, {player_name}!" " You step on the path and venture forward")

elif decision == "no":
    print(f"{player_name}, you decide to wait. Perhaps courage will find you later.")
