board = [' ' for _ in range(9)]


def board_print ():
    # print("   |   |")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("___|___|___")
    print("   |   |")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("___|___|___")
    print("   |   |")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("   |   |")


# def is_winner (mark):
#     if ((board[0] == mark and board[1] == mark and board[2]==mark) or 
#     (board[3] == mark and board[4] == mark and board[5]==mark) or 
#     (board[6] == mark and board[7] == mark and board[8]==mark) or 
#     (board[0] == mark and board[4] == mark and board[8]==mark) or 
#     (board[2] == mark and board[4] == mark and board[6]==mark) or 
#     (board[0] == mark and board[3] == mark and board[6]==mark) or 
#     (board[1] == mark and board[4] == mark and board[7]==mark) or 
#     (board[2] == mark and board[5] == mark and board[8]==mark)):
#         return True
#     else :
#         return False
    

def is_winner(mark):
    for i in range(0, 9, 3):
        if board[i:i+3] == [mark]*3:
            return True
    for i in range(3):
        if board[i::3] == [mark]*3:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == mark:
        return True
    if board[2] == board[4] == board[6] == mark:
        return True
    return False    
    
    
def is_board_full():
    return ' ' not in board
    
def play_game():
    board_print()
    while True:
        player1_choice = int(input("Player 1 (X) choose a position (1-9)"))-1
        if board[player1_choice] == ' ':
            board[player1_choice] = 'X'
        else:
            print("That position is already taken!")
            continue
        board_print()
        
        if is_winner('X'):
            print("Player 1 wins!")
            break
        if is_board_full():
            print("Tie game!")
            break
        
        
        player2_choice = int(input("Player 2 (O) choose a position (1-9)"))-1
        if board[player2_choice] == ' ':
            board[player2_choice] = 'O'
        else:
            print("That position is already taken!")
            continue
        board_print()
        
        if is_winner('O'):
            print("Player 2 wins!")
            break
        if is_board_full():
            print("Tie game!")
            break
        
        
play_game()