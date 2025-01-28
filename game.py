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

#Concatenate strings to create a personalized messsage
print("Welcome, " + player_name + "! Your journey begins now.")

# Use an f-string to display the same message in a more readable way
print(f"Welcome, {player_name}! Your journey begins now.")

# Describe the starting area
starting_area = """
You find yourself in a dark forest.
The sound of rustling leaves fills the air.
A fi=aint paths lies ahead, leading deeper into the 
unknown...
"""
print(starting_area)