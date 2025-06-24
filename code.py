import random
board=["_","_","_",
       "_","_","_",
       "_","_","_"]
humanplayer="X"
computerplayer="O"
Winner=None


def print_board(board):
    print(board[0] + " | ",board[1] + " | ",board[2] + " | ")
    print("---------------")
    print(board[3] + " | ",board[4] + " | ",board[5] + " | ")
    print("---------------")
    print(board[6] + " | ",board[7] + " | ",board[8] + " | ")

def player_input(board):
    while True:
        inp=int(input("Please enter your choice(1-9): "))
        if ((inp>=1 and inp<=9 and board[inp-1]=="_")):
             board[inp-1]= humanplayer
             break
        else:
            print("Oops! Player is already in that spot.")

def computer_input(board):
    while True:
        random_num=random.randint(1,8)
        if  board[random_num-1]=="_":
            board[random_num-1]=computerplayer
            break

def check_horizontal(board):
    global Winner
    if (board[0]==board[1]==board[2] and board[0]!="_"):
        Winner=board[0]
    elif (board[3]==board[4]==board[5] and board[3]!="_"):
        Winner=board[3]
    elif (board[6]==board[7]==board[8] and board[6]!="_"):
        Winner=board[6]

def check_vertical(board):
    global Winner
    if board[0] == board[3] == board[6] and board[0] != "_":
        Winner = board[0]
    elif board[1] == board[4] == board[7] and board[1] != "_":
        Winner = board[1]
    elif board[2] == board[5] == board[8] and board[2] != "_":
        Winner = board[2]

def check_diagonal(board):
    global Winner
    if board[0] == board[4] == board[8] and board[0] != "_":
        Winner = board[0]
    elif board[2] == board[4] == board[6] and board[2] != "_":
        Winner = board[2]
        
def check_tie(board):
    if "_" not in board and Winner==None:
        print_board(board)
        print("There is no winner. It's a tie.")
        exit()
        
play=input("Press enter if you want to play this game or enter q to exit:")
if play.lower()=='q':
    print("Exiting the game")
    exit()

else:
    print("Welcome to the game")

while True:
    print() 
    print_board(board)

    player_input(board)

    check_horizontal(board)
    check_vertical(board)
    check_diagonal(board)
    if Winner != None:
        print_board(board)
        print(f"The winner is {Winner}")
        break
    check_tie(board)

    computer_input(board)

    check_horizontal(board)
    check_vertical(board)
    check_diagonal(board)
    if Winner != None:
        print_board(board)
        print(f"The winner is {Winner}")
        break
    check_tie(board)
