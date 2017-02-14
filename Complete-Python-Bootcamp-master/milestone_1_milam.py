#%%
# Python A-Z Milestone Project 1
# Tic - Tac - Toe

#%%
# the board
board = [['-']*3 for x in xrange(3)]
board

#%%
# print the board
def print_board(board):
    for idx, row in enumerate(board):
        print row[0]+' '+row[1]+' '+row[2]

print_board(board)

#%%
# get player input
def get_input():
    print 'Enter an X,Y coordinate "(X,Y)"":'
    return tuple(raw_input())

print 'your input:', get_input()

#%%
# place markers on board
def place_marker(pos):
    x = int(pos[0])
    y = int(pos[1])

    board[x][y] = 'X'

#%%
# trial run
place_marker(get_input())
print_board(board)
