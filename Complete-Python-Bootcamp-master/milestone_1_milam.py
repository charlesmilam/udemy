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
    return raw_input()

print 'your input:', get_input()
