"""Simulate rolling two dice, three times. 
Prints the results of each die roll.
This program is used to show how variable scope works."""

import random

def roll_dice():
    
    NUM_SIDES = 6
    
    dice1 = random.randint(1, NUM_SIDES)
    dice2 = random.randint(1, NUM_SIDES)
    
    total = dice1 + dice2
    
    print(f"dice 1 is: {dice1}, dice 2 is: {dice2}, and Total of two dice is =", total)
    
def main():
    
    dice1: int = 10
    print(f"die1 in main(): starts as {dice1}")
    roll_dice()
    roll_dice()
    roll_dice()
    print(f"die1 in main() is still : {dice1}")

if __name__ == "__main__":
    main()