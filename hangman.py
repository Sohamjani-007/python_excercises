# algorithm
# 1. develop the interface
# 2.predefined list
# 3.instruction
# 4.check the words
# 5.if right enter in the empty list 
# 6.if wrong return the turns and draw
# 7. generate the figure.
# 8. checking if the word is valid or not
# 9. Word Main(Main = word the users win)

import random

def hangman():
    word = random.choice(["superman", "batman", "wonderwomen", "flash", "aquaman", "cyborg", "greenlatern", "joker", "deathstroke","harleyquinn"])
    valid_letters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''
    while len(word) > 0:
        main = ""
        missed = 0
        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "


        if main == word:
            print(main)
            print("You win !", name)
            break
        print("Guess the word", main)
        guess = input()


        if guess in valid_letters:
            guessmade = guessmade + guess
        else:
            print("enter valid letter")

        if guess not in word:
            turns = turns - 1
            if turns == 9:
                print("9 turns left")
                print("---------")
            if turns == 8:
                print("8 turns left")
                print("---------")
                print("    0    ")
            if turns == 7:
                print("7 turns left")
                print("---------")
                print("    0    ")
                print("    |    ")
            if turns == 6:
                print("6 turns left")
                print("---------")
                print("    0    ")
                print("    |\   ")
            if turns == 5:
                print("5 turns left")
                print("---------")
                print("    0    ")
                print("   /|\   ")
            if turns == 4:
                print("4 turns left")
                print("---------")
                print("    0    ")
                print("   /|\   ")
                print("   /     ")
            if turns == 3:
                print("3 turns left")
                print("---------")
                print("    0    ")
                print("   /|\   ")
                print("   / \   ")
            if turns == 2:
                print("2 turns left")
                print("-------|-")
                print("    0  | ")
                print("   /|\   ")
                print("   / \   ")
            if turns == 1:
                print("1 turns left")
                print("Final wishes !!!")
                print("--------|-")
                print("   _0_--| ")
                print("   /|\    ")
                print("   / \    ")
            if turns == 0:
                print("0 turns left")
                print("SMACKK !! Be-headed Brutally")
                print("--------|-")
                print("   ___--| ")
                print("   /|\    ")
                print(" 0 / \    ")
                print(" YOU LOSE ")
                break

            





name = input("Enter your name: ")
print("Welcome", name)
print("--------------")
print("Try to guess words in (less than)< 10 attempts (:>) ")
hangman()
print()

