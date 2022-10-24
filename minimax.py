from copy import deepcopy
import time

class Node:
    def __init__(self, state, heuristic, children, depth):
        self.state = state
        self.heuristic = heuristic
        self.children = children
        self.depth = depth


game_rows = 5
game_columns = 6
gameboard = [['-' for i in range(game_columns)] for j in range(game_rows)]

# first moves by players
# Player 1 (X) puts X at [3,4]
gameboard[2][3] = 'X'
# Player 2 (O) puts O at [3,3]
gameboard[2][2] = 'O'

turn = 1

for row in gameboard:
    print(row)


# gameboard is the starting state of the game
# turn is who's turn it is
def play_game(state, player):
    # player 1 and 2 should make moves back and forth using minimax_decision
    terminate = False
    winner = 0
    while not terminate and state:
        if player == 1:
            # player 1 makes a move
            start = time.process_time()
            print("X's turn")
            state = two_ply_minimax(state)
            end = time.process_time()
            print("CPU time: " + str(end-start))
            for row in state:
                print(row)
            print("*************************")
            player = 2
        if player == 2:
            # player 2 makes a move
            start = time.process_time()
            print("O's turn")
            state = four_ply_minimax(state)
            end = time.process_time()
            print("CPU time: " + str(end-start))
            for row in state:
                print(row)
            print("*************************")
            player = 1

        terminate, winner = check_game_over(state)
    if winner == 1:
        print('winner: player 2')
    else:
        print('winner: player 1')


def move_available(state, i, j, player_letter):
    if state:
        if state[i][j] == '-':
            if i + 1 < 5:
                if state[i + 1][j] == player_letter:
                    return True
            if i + 1 < 5 and j + 1 < 6:
                if state[i + 1][j + 1] == player_letter:
                    return True
            if j + 1 < 6:
                if state[i][j + 1] == player_letter:
                    return True
            if i - 1 > -1 and j + 1 < 6:
                if state[i - 1][j + 1] == player_letter:
                    return True
            if i - 1 > -1:
                if state[i - 1][j] == player_letter:
                    return True
            if i - 1 > -1 and j - 1 > -1:
                if state[i - 1][j - 1] == player_letter:
                    return True
            if j - 1 > -1:
                if state[i][j - 1] == player_letter:
                    return True
            if i + 1 < 5 and j - 1 > 0:
                if state[i + 1][j - 1] == player_letter:
                    return True
        return False


# makes a decision
def two_ply_minimax(state):
    node_counter = 0
    # generate all possible moves by player
    root = Node(state, calculate_hn(state, 1), [], 0)
    node_counter += 1
    level_1_possible_moves = []
    for j in range(game_columns):
        for i in range(game_rows):
            if move_available(state, i, j, 'X'):
                level_1_possible_moves.append([i, j])
    # generate my moves - level 1
    for k in range(len(level_1_possible_moves)):
        i = level_1_possible_moves[k][0]
        j = level_1_possible_moves[k][1]
        new_state = deepcopy(state)
        new_state[i][j] = 'X'
        child = Node(new_state, 2000, [], 1)  # 2000 equals infinity
        node_counter += 1
        root.children.append(child)
    # generate level 2
    for k in range(len(root.children)):
        level_2_possible_moves = []
        for j in range(game_columns):
            for i in range(game_rows):
                if move_available(root.children[k].state, i, j, 'O'):
                    level_2_possible_moves.append([i, j])
        for l in range(len(level_2_possible_moves)):
            i = level_2_possible_moves[l][0]
            j = level_2_possible_moves[l][1]
            new_state = deepcopy(root.children[k].state)
            new_state[i][j] = 'O'
            child = Node(new_state, calculate_hn(new_state, 1), [], 2)
            node_counter += 1
            if child.heuristic < root.children[k].heuristic:
                root.children[k].heuristic = child.heuristic
            root.children[k].children.append(child)

    # we will pick move that maximizes level 1 heuristics
    temp_state = []
    temp_max = -2000

    for m in range(len(root.children)):

        if root.children[m].heuristic > temp_max:
            temp_max = root.children[m].heuristic
            temp_state = deepcopy(root.children[m].state)
    # set global game board
    print("Number of nodes generated: " + str(node_counter))
    return temp_state



def four_ply_minimax(state):
    node_counter = 0
    # generate all possible moves by player
    root = Node(state, calculate_hn(state, 1), [], 0)
    node_counter += 1
    level_1_possible_moves = []
    for j in range(game_columns):
        for i in range(game_rows):
            if move_available(state, i, j, 'O'):
                level_1_possible_moves.append([i, j])
    # generate my moves - level 1
    for k in range(len(level_1_possible_moves)):
        i = level_1_possible_moves[k][0]
        j = level_1_possible_moves[k][1]
        new_state = deepcopy(state)
        new_state[i][j] = 'O'
        child = Node(new_state, 2000, [], 1)  # 2000 equals infinity
        node_counter += 1
        root.children.append(child)
    # generate level 2
    for k in range(len(root.children)):
        level_2_possible_moves = []
        for j in range(game_columns):
            for i in range(game_rows):
                if move_available(root.children[k].state, i, j, 'X'):
                    level_2_possible_moves.append([i, j])
        for l in range(len(level_2_possible_moves)):
            i = level_2_possible_moves[l][0]
            j = level_2_possible_moves[l][1]
            new_state = deepcopy(root.children[k].state)
            new_state[i][j] = 'X'
            child = Node(new_state, calculate_hn(new_state, 1), [], 2)
            node_counter += 1
            if child.heuristic < root.children[k].heuristic:
                root.children[k].heuristic = child.heuristic
            root.children[k].children.append(child)

    # we will pick move that maximizes level 1 heuristics
    temp_state = []
    temp_max = -2000

    for m in range(len(root.children)):

        if root.children[m].heuristic > temp_max:
            temp_max = root.children[m].heuristic
            temp_state = deepcopy(root.children[m].state)
    # set global game board
    print("Number of nodes generated: " + str(node_counter))
    return temp_state


def calculate_hn(state, player):
    if state:
        score = 0
        them = 2
        if (player == 2):
            them = 1
        # find num of 2-side-open-3-in-row
        count2side3me = two_side_open_3_in_row(state, player)
        count2side3them = two_side_open_3_in_row(state, them)
        count1side3me = one_side_open_3_in_row(state, player)
        count1side3them = one_side_open_3_in_row(state, them)

        count2side2me = two_side_open_2_in_row(state, player)
        count2side2them = two_side_open_2_in_row(state, them)
        count1side2me = one_side_open_2_in_row(state, player)
        count1side2them = one_side_open_2_in_row(state, them)

        return 200 * count2side3me - 80 * count2side3them + 150 * count1side3me - 40 * count2side3them + 20 * count2side2me - 15 * count2side2them + 5 * count1side2me - 2 * count1side2them
    return None


def two_side_open_3_in_row(state, player):
    if state:
        me = 'X'
        if player == 2:
            me = 'O'
        count = 0

        # check vertical
        for i in range(game_columns):
            # check 0 and 4 are open
            if state[0][i] == state[4][i] == '-':
                # check 1-3 are right
                if state[1][i] == state[2][i] == state[3][i] == me:
                    count += 1

        # check horizontal
        for j in range(game_rows):
            for k in range(1, 3):
                # check k-1 and k+3 are open
                if state[j][k - 1] == state[j][k + 3] == '-':
                    # check k, k+1, and k+2 are right
                    if state[j][k] == state[j][k + 1] == state[j][k + 2] == me:
                        count += 1

        # check diagonal LtoR - must begin at [1,1] or [1,2]
        for j in range(1, 3):
            if state[0][j - 1] == state[4][j + 3] == '-':
                if state[1][j] == state[2][j + 1] == state[3][j + 2] == me:
                    count += 1

        # check diagonal RtoL - must begin at [1,3] or [1,4]
        for j in range(3, 5):
            if state[0][j + 1] == state[4][j - 3] == '-':
                if state[1][j] == state[2][j - 1] == state[3][j - 2] == me:
                    count += 1

        return count
    return -1


def one_side_open_3_in_row(state, player):
    me = 'X'
    if player == 2:
        me = 'O'
    count = 0
    # check horizontal - touching edge
    for i in range(game_rows):
        if (state[i][0] == state[i][1] == state[i][2] == me) and (state[i][3] == '-'):
            count += 1
        elif (state[i][2] == '-') and (state[i][3] == state[i][4] == state[i][5] == me):
            count += 1

    # check vertical - touching edge
    for j in range(game_columns):
        if (state[0][j] == state[1][j] == state[2][j] == me) and (state[3][j] == '-'):
            count += 1
        elif (state[1][j] == '-') and (state[2][j] == state[3][j] == state[4][j] == me):
            count += 1

    # check diagonal LtoR - touching edge
    startingpoint = [(1, 0), (0, 0), (0, 1), (0, 2)]
    for k in range(len(startingpoint)):
        i = startingpoint[k][0]
        j = startingpoint[k][1]
        if (state[i][j] == state[i + 1][j + 1] == state[i + 2][j + 2] == me) and (state[i + 3][j + 3] == '-'):
            count += 1
    startingpointB = [(4, 3), (4, 4), (4, 5), (3, 5)]
    for k in range(len(startingpointB)):
        i = startingpointB[k][0]
        j = startingpointB[k][1]
        if (state[i][j] == state[i - 1][j - 1] == state[i - 2][j - 2] == me) and (state[i - 3][j - 3] == '-'):
            count += 1

    # check diagonal RtoL - touching edge
    startingpointC = [(0, 3), (0, 4), (0, 5), (1, 5)]
    for k in range(len(startingpointC)):
        i = startingpointC[k][0]
        j = startingpointC[k][1]
        if (state[i][j] == state[i + 1][j - 1] == state[i + 2][j - 2] == me) and (state[i + 3][j - 3] == '-'):
            count += 1
    startingpointD = [(3, 0), (4, 0), (4, 1), (4, 2)]
    for k in range(len(startingpointD)):
        i = startingpointD[k][0]
        j = startingpointD[k][1]
        if (state[i][j] == state[i - 1][j + 1] == state[i - 2][j + 2] == me) and (state[i - 3][j + 3] == '-'):
            count += 1
    return count


def two_side_open_2_in_row(state, player):
    me = 'X'
    if player == 2:
        me = 'O'
    count = 0

    # check horizontal
    for j in range(game_rows):
        for k in range(1, 4):
            # check k-1 and k+2 are open
            if state[j][k - 1] == state[j][k + 2] == '-':
                # check k, k+1 are right
                if state[j][k] == state[j][k + 1] == me:
                    count += 1

    # check vertical
    for i in range(game_columns):
        for k in range(1, 3):
            # check k-1 and k+2 are open
            if state[k - 1][i] == state[k + 2][i] == '-':
                # check k, k+1 are right
                if state[k][i] == state[k + 1][i] == me:
                    count += 1

    # check diagonal LtoR - must begin between [1,1] and [2,2]
    for i in range(1, 3):
        for j in range(1, 3):
            if state[i - 1][j - 1] == state[i + 2][j + 2] == '-':
                if state[i][j] == state[i + 1][j + 1] == me:
                    count += 1

    # check diagonal RtoL - must begin between [1,2] and [2,4]
    for i in range(1, 3):
        for j in range(2, 5):
            if state[i - 1][j + 1] == state[i + 2][j - 2] == '-':
                if state[i][j] == state[i + 1][j - 1] == me:
                    count += 1
    return count


def one_side_open_2_in_row(state, player):
    me = 'X'
    if player == 2:
        me = 'O'
    count = 0
    # check horizontal - touching edge
    for i in range(game_rows):
        if (state[i][0] == state[i][1] == me) and (state[i][2] == '-'):
            count += 1
        if (state[i][3] == '-') and (state[i][4] == state[i][5] == me):
            count += 1

    # check vertical - touching edge
    for j in range(game_columns):
        if (state[0][j] == state[1][j] == me) and (state[2][j] == '-'):
            count += 1
        elif (state[2][j] == '-') and (state[3][j] == state[4][j] == me):
            count += 1

    # check diagonal LtoR - touching edge
    startingpoint = [(2, 0), (1, 0), (0, 0), (0, 1), (0, 2), (0, 3)]
    for k in range(len(startingpoint)):
        i = startingpoint[k][0]
        j = startingpoint[k][1]
        if (state[i][j] == state[i + 1][j + 1] == me) and (state[i + 2][j + 2] == '-'):
            count += 1
    startingpointB = [(4, 2), (4, 3), (4, 4), (4, 5), (3, 5), (2, 5)]
    for k in range(len(startingpointB)):
        i = startingpointB[k][0]
        j = startingpointB[k][1]
        if (state[i][j] == state[i - 1][j - 1] == me) and (state[i - 2][j - 2] == '-'):
            count += 1

    # check diagonal RtoL - touching edge
    startingpointC = [(0, 2), (0, 3), (0, 4), (0, 5), (1, 5), (2, 5)]
    for k in range(len(startingpointC)):
        i = startingpointC[k][0]
        j = startingpointC[k][1]
        if (state[i][j] == state[i + 1][j - 1] == me) and (state[i + 2][j - 2] == '-'):
            count += 1
    startingpointD = [(2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3)]
    for k in range(len(startingpointD)):
        i = startingpointD[k][0]
        j = startingpointD[k][1]
        if (state[i][j] == state[i - 1][j + 1] == me) and (state[i - 2][j + 2] == '-'):
            count += 1
    return count


# checks the gameboard for a winner (someone has 4 in a row)
def check_game_over(gameboard):
    test = False
    # check horizontal
    if gameboard:
        for i in range(game_rows):
            for j in range(game_columns - 3):
                countO = 0
                countX = 0
                for n in range(j, j + 4):
                    # print("horizontal: " + str(i) + " " + str(j) + " " + str(n))
                    countX, countO = countXO(gameboard[i][n], countX, countO)
                test, player = checkXO(countX, countO)
            if test:
                return test, player

        # check vertical
        for j in range(game_columns):
            countO = 0
            countX = 0
            for i in range(game_rows - 3):
                for n in range(i, i + 4):
                    # print("vertical: " + str(i) + " " + str(j) + " " + str(n))
                    countX, countO = countXO(gameboard[n][j], countX, countO)
                # print("X: " + str(countX) + " O: " + str(countO))
                test, player = checkXO(countX, countO)
                if test:
                    return test, player

        # check diagonal LtoR - must start between [0,0] and [1,2]
        for i in range(0, 2):
            for j in range(0, 3):
                countO = 0
                countX = 0
                for n in range(4):
                    # print("diagonal L to R: " + str(i) + " " + str(j) + " " + str(n))
                    countX, countO = countXO(gameboard[i + n][j + n], countX, countO)
                test, player = checkXO(countX, countO)
                if test:
                    return test, player

        # check diagonal rtoL - must start between [0,3] and [1,5]
        for i in range(0, 2):
            for j in range(3, 6):
                countO = 0
                countX = 0
                for n in range(4):
                    # print("diagonal R to L: " + str(i) + " " + str(j) + " " + str(n))
                    countX, countO = countXO(gameboard[i - n][j - n], countX, countO)
                test, player = checkXO(countX, countO)
                if test:
                    return test, player

    return False, 0


def countXO(n, countX, countO):
    if n == 'O':
        countO += 1
    elif n == 'X':
        countX += 1
    return countO, countX


def checkXO(countX, countO):
    # print("X: " + str(countX) + " O: " + str(countO))
    if countX >= 4:
        return True, 1
    if countO >= 4:
        return True, 2
    else:
        return False, 0


play_game(gameboard, turn)
