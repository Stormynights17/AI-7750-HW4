game_rows = 5
game_columns = 6
gameboard = [['-' for i in range(cols)] for j in range(rows)]

#first moves by players
#Player 1 (X) puts X at [3,4]
gameboard[2][3] = 'X'
#Player 2 (O) puts O at [3,3]
gameboard[2][2] = 'O'

for row in gameboard:
    print(row)

#gameboard is the starting state of the game
#turn is who's turn it is
def play_game(gameboard, turn):
    #player 1 and 2 should make moves back and forth using minimax_decision
    terminate = False
    winner = 0
    while not terminate:
        if turn == 1:
            #player 1 makes a move
            minimax_decision(gameboard, 1)
        if turn == 2:
            #player 2 makes a move
            minimax_decision(gameboard, 2)
        terminate, winner = check_game_over(gameboard)
    print('winner: ' + str(winner))

# makes a decision
def minimax_decision(state, player):
    # generate all possible moves by player who's turn, then generate for that move all possible moves by other players

def calculate_hn(state, player):
    score = 0
    #find num of 2-side-open-3-in-row
    count2side3 = two_side_open_3_in_row(state, player)



def two_side_open_3_in_row(state, player):
    me = 'X'
    if player == 2:
        me = 'O'
    count = 0

    #check vertical
    for i in range(game_columns):
        #check 0 and 4 are open
        if state[0][i] == state[4][i] == '-':
            #check 1-3 are right
            if state[1][i] == state[2][i] == state[3][i] == me:
                count += 1

    #check horizontal
    for j in range(game_rows):
        for k in range(1,3):
            #check k-1 and k+3 are open
            if state[j][k-1] == state[j][k+3] == '-':
                #check k, k+1, and k+2 are right
                if state[j][k] == state[j][k+1] == state[j][k+2] == me:
                    count += 1

    #check diagonal LtoR - must begin at [1,1] or [1,2]
    for j in range(1,3):
        if state[0][j-1] == state[4][j+3] == '-':
            if state[1][j] == state[2][j+1] == state[3][j+2] == me:
                count += 1

    #check diagonal RtoL - must begin at [1,3] or [1,4]
    for j in range(3,5):
        if state[0][j+1] == state[4][j-3] == '-':
            if state[1][j] == state[2][j-1] == state[3][j-2] == me:
                count += 1

    return count

def one_side_open_3_in_row(state, player):
    me = 'X'
    if player == 2:
        me = 'O'
    count = 0
    #check horizontal - touching edge
    for i in range(game_rows):
        if (state[i][0] == state[i][1] == state[i][2] == me) and (state[i][3] == '-'):
            count += 1
        else if (state[i][2] == '-') and (state[i][3] == state[i][4] == state[i][5] == me):
            count += 1

    #check vertical - touching edge
    for j in range(game_columns):
        if (state[0][j] == state[1][j] == state[2][j] == me) and (state[3][j] == '-'):
            count += 1
        else if (state[1][j] == '-') and (state[2][j] == state[3][j] == state[4][j] == me):
            count += 1

    #check horizontal LtoR - touching edge



#checks the gameboard for a winner (someone has 4 in a row)
def check_game_over(gameboard):
    #check horizontal
    for i in range(game_rows):
        for j in range(game_columns-3):
            countO = 0
            countX = 0
            for n in range(j, j+4):
                countX, countO = countXO(gameboard[i][n], countX, countO)
        test, player = checkXO(countX, countO)
        if test:
            return test, player

    #check vertical
    for j in range(game_columns):
        for i in range(game_rows-3):
            countO = 0
            countX = 0
            for n in range(i, i+4):
                countX, countO = countXO(gameboard[n][j], countX, countO)
            test, player = checkXO(countX, countO)
            if test:
                return test, player

    #check diagonal LtoR - must start between [0,0] and [1,2]
    for i in range(0,2):
        for j in range(0,3):
            countO = 0
            countX = 0
            for n in range(4):
                countX, countO = countXO(gameboard[i+n][j+n], countX, countO)
            test, player = checkXO(countX, countO)
            if test:
                return test, player

    #check diagonal rtoL - must start between [0,3] and [1,5]
    for i in range(0,2):
        for j in range(3,6):
            countO = 0
            countX = 0
            for n in range(4):
                countX, countO = countXO(gameboard[i-n][j-n], countX, countO)
            test, player = checkXO(countX, countO)
            if test:
                return test, player

    return False, 0

def countXO(n, countX, countO):
    if n == 'O':
        countO += 1
    elif n == 'X':
        countX +=1
    return countO, countX

def checkXO(countX, countO):
    if countX >= 4:
        return True, 1
    if countO >= 4:
        return True, 2
    else:
        return False, 0
