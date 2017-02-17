#%%
# Python A-Z Milestone Project 1
# Tic - Tac - Toe



#%%
# get a new board
def get_new_board():
    return [['-']*3 for x in xrange(3)]




#%%
# print the board
def print_board():
    print
    for row in board:
        # print 'board index:', idx
        print row[0]+' '+row[1]+' '+row[2]

    print

# print_board(board)

#%%
# get player input
def get_marker_pos():
    print 'Place your marker:'
    return tuple(raw_input())

# print 'your input:', get_marker_pos()

#%%
# place markers on board
def place_marker(pos, player_one):
    x = int(pos[0])
    y = int(pos[1])

    if player_one:
        board[x][y] = 'X'
    else:
        board[x][y] = 'O'


#%%
# check the game state
def check_state():
    tie_msg = "It's a tie! gg"
    x_wins_msg = 'X wins!'
    o_wins_msg = 'O wins!'
    # check tie
    if all('-' not in p for p in board):
        print tie_msg
        return True
    # check horizontal win
    elif all(p == 'X' for p in board[0]):
        print x_wins_msg
        return True
    elif all(p == 'X' for p in board[1]):
        print x_wins_msg
        return True
    elif all(p == 'X' for p in board[2]):
        print x_wins_msg
        return True
    elif all(p == 'O' for p in board[0]):
        print o_wins_msg
        return True
    elif all(p == 'O' for p in board[1]):
        print o_wins_msg
        return True
    elif all(p == 'O' for p in board[2]):
        print o_wins_msg
        return True
    # check vertical win
    elif all(p == 'X' for p in get_col(0)):
        print x_wins_msg
        return True
    elif all(p == 'X' for p in get_col(1)):
        print x_wins_msg
        return True
    elif all(p == 'X' for p in get_col(2)):
        print x_wins_msg
        return True
    elif all(p == 'O' for p in get_col(0)):
        print o_wins_msg
        return True
    elif all(p == 'O' for p in get_col(1)):
        print o_wins_msg
        return True
    elif all(p == 'O' for p in get_col(2)):
        print o_wins_msg
        return True
    # diagonal check
    elif all(p == 'X' for p in get_diag()[0]):
        print x_wins_msg
        return True
    elif all(p == 'X' for p in get_diag()[1]):
        print x_wins_msg
        return True
    elif all(p == 'O' for p in get_diag()[0]):
        print o_wins_msg
        return True
    elif all(p == 'O' for p in get_diag()[1]):
        print o_wins_msg
        return True


#%%
# get a column from the board
def get_col(col_num):
    # print 'get col:', [board[x][col_num] for x in xrange(3)]
    return [board[x][col_num] for x in xrange(3)]

# get diagonals
def get_diag():
    dr = [board[x][x] for x in xrange(3)]
    ur = [board[x][2-x] for x in xrange(2, -1, -1)]
    return (ur, dr)


#%%
# main game routine
def play_game():
    print_board()

    # player one?
    is_player_one = True
    # is the game over
    game_over = False
    while not game_over:
        place_marker(get_marker_pos(), is_player_one)
        print_board()
        if is_player_one:
            print "O's turn"
            is_player_one = False
        else:
            print "X's turn"
            is_player_one = True

        game_over = check_state()

#%%
# play game
board = get_new_board()
play_again = True
while play_again:
    play_game()
    print 'Play again? (y/n)'
    choice = raw_input()
    if choice == 'y':
        board = get_new_board()
    elif choice == 'n':
        play_again = False
    else:
        pass
