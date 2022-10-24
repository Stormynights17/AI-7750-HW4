# AI-7750-HW4
Homework 4 for AI class 7750
Olivia LaVal, Katelyn Van Dyke, and Malek Necibi

Description of implementation:

The play_game function takes in a gameboard (with any starting moves made) and a player whose turn it is
- The function calls the two_ply_minimax if it is player 1's turn and the four_ply_minimax if it is player 2's turn
- After a player has made their move, the function calls check_game_over to see if someone has won. If so, we stop. If not, the turn marker switches to the other player and the loop restarts

The two and four ply minimax functions create a specific depth tree of nodes with possible moves for player 1 and 2, starting with the player whose turn it is and going to the max depth
- First the function finds all possible moves for the player whose turn it is on that layer (depth) of the tree
- Based on each of those moves, all possible moves for the other player are found, and so on until the max depth is reached (2 or 4)
- Then the function chooses a move based on minimax principles, so the "opponent" player minimizes the "me" player's score and the "me" player maximizes their score
- The score of a move is determined by the given heuristic

The check_game_over function is based on a chart I drew that visually represents all possible ways to win the game

The heuristic function adds up different types of desirable positions. The function finds the desirable positions based on a series of charts I drew that visually represent all possible ways to achieve that position
