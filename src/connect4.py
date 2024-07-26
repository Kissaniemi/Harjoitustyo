from copy import deepcopy

"""
Basis for the connect4 game (first 100 lines of code) based purely on the code found here
https://www3.nd.edu/~pbui/teaching/cdt.30010.fa16/project01.html 

Lines 105-200, functions possible_moves, next_move_valid, terminal, evaluate, score_position based on the 
functions get_valid_locations, is_valid_location, is_terminal_node, evaluate_window, score_position
found https://roboticsproject.readthedocs.io/en/latest/ConnectFourAlgorithm.html (Same code also found elsewhere)
    """
    
class Connect4:
       
    def __init__(self, board = [
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0], 
                 [0,0,0,0,0,0,0]]):
        
        """Blank board given as default, possible to give another board as input.
        self.directions used in the find_winner function to navigate.
        """
        
        self.board = board
        self.directions = (
                        (-1, -1), (-1, 0), (-1, 1),
                        ( 0, -1),          ( 0, 1),
                        ( 1, -1), ( 1, 0), ( 1, 1),
                    )

    def return_current_board(self):  
        """returns current board"""
        return self.board
    
    def print_board(self):
        """prints out the current game board"""
        for row in self.board:
            print(row)
  
    def drop_piece(self, column, player): 
        """Adds a piece to the game board, takes wanted column and player number as input.
        No row information needed, adds to the next free space from the bottom row of the board.


        Returns: 
                True if move was ok, False if not
        """
    
        for row in reversed(self.board):   # reversed so that the bottom row of the matrix is handled as the 1st row (piece goes to the bottom row)
            if row[column-1] == 0:         # -1 since the columns start from 0-6 but as a player easier to think of it as 1-7      
               row[column-1] = player
               print("move ok")
               return True
        print("move not ok")
        return False 
            
    def find_winner(self, board):
        """Check to find if there is a winner on the board. Starts from the top and checks if a player piece is found, 
        then calls the check_piece function to navigate surrounding area and whether a 4 in a row of the same number is found

        Returns:
                winner number if winner found, None if not.
        """
        
        for row in range(0,5):
            for column in range(0,6):
                if board[row][column] == 0:
                    continue

                if self.check_piece(row, column):
                    print("Winner", board[row][column])   
                    return board[row][column]
        print("No winner")
        return None
    
    def check_piece(self, row, column):
        """Checks the surrounding are of a given row+column placement. uses self.directions to navigate.

        Returns:
                True if winner found, False if not
        """

        for dr, dc in self.directions:
            found_winner = True

            for i in range(1, 4):
                r = row+dr*i
                c = column +dc*i

                if r not in range(6) or c not in range(7):
                    found_winner = False
                    break

                if self.board[r][c] != self.board[row][column]:
                    found_winner = False
                    break

            if found_winner:
                return True

        return False
 
    def copy_board(self):
        """returns a deepcopy of the board"""
        return deepcopy(self.board)


    def possible_moves(self, player, board):
        """returns next possible moves for a given board"""

        boards = list()
        for i in range(1,8):
            next_board = self.next_move_valid(i, player, deepcopy(board))
            if next_board != False:
                boards.append(next_board)
                
        return boards

    def next_move_valid(self, column, player, board): 
        """returns next possible move if move possible"""

        for row in reversed(board):  
            if row[column-1] == 0:            
               row[column-1] = player
               return deepcopy(board)
        return False 
    
    def terminal(self, board):
        """checks if board is terminal (no possible moves left), returns False if there are, True if not"""

        for i in range(1,7):
            for row in reversed(board): 
                if row[i-1] == 0:   
                    return False
        return True

    def evaluate(self, window, player):   # heuristics, to be improved
        score = 0
        opp = 2
        if player == 2:
            opp = 1

        if window.count(player) == 4:
            score += 100
        elif window.count(player) == 3 and window.count(0) == 1:
            score += 5
        elif window.count(player) == 2 and window.count(0) == 2:
            score += 2
        
        if window.count(opp) == 3 and window.count(0) == 1:
            score -= 4
        
        return score
  
    def score_position(self, board, player):
        score = 0
        center = []

        # Score center column
        for i in range(0,6):
          center.append(board[i][3])
        
        center_count = center.count(player)
        score += center_count * 3

        # Score horizontal
        for r in range(6):
            row = []
            for i in range(7):
                row.append(board[r][i])
            for c in range(7-3):
                window = row[c:c+4]
                score += self.evaluate(window, player)
        
        # Score vertical
        for c in range(7):
            col = []
            for i in range(6):
                col.append(board[i][c])
            for r in range(6-3):
                window = col[r:r+4]
                score += self.evaluate(window, player)

        # Score diagonal
        for r in range(6-3):
            for c in range(7-3):
                window = [board[r+i][c+i] for i in range(4)]
                score += self.evaluate(window, player)

        for r in range(6-3):
            for c in range(7-3):
                window = [board[r+3-i][c+i] for i in range(4)]
                score += self.evaluate(window, player)
        
        if player == 1:     # This currently needed to return correct best position for the min player (1)
            return -score
        
        return score

        


