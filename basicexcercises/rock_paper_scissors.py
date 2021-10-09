import sys

user1 = input("Hi,Player1 : What's your name : ")
user2 = input("Hi,Player2 : What's your name : ")
user1_answer = input("%s, do yo want to choose rock, paper or scissors?" % user1)
user2_answer = input("%s, do you want to choose rock, paper or scissors?" % user2)


def play(u1, u2):
    if u1 == u2:
        return("~~ Tie ~~")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return("Rock Wins!")
        else:
            return("Paper Wins!")
    elif u1 == 'scissor':
        if u2 == 'paper':
            return("Scissors win!")
        else:
            return("Rock wins")
    elif u1 == 'rock':
        if u2 == 'paper':
            return("Paper wins!")
        else:
            return("Scissor wins!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()

print(play(user1_answer, user2_answer))



