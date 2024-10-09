import chess.pgn
from chess_game.utils import board_to_input
import torch

def process_pgn(pgn_file):
    """
    Procesa un archivo PGN y extrae los estados de los tableros como ejemplos de entrenamiento.
    Esto devuelve una lista de tuplas (estado del tablero, UCI movimiento correcto).
    """
    training_data = []
    
    with open(pgn_file) as pgn:
        while True:
            game = chess.pgn.read_game(pgn)
            if game is None:
                break  #No games
            
            board = game.board()
            
            for move in game.mainline_moves():
                board_input = board_to_input(board)  
                move_index = (move.from_square * 64) + move.to_square # Codex to 64x64
                training_data.append((torch.tensor(board_input, dtype=torch.float32), move_index))
                
                board.push(move)
    
    return training_data

print(process_pgn(r'neural_network\data\Modern.pgn')) # Test
