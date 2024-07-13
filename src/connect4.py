
"""
Basis for the connect4 game based purely on the code found here
https://www3.nd.edu/~pbui/teaching/cdt.30010.fa16/project01.html 
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
            
    def find_winner(self):
        """Check to find if there is a winner on the board. Starts from the top and checks if a player piece is found, 
        then calls the check_piece function to navigate surrounding area and whether a 4 in a row of the same number is found

        Returns:
                winner number if winner found, None if not.
        """
        
        for row in range(0,5):
            for column in range(0,6):
                if self.board[row][column] == 0:
                    continue

                if self.check_piece(row, column):
                    print("Winner", self.board[row][column])   
                    return self.board[row][column]
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
     
