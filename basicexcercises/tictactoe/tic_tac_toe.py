# 1.input for loop
# 2.board structure
# 3.input for 9 values
# 4.user's move , computer move
# 5.win,lose and tie
# 6.is there any free space
# 7.post work for winning.
# 8.player move
# 9.computer move

# ALGORITHM

board = [' ' for x in range(10)] # it is from 1 to 9


def insertLetter(letter, pos):
    board[pos] = letter


def space_free(pos):
    return board[pos] == ' '


def printBoard(board):
    print('  |   |  ')
    print(' ' + board[1] + '| ' + board[2] + ' | ' + board[3])
    print('  |   |  ')
    print('----------')
    print('  |   |  ')
    print(' ' + board[4] + '| ' + board[5] + ' | ' + board[6])
    print('  |   |  ')
    print('----------')
    print('  |   |  ')
    print(' ' + board[7] + '| ' + board[8] + ' | ' + board[9])
    print('  |   |  ')


def is_board_full(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def Iswinner(b,l):
    return ((b[1] == l and  b[2] == l and b[3] == l) or
    (b[4] == l and  b[5] == l and b[6] == l) or
    (b[7] == l and  b[8] == l and b[9] == l) or
    (b[1] == l and  b[4] == l and b[7] == l) or
    (b[2] == l and  b[5] == l and b[8] == l) or
    (b[3] == l and  b[6] == l and b[9] == l) or
    (b[1] == l and  b[5] == l and b[9] == l) or
    (b[3] == l and  b[5] == l and b[7] == l))


def playerMove():
    run = True
    while run:
        move = input("Select position(X) between 1 to 9 : ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if space_free(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied')
            else:
                print('Please type a number from 1 to 9')
        except:
            print('Please a type a number')


def computerMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0 ]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if Iswinner(boardcopy, let):
                move = i
                return move

    cornerOpen = []
    for i in possibleMoves:
        if i in [1 , 3 , 7 , 9]:
            cornerOpen.append(i)

    if len(cornerOpen) > 0:
        move = selectRandom(cornerOpen)
        return move
    if 5 in possibleMoves:
        move = 5
        return move
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

        if len(edgesOpen) > 0:
            move = selectRandom(edgesOpen)
            return move
    

def selectRandom(li): 
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]


def main():
    print("Welcome to TIC-TAC-TOE")

    while not(is_board_full(board)):
        if not(Iswinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print("You lost!")

        if not(Iswinner(board, 'X')):
            move = computerMove()
            if move == 0:
                print(" WHAT A GAME! GOOD JOB ")
            else:
                insertLetter('O', move)
                print('computer placed an o on position', move, ':')
                printBoard(board)
        else:
            print("YOU WIN")
            break

    if is_board_full(board):
        print("Tie Game")
    

while True:
    x = input("Do you want to play again ? (y/n) : ")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('-----------------------')
        main()
    else:
        break







