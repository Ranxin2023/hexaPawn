import copy

### oskaplayer ###

# This function generate the movement, it is main function
#   input argument 
#     state: a board 
#     side: whose turn , 'b' or 'w' 
#   Return
#     new_states: list of all new chessboards that can be generated      
def movegen(state, side):
    new_states=list()
    mid=len(state)//2
    #white's turn
    if side=='w':
        for i in range(len(state)-1):
            for j in range(len(state[i])):
                if state[i][j]=='w':
                    #on the upper of chessboard
                    if i<mid:
                        #left direction
                        if j>0:
                            #1 step to the left
                            if state[i+1][j-1]=='-':
                                changestate(new_states, state, i, j, 1, -1, 0, 0)
                            #take opponent pieces to the left
                            elif state[i+1][j-1]=='b':
                                if i==mid-1:
                                    if state[i+2][j-1]=='-':
                                        changestate(new_states, state, i, j, 2, -1, 1, -1)
                                
                                else:
                                    #cannot take opponent's piece when j euqals to 1
                                    if j>1 and state[i+2][j-2]=='-':
                                        changestate(new_states, state, i, j, 2, -2, 1, -1)
                        #right direction
                        if j<len(state[i])-1:
                            #1 step to the right
                            if state[i+1][j]=='-':
                                changestate(new_states, state, i, j, 1, 0, 0, 0)
                            elif state[i+1][j]=='b':
                                if i==mid-1:
                                    if state[i+2][j+1]=='-':
                                        changestate(new_states, state, i, j, 2, 1, 1, 0)
                                else:
                                    #cannot take opponent's piece when j euqals to len minus 2
                                    if j<len(state[i])-2 and state[i+2][j]=='-':
                                        changestate(new_states, state, i, j, 2, 0, 1, 0)

                    #on the lower of chessboard
                    else:
                        #left direction
                        #1 step to the left
                        if state[i+1][j]=='-':
                            changestate(new_states, state, i, j, 1, 0, 0, 0)
                        elif state[i+1][j]=='b':
                            #cannot take opponent's piece when i equals to len minus 2
                            if i<len(state)-2 and state[i+2][j]=='-':
                                changestate(new_states, state, i, j, 2, 0, 1, 0)
                        #right direction
                        #1 step to the right
                        if state[i+1][j+1]=='-':
                            changestate(new_states, state, i, j, 1, 1, 0, 0)
                        elif state[i+1][j+1]=='b':
                            #cannot take opponent's piece when i equals to len minus 2
                            if i<len(state)-2 and state[i+2][j+2]=='-':
                                changestate(new_states, state, i, j, 2, 2, 1, 1)
    #black's turn
    if side=='b':
        for i in range(1, len(state)):
            for j in range(len(state[i])):
                if state[i][j]=='b':
                    #on the lower of chessboard
                    if i>mid:
                        #left direction
                        if j>0:
                            #1 step to the left
                            if state[i-1][j-1]=='-':
                                changestate(new_states, state, i, j, -1, -1, 0, 0)
                            #eat opponent pieces to the left
                            elif state[i-1][j-1]=='w':
                                if i==mid+1:
                                    if state[i-2][j-1]=='-':
                                        changestate(new_states, state, i, j, -2, -1, -1, -1)
                                else:
                                    #cannot take opponent's piece when j euqals to 1
                                    if j>1 and state[i-2][j-2]=='-':
                                        changestate(new_states, state, i, j, -2, -2, -1, -1)
                        #right direction
                        if j<len(state[i])-1:
                            #1 step to the right
                            if state[i-1][j]=='-':
                                changestate(new_states, state, i, j, -1, 0, 0, 0)
                            elif state[i-1][j]=='w':
                                if i==mid+1:
                                    if state[i-2][j+1]=='-':
                                        changestate(new_states, state, i, j, -2, 1, -1, 0)
                                else:
                                    #cannot take opponent's piece when j euqals to len minus 2
                                    if j<len(state[i])-2 and state[i-2][j]=='-':
                                        changestate(new_states, state, i, j, -2, 0, -1, 0)

                    #on the upper of chessboard
                    else:
                        #left direction
                        #1 step to the left
                        if state[i-1][j]=='-':
                            changestate(new_states, state, i, j, -1, 0, 0, 0)
                        elif state[i-1][j]=='w':
                            if i>1 and state[i-2][j]=='-':
                                changestate(new_states, state, i, j, -2, 0, -1, 0)
                        #right direction
                        #1 step to the right
                        if state[i-1][j+1]=='-':
                            changestate(new_states, state, i, j, -1, 1, 0, 0)
                        elif state[i-1][j+1]=='w':
                            #cannot take opponent's piece when i equals to 1
                            if i>1 and state[i-2][j+2]=='-':
                                changestate(new_states, state, i, j, -2, 2, -1, 1)
    return new_states
                
            

#This function convert the list strings into 2-dimension array
#  Input
#    list_strings : list strings of board
#  Return 
#    ret : 2-dimension array              
def converttoboard(list_strings):
    ret=list()
    for one_list in list_strings:
        grid_list=list()
        for grid in one_list:
            grid_list.append(grid)
        ret.append(grid_list)
    return ret

#This function convert the list (2-dimension array) into list strings
#  Input
#    board : list strings of board
#  Return 
#    ret : list strings of board    
def converttoliststrings(board):
    ret=list()
    for i in range(len(board)):
        string_list=""
        for grid in board[i]:
            string_list+=grid
        ret.append(string_list)
    return ret

#This function is for changing the grid on the chessboard
#  Input
#    new_states : list strings of board
#    states : list strings of board
#    i: position on row before moving
#    j: position on row before moving
#    i_offset: step of moving on row  
#    j_offset: step of moving on column 
#    i_captured_offset: relative position of piece being captured 
#    j_captured_offset: relative position of piece being captured  
#  Return 
#    (none) 
def changestate(new_states, state,i, j, i_offset, j_offset, i_captured_offset, j_captured_offset):
    state_copy=converttoboard(state)
    state_copy[i][j], state_copy[i+i_offset][j+j_offset]=state_copy[i+i_offset][j+j_offset], state_copy[i][j]
    if i_captured_offset or j_captured_offset:
        state_copy[i+i_captured_offset][j+j_captured_offset]='-'
    string_state_copy=converttoliststrings(state_copy)
    new_states.append(string_state_copy)
