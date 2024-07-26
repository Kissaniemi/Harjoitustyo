from connect4 import Connect4

def minmax(node, depth=4, player=2):
    """MinMax algorithm (currently without alpha-beta pruning)
    based on the wikipedia pseudocode for minmax algorithm https://en.wikipedia.org/wiki/Minimax, 
    with additions based on the minmax algorithm from https://roboticsproject.readthedocs.io/en/latest/ConnectFourAlgorithm.html (Same code also found elsewhere)

    Args:
        node: board position to start from
        player: which players turn, min is 1, max is 2. Defaults to 2.
        depth: search depth, Defaults to 4.
        
    Returns:
        new_move: The best next move (board)
        value: The heuristic value of the move (board)

    """
    
    game = Connect4()
    moves = game.possible_moves(player, node)
    terminal_node = game.terminal(node)

    if depth == 0 or terminal_node:
        if terminal_node:
            node_value = game.find_winner(node)

            if node_value == 2:
                return (None, float("inf"))
            
            elif node_value == 1:
                return (None, float("-inf"))

            else:
                return (None, 0)
                
        else:
            return (None, game.score_position(node, player))
    
 
    if player == 2:  #Max player
        value = float("-inf")
        for move in moves:
            new_value = minmax(move, depth -1, 1)[1]
            if new_value > value:
                value = new_value
                next_move = move 

        return next_move, value
    
    else: # Min player
        value = float("inf")
        for move in moves:    
            new_value = minmax(move, depth -1, 2)[1]
            if new_value < value:
                value = new_value
                next_move = move

        return next_move, value