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
    if all(p != '-' for p in board):
        print "It's a tie! gg"
        return True
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

#%%
# trial run
print_board()
while not game_over:
    place_marker(get_input(), is_player_one)
    print_board()
    if is_player_one:
        is_player_one = False
    else:
        is_player_one = True

    game_over = check_state()
    is_player_one
