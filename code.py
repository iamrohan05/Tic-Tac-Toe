board=["_","_","_",
       "_","_","_",
       "_","_","_"]
currentplayer="X"
computerplayer="O"
Winner=None
Game_running=True

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
             board[inp-1]= currentplayer
             break
        else:
            print("Oops! Player is already in that spot.")

while Game_running:
    print_board(board)
    player_input(board)




  