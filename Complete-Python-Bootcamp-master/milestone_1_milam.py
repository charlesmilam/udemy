#%%
# Python A-Z Milestone Project 1
# Tic - Tac - Toe

#%%
# the board
board = [['-']*3 for x in xrange(3)]
# board

# player one?
is_player_one = True

# is the game over
game_over = False

#%%
# print the board
def print_board():
    for row in board:
        # print 'board index:', idx
        print row[0]+' '+row[1]+' '+row[2]

# print_board(board)

#%%
# get player input
def get_input():
    print 'Enter an X,Y coordinate "(X,Y)"":'
    return tuple(raw_input())

# print 'your input:', get_input()

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
    # print 'check board:'
    # print_board()
    # check tie
    if all('-' not in p for p in board):
        print "It's a tie! gg"
        return True
    # check horizontal win
    elif all(p == 'X' for p in board[0]):
        print 'X wins!'
        return True
    elif all(p == 'X' for p in board[1]):
        print 'X wins!'
        return True
    elif all(p == 'X' for p in board[2]):
        print 'X wins!'
        return True
    elif all(p == 'O' for p in board[0]):
        print 'O wins!'
        return True
    elif all(p == 'O' for p in board[1]):
        print 'O wins!'
        return True
    elif all(p == 'O' for p in board[2]):
        print 'O wins!'
        return True
    # check vertical win
    elif all(p == 'X' for p in get_col(0)):
        print 'X wins!'
        return True
    elif all(p == 'X' for p in get_col(1)):
        print 'X wins!'
        return True
    elif all(p == 'X' for p in get_col(2)):
        print 'X wins!'
        return True
    elif all(p == 'O' for p in get_col(0)):
        print 'O wins!'
        return True
    elif all(p == 'O' for p in get_col(1)):
        print 'O wins!'
        return True
    elif all(p == 'O' for p in get_col(2)):
        print 'O wins!'
        return True
    # diagonal check
    elif all(p == 'X' for p in get_diag()[0]):
        print 'X wins!'
        return True
    elif all(p == 'X' for p in get_diag()[1]):
        print 'X wins!'
        return True
    elif all(p == 'O' for p in get_diag()[0]):
        print 'O wins!'
        return True
    elif all(p == 'O' for p in get_diag()[1]):
        print 'O wins!'
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
# trial run
print_board()
while not game_over:
    place_marker(get_input(), is_player_one)
    print_board()
    if is_player_one:
        print "Player Two's turn"
        is_player_one = False
    else:
        print "Player One's turn"
        is_player_one = True

    game_over = check_state()
