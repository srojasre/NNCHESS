import pygame
import os
import chess

# Load and Scale Chess Pieces
def load_pieces():
    piece_images = {}
    pieces = ['P', 'N', 'B', 'R', 'Q', 'K']  # Pawn, Knight, Bishop, Rook, Queen, King
    colors = ['w', 'b']  # White, Black

    for color in colors:
        for piece in pieces:
            image_path = rf'C:\Users\sroja\Downloads\nnChess\chess_game\resources\chess_pieces\{color}{piece}.png'
            piece_images[f'{color}{piece}'] = pygame.image.load(image_path)
            piece_images[f'{color}{piece}'] = pygame.transform.scale(piece_images[f'{color}{piece}'], (80, 80))  # Resize to fit square size

    return piece_images

# Chess Renderer Class
class ChessRenderer:
    def __init__(self, screen, tile_size=80):
        self.screen = screen
        self.tile_size = tile_size
        self.board_color_1 = (240, 217, 181)
        self.board_color_2 = (181, 136, 99)
        self.pieces = load_pieces()

    def draw_board(self):
        """Draw the chessboard (8x8 grid alternating colors)."""
        for x in range(8):
            for y in range(8):
                rect = pygame.Rect(x * self.tile_size, y * self.tile_size, self.tile_size, self.tile_size)
                if (x + y) % 2 == 0:
                    pygame.draw.rect(self.screen, self.board_color_1, rect)
                else:
                    pygame.draw.rect(self.screen, self.board_color_2, rect)

    def draw_pieces(self, board):
        """Draw chess pieces on the board."""
        piece_map = board.piece_map()
        for square, piece in piece_map.items():
            row, col = divmod(square, 8)
            piece_color = 'w' if piece.color == chess.WHITE else 'b'
            piece_type = piece.symbol().upper()  # P, N, B, etc.
            piece_image_key = f'{piece_color}{piece_type}'
            piece_image = self.pieces[piece_image_key]
            self.screen.blit(piece_image, (col * self.tile_size, row * self.tile_size))

    def highlight_square(self, square):
        """Highlight a square on the board (e.g., for selected pieces)."""
        col, row = divmod(square, 8)
        highlight_color = (124, 252, 0)  # Green
        pygame.draw.rect(self.screen, highlight_color, 
                         (row * self.tile_size, col * self.tile_size, self.tile_size, self.tile_size),
                         3)  