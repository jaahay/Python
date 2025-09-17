"""
Lab 1
Group #12
Author: James Rohr, James Hay
Date: 9-25-25

This main file allows the user to choose between two games.  First game is a random number
guessing game, and the second game is rock paper scissors"""

from Guess import guess_game
#from RockPaperScissors_File import rockpaperscissors_game

def main():
    User_selection = int(input("Enter your choice: \n"
                               "1. Random Number Guessing Game\n"
                               "2. Rock Paper Scissors Game\n"
                               "3. Exit\n"))
    while User_selection != 3:
        if User_selection == 1:
            guess_game()
        elif User_selection == 2:
            #rockpaperscissors_game()
            print("You chose an invalid option.")
        elif User_selection == 3:
            print("Thank you for playing!")
            break
if __name__ == "__main__":
    main()
