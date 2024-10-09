import chess
from chess_game.utils import board_to_input
class ChessEnv:
    def __init__(self):
        """Initialize the environment with a new chess board."""
        self.board = chess.Board()
        self.is_done = False
        self.winner = None
    
    def reset(self):
        """Reset the board."""
        self.board.reset()
        self.is_done = False
        self.winner = None
        return board_to_input(self.board)
    
    def step(self, action):
        """
        Play a move on the board.
        
        :param action: a move in UCI format (e.g., 'e2e4')
        :return: A tuple (board_state, reward, done, info)
        """
        move = chess.Move.from_uci(action)
        if move not in self.board.legal_moves:
            raise ValueError("Illegal move")

        self.board.push(move)  # Play the move
        
        # Check if the game has ended (checkmate, stalemate, etc.)
        reward = 0
        if self.board.is_checkmate():
            self.is_done = True
            self.winner = self.board.turn  # Opponent wins
            reward = 1 if not self.board.turn else -1  # +1 for white win, -1 for black win
        elif self.board.is_stalemate() or self.board.is_insufficient_material():
            self.is_done = True
            reward = 0  # Draw
        
        # Return board state
        return board_to_input(self.board), reward, self.is_done, {}
    
    def render(self):
        """Print the board to console."""
        print(self.board)

    def get_legal_moves(self):
        """Return all legal moves in UCI format."""
        return [move.uci() for move in self.board.legal_moves]
