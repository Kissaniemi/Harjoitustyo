import unittest
from connect4 import Connect4

class TestConnect4(unittest.TestCase):
    def setUp(self):
        pass

    def test_board_default_ok(self):
        """tests that the default board is initiated
        """
        game = Connect4()
        self.assertEqual(game.board , [
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0], 
                 [0,0,0,0,0,0,0]])
        
    def test_board_input_ok(self):
        """tests that the input board is initiated
        """
        game = Connect4(
                [[0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,2,0,0],
                 [0,0,0,2,1,2,0],
                 [0,0,2,1,2,2,0], 
                 [0,2,1,2,2,1,0]])
        
        self.assertEqual(game.board , 
                [[0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,2,0,0],
                 [0,0,0,2,1,2,0],
                 [0,0,2,1,2,2,0], 
                 [0,2,1,2,2,1,0]])
        

    def test_no_winner_blank(self):
        """tests that the find_winner function doesn't return a winner when there is a blank board"""
        game = Connect4()
        self.assertEqual(game.find_winner([
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0], 
                 [0,0,0,0,0,0,0]]), None)

    
    def test_no_winner_3in_line(self):
        """tests that the find_winner function doesn't return a winner when there is less than 4 (3) in a row"""
        game = Connect4(
            [[0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,1,0,0,0],
            [0,0,0,1,0,0,0], 
            [0,0,0,1,0,0,0]])
        self.assertEqual(game.find_winner(
            [[0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,1,0,0,0],
            [0,0,0,1,0,0,0], 
            [0,0,0,1,0,0,0]]), None)

    def test_winner_vertical(self):
        """tests that the find_winner function returns winner when there is 4 in a row (vertical)"""
        game = Connect4()
        self.assertEqual(game.find_winner(
            [[0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,1,0,0,0],
            [0,0,0,1,0,0,0],
            [0,0,0,1,0,0,0], 
            [0,0,0,1,0,0,0]]), 1)

    def test_winner_horizontal(self):
        """tests that the find_winner function returns winner when there is 4 in a row (horizontal)"""
        game = Connect4([
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0], 
                 [0,0,1,1,1,1,0]])
        self.assertEqual(game.find_winner([
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0], 
                 [0,0,1,1,1,1,0]]), 1)

    def test_winner_diagonal(self):
        """tests that the find_winner function returns winner when there is 4 in a row (diagonal)"""
        game = Connect4([
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,1,0],
                 [0,0,0,0,2,0,0],
                 [0,0,0,2,0,0,0],
                 [0,0,2,0,0,0,0], 
                 [0,2,0,0,0,0,0]])
        
        self.assertEqual(game.find_winner([
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,1,0],
                 [0,0,0,0,2,0,0],
                 [0,0,0,2,0,0,0],
                 [0,0,2,0,0,0,0], 
                 [0,2,0,0,0,0,0]]), 2)


    def test_winner_horizontal(self):
        """tests that the find_winner function doesn't return winner when there is 3 pieces on board that sum to 4"""
        game = Connect4([
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,1,0,0,0], 
                 [0,0,1,2,0,0,0]])
        self.assertEqual(game.find_winner([
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,1,0,0,0], 
                 [0,0,1,2,0,0,0]]), None)

    def test_piece_drop(self):
        """tests that the add_piece function works"""
        game = Connect4()
        game.drop_piece(4,2)
        self.assertEqual(game.board, [
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0],
                 [0,0,0,0,0,0,0], 
                 [0,0,0,2,0,0,0]])