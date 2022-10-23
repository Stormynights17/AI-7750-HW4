game_rows = 5
game_columns = 6
gameboard = [['-' for i in range(cols)] for j in range(rows)]

#first moves by players
#Player 1 (X) puts X at [3,4]
gameboard[2,3] = 'X'
#Player 2 (O) puts O at [3,3]
gameboard[2,2] = 'O'

for row in gameboard:
    print(row)

#gameboard is the starting state of the game
#turn is who's turn it is
def play_game(gameboard, turn):
    #player 1 and 2 should make moves back and forth using minimax_decision
    terminate = False
    winner = 0
    while(!terminate):
        if (turn==1):
            #player 1 makes a move
            minimax_decision(gameboard, 1)
        if (turn==2):
            #player 2 makes a move
            minimax_decision(gameboard, 2)
        terminate, winner = check_game_over(gameboard)
    print('winner: ' + str(winner))

#makes a decision
def minimax_decision(state, player):
    #generate all possible moves by player who's turn, then generate for that move all possible moves by other players

def calculate_hn(state, player):
    countX = 0
    countO = 0
    score = 0
    #find num of 2-side-open-3-in-row
    countX, countO = two_side_open_3_in_row(state)



def two_side_open_3_in_row(state):
    #check vertical
    countX = 0
    for i in range(game_columns):
        test = True
        #check 1 and 5 are not right
        if (state[0][i] != 'X' && state[4][i] != 'X'):
            #check 2-4 are right
            for j in range()




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

    #check diagonal rtoL - must start between [1,4] and [2,6]
    for i in range(1,3):
        for j in range(4,7):
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
        countO++
    elif n == 'X':
        countX++
    return countO, countX

def checkXO(counX, countO):
    if countX >= 4:
        return True, 1
    if countO >= 4:
        return True, 2
    else
        return False, 0
