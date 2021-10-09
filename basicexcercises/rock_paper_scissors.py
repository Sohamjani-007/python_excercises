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


# DIDN'T UNDERSTOOD THE BELOW CODE MUCH.

print('''Please pick one:
            rock
            scissors
            paper''')

while True:
    game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
    player_a = str(input("Player a: "))
    player_b = str(input("Player b: "))
    a = game_dict.get(player_a)
    b = game_dict.get(player_b)
    dif = a - b

    if dif in [-1, 2]:
        print('player a wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    elif dif in [-2, 1]:
        print('player b wins.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break
    else:
        print('Draw.Please continue.')
        print('')



