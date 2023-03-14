### oskaplayer ###
### Ranxin Li ###
### May. 19th. 2022 ###
### ECS 170, SQ 2022 ###
import copy
import math
#This is the entrance of this project
#   input argument
#     list_string: board 
#     side:  whose turn w or b 
#     ahead: deapth to thinking
#   Return
#       the best next move
def osakaplayer(list_string, side, ahead):
    #the win_number is a global variable for winning side
    global win_number
    win_number=(len(list_string)-1)*(len(list_string))+1
    
    if len(movegen(list_string,side))==0:
        return list_string
    if side=='w':
        return maxmin(list_string, 'w', side, ahead)[0]
    if side=='b':
        return maxmin(list_string, 'b', side, ahead)[0]
    
#This function use recursion to find the best move and the minmax value certain steps ahead or the game end
#   input argument
#       state: the current board
#       firstgoes: which side goes first
#       depth: the number of recursion
#   Return
#       a tuple (bestmove, value of static board evaluation)
def maxmin(state, firstgoes, side, depth):
    win_side=wingame(state)
    if win_side=='draw':
        return (None, 0)
    if win_side[0] or win_side[1] or depth==0:
        return (None, staticboardeval(state,firstgoes))
    if len(movegen(state, side))==0:
        if side=='w':
            return maxmin(state, firstgoes, 'b',depth-1)
        if side=='b':
            return maxmin(state, firstgoes, 'w', depth-1)
    next_states=movegen(state,side)
    best_move=state
    if firstgoes=='w':
        if side=='w':
            h_value=-math.inf
            
            for new_state in next_states:
                value=maxmin(new_state, firstgoes, 'b', depth-1)[1]
                if value>h_value:
                    h_value=value
                    best_move=new_state
            return (best_move, h_value)
        if side=='b':
            h_value=math.inf
            
            for new_state in next_states:
                value=maxmin(new_state, firstgoes, 'w',depth-1)[1]
                if value<h_value:
                    h_value=value
                    best_move=new_state
            return (best_move, h_value)
        
    if firstgoes=='b':
        if side=='b':
            h_value=-math.inf
            for new_state in next_states:
                value=maxmin(new_state, firstgoes, 'w',depth-1)[1]
                if value>h_value:
                    h_value=value
                    best_move=new_state
            return (best_move, h_value)
        if side=='w':
            h_value=math.inf
            for new_state in next_states:
                value=maxmin(new_state, firstgoes, 'b',depth-1)[1]
                if value<h_value:
                    h_value=value
                    best_move=new_state
            return (best_move, h_value)
                    
#This function evaluate the heuristic value of the board
#heuristic value:(number of player's pieces-number of opponent's pieces)+(the sum of opponent's steps to the goal)-(the sum of the player's stpes to the goal)
#   Input argument
#       board: the curruent status
#       side: which one to move
#   Return
#       the heuristic value according to the side
def staticboardeval(board, side):
    win_side=wingame(board)
    if side=='w':
        if win_side[0]:
            return win_number
        if win_side[1]:
            return -win_number
    if side=='b':
        if win_side[0]:
            return -win_number
        if win_side[1]:
            return win_number
    num_of_white=0
    num_of_black=0
    white_distance=0
    black_distance=0
    first_line=0
    bottom_line=len(board)-1

    for i in range(len(board)):
        for piece in board[i]:
            if piece=='w':
                num_of_white+=1
                white_distance+=(bottom_line-i)
            elif piece=='b':
                num_of_black+=1
                black_distance+=(i-first_line)
    if side=='w':
        
        h=(num_of_white-num_of_black)+black_distance-white_distance
        return h
        
    if side=='b':
        
        h=(num_of_black-num_of_white)+white_distance-black_distance
        return h
    
#This function judge whether the static board is a win status or not
#   Input argument:
#       board: the current status
#   Local variables to be return:
#       b_win: whether black side wins
#       w_win: whether white side wins
#   Return:
#       a tuple: (w_win, b_win) if one side wins
#       string: 'draw' if neither side or both sides wins
    
def wingame(board):
    #set initial to be false because if there is no b on the bottom, then b_win will be false
    b_win=False
    num_of_b=0
    for piece in board[0]:
        if piece=='b':
            b_win=True
            num_of_b+=1
    for i in range(1, len(board)):
        for piece in board[i]:
            if piece=='b':
                b_win=False
                num_of_b+=1
    w_win=False
    num_of_w=0
    for piece in board[len(board)-1]:
        if piece=='w':
            w_win=True
            num_of_w+=1
    for i in range(0, len(board)-2):
        for piece in board[i]:
            if piece=='w':
                w_win=False
                num_of_w+=1
    #when both side win, which side that has more pieces wins
    if w_win and b_win:
        #because both value is True, set the less piece side to be false
        if num_of_w>num_of_b:
            b_win=False
        elif num_of_b>num_of_w:
            w_win=False
        else:
            return "draw"
        
    if not w_win and not b_win:
        if len(movegen(board, 'w'))==0 and len(movegen(board,'b'))==0:
            if num_of_w>num_of_b:
                w_win=True
            elif num_of_b>num_of_w:
                b_win=True
            else:
                return "draw"
        
    return (w_win, b_win)

############################homework3 begin##############################


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

############################homework3 end##############################

####################This part is for testing######################################
#print(osakaplayer(['----','w--','bw','w-b','----'], 'b', 13))
#print(osakaplayer(['www-','bb-','--','--w','----'], 'b', 2))
#print(osakaplayer(['b---','---','-w','w-b','----'], 'w', 2))
#print(osakaplayer(['b---','---','-w','--b','w---'], 'b', 1))
#print(win_game(['b---','-b-','--','---','w---']))
#print(win_number)
#print(osakaplayer(['----','-w-','bw','-b-','----'],'w',2))
print(osakaplayer(['----','-w-','bb','-w-','----'], 'w', 5))
#print(osakaplayer(['----','b-w','w-','--b','----'], 'w', 13))
#print(osakaplayer(['----','-wb','b-','-w-','--w-'],'b',3))
