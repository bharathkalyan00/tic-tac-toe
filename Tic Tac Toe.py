from IPython.display import clear_output

def display_board(board):
    print(board[7] + ' | ' + board[8]+ ' | ' + board[9])
    print('---'+'---'+'----')
    print(board[4] + ' | ' + board[5]+ ' | ' + board[6])
    print('---'+'---'+'----')
    print(board[1] + ' | ' + board[2]+ ' | ' + board[3])


#display_board(board)

def player_marker():
    mark_flag = False
    while mark_flag == False:
        marker = input("Choose player 1's marker X or O: ").upper()
        if marker in ('X','O'):
            mark_flag = True
            return marker
        else:
            print('Please choose X or O')
        continue
#marker = player_marker()
    
7
def player_pos(marker,board):
    position_flag = False
    while position_flag == False:
        position = int(input(f'Select {marker} position between 1-9: '))
        if position in range(1,10) and board[position] == ' ':
            position_flag = True
            board[position] = marker
            return position        
        else:
            print("Please choose between 1-9")
        continue
#position = player_pos(marker,board)
#display_board(board)

def win_draw(board,position,marker):
    if (board[1]==board[2]==board[3]==marker) or (board[4]==board[5]==board[6]==marker) or (board[7]==board[8]==board[9]==marker) or (board[1]==board[4]==board[7]==marker) or (board[2]==board[5]==board[8]==marker) or (board[3]==board[6]==board[9]==marker) or (board[1]==board[5]==board[9]) or (board[3]==board[5]==board[7]==marker):
        
        return True
    else:
        return False
#win_draw(board,position,marker)

def full_board_check(board):
    if ' ' not in board:
        return True
    else: 
        return False
#empty_full(board)

def space_check(board, position):
    if board[position] == ' ':
        return True
    else:
        return False





def replay():
    flag = False
    while flag == False:
        game = (input('Do you want to play again (Y or N): ')).upper()
        if game in ('Y','N'):
            if game == "Y":
                flag = True
                return True
            if game == 'N':
                return False
        else:
            print("Invalid choice")
    
#replay()





print('Welcome to Tic Tac Toe!')
game_on = True

while True:
    
    marker1 = player_marker()
    if marker1.upper() == 'X':
        marker2 = 'O'
    else:
        marker2 = 'X'
    board = [' '] * 10
    display_board(board)


    while game_on:
        #Player 1
        #marker = player_marker()
        position = player_pos(marker1,board)
        display_board(board)
        #empty = space_check(board,position)
        win_draw(board,position, marker1)
        if win_draw(board, position, marker1) == True:

            print(f"{marker1} has won!")
            replay()
            if replay() == True:
                game_on = True
                print('\n'*100)
                continue
            else:
                game_on = False
                print('\n'*100)
                print("Thanks for playing")
                break
        if full_board_check(board) == True:
            print("Draw..")
            replay()
            if replay() == True:
                game_on = True
                print('\n'*100)
                continue
            else:
                game_on = False
                print('\n'*100)
                print("Thanks for playing")
                break
        


            
            
        
        
        #player 2
        #marker2 = player_marker()
        position = player_pos(marker2,board)
        display_board(board)
        #empty = empty_full(board)
        win_draw(board,position, marker2)
        if win_draw(board, position, marker2) == True:
            print(f"{marker2} has won!")
            replay()
            if replay() == True:
                game_on = True
                print('\n'*100)
                continue
            else:
                game_on = False
                print('\n'*100)
                print("Thanks for playing")
                break
        if full_board_check(board) == True:
            print("Draw..")
            replay()
            if replay() == True:
                game_on = True
                print('\n'*100)
                continue
            else:
                game_on = False
                print('\n'*100)
                print("Thanks for playing")
                break
        else:
            continue
            
        
        

        
        





