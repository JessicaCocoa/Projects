import random
"""
Introduction to the game
"""
def intro_game():
    print("You are a kid who only thinks of candy and fun. You decide to test your fate at two very different lands to get some CANDY!")
    print("Boogeyman land is a guessing number game and you have two tries to guess the right number. Goblin's Dice is a game where you must roll a 12 in two tries.")
    print("Both games have a candy reward or a consequence!")
"""
function that makes the player choose a game
"""
def choose_game():
    print("Which game would you like to play?")
    game_choice = input("Press 'b' for Boogeyman Land or 'g' for Goblin's Gambling: ")
    return game_choice ## returns the answer to main
"""Function named boogeyman_land that allows player to guess a random number 1-10"""

def boogeyman_land():
    print("You have two tries to guess a number I am thinking of 1-10. If you guess right you will get two pieces of candy.")
    print("If you lose, you sink in my quicksand! HAHAHAH")
    answer = random.randint(1, 10) ## picks a random number
    counter = 0 ## gives the person two tries
    while counter < 2:
        choice = int(input("What is your guess? "))
        if choice == answer:
            print("You may have two pieces of candy!")
            return ## goes out of the function back to main
        elif choice > 10 or choice < 1:
            print("You guessed a number that was higher than 10 or less than 1. Try again.")
        else:
            print("You guessed wrong.")
            counter += 1 ## adds to the counter
    print("You sank in the quicksand!") ## outside of while function, so once it passes 2 reps, the person looses
"""Function named goblins_dice that allows the player to roll a dice and get the number 12"""
def goblins_dice():
    print("I am going to roll two dice and if you get the number 12 you get two pieces of candy. If you don't get a 12, you lose all your money.")
    counter2 = 0
    while counter2 < 2:
        dice_roll1 = random.randint(1, 6) # dice rolls a number
        dice_roll2 = random.randint(1, 6) # dice rolls a number
        total = dice_roll1 + dice_roll2 # total number rolled
        if total == 12:
            print("You win! Here are two pieces of candy!")
            return # goes out of function
        else:
            print("You have one more chance!")
            counter2 += 1 # adds to counter and gives another chance
    print("You lost all your money from gambling.")

"""Main game that controls if the user would like to play again"""
def main():
    intro_game()
    keep_playing = input("Would you like to play? y/n: ")
    while keep_playing.lower() == "y":
        game_choice = choose_game()
        if game_choice.lower() == "b":
            boogeyman_land()
        elif game_choice.lower() == "g":
            goblins_dice()
        else:
            print("Invalid choice. Please choose 'b' or 'g'.")
        keep_playing = input("Would you like to play again? y/n: ")
    print("Goodbye!")


if __name__ == "__main__":
    main()




