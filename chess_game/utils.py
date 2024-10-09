"""
Utils file for the chess game.

"""

import chess
import numpy as np

def board_to_input(board):
    """
    Convert the board into a 3D binary matrix of shape (8, 8, 12).
    Each channel represents one piece type (6 for white, 6 for black).
    Channels:
        Index 0-5: White's pieces (P, N, B, R, Q, K)
        Index 6-11: Black's pieces (P, N, B, R, Q, K)
    
    :param board: The current state of the chessboard
    :return: A 3D numpy array representing the chessboard
    """
    board_matrix = np.zeros((8, 8, 12), dtype=np.float32)

    piece_map = board.piece_map()

    for square, piece in piece_map.items():
        # Determine the piece type index in the matrix (0 = Pawn, 1 = Knight, ... etc.)
        piece_type = piece.piece_type - 1  # 0 for P, 1 for N, ..., 5 for King
        piece_color_index = 0 if piece.color == chess.WHITE else 6  # First 6 for white, next 6 for black.

        row, col = divmod(square, 8)
        board_matrix[row, col, piece_color_index + piece_type] = 1
    
    return board_matrix