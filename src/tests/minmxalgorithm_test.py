import unittest
from minmaxalgorithm import minmax

class TestConnect4(unittest.TestCase):
    def setUp(self):
        pass

    def test_minmax_returns_correct_move_player_2_max(self):
        """Tests does it make the next best move on a board where the best move is clear"""

        self.assertEqual(minmax(
            [[0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0], 
            [1,1,1,0,2,2,2]], 4, 2)[0] , 

            [[0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0], 
            [1,1,1,2,2,2,2]])
        
    def test_minmax_returns_correct_move_blank_player_2_max(self):
        """tests does it make the best move on an empty board"""

        self.assertEqual(minmax(
            [[0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0], 
            [0,0,0,0,0,0,0]], 4, 2)[0] , 

            [[0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0], 
            [0,0,0,2,0,0,0]])
        
    def test_minmax_returns_correct_move_player_1_min(self):
        """Tests does it make the next best move on a board where the best move is clear,
        needed for the min player since score calculations differ from max player"""

        self.assertEqual(minmax(
            [[0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0], 
            [1,1,1,0,2,2,2]], 4, 1)[0] , 

            [[0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0], 
            [1,1,1,1,2,2,2]])
        
    def test_minmax_returns_correct_move_blank_player_1_min(self):
        """tests does it make the best move on an empty board,
        needed for the min player since score calculations differ from max player"""

        self.assertEqual(minmax(
            [[0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0], 
            [0,0,0,0,0,0,0]], 4, 1)[0] , 

            [[0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0], 
            [0,0,0,1,0,0,0]])




