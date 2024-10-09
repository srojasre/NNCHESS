import pygame
from chess_game.game import ChessEnv
from chess_game.renderer import ChessRenderer
import chess

# ===== Initialize pygame =====
# Initialize pygame
pygame.init()
# =============== Pre-game setup ===============
TILE_SIZE = 80
BOARD_SIZE = TILE_SIZE * 8
INFO_PANEL_WIDTH = 200
WINDOW_WIDTH = BOARD_SIZE + INFO_PANEL_WIDTH
WINDOW_HEIGHT = BOARD_SIZE

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Chess Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GREY = (200, 200, 200)

def draw_info_panel(screen, font, env, move_history):
    """Render game information to the right of the chessboard."""
    
    pygame.draw.rect(screen, LIGHT_GREY, (BOARD_SIZE, 0, INFO_PANEL_WIDTH, WINDOW_HEIGHT))


    # ======= Right panel =======
    
    label = font.render("Game Info", True, BLACK)
    screen.blit(label, (BOARD_SIZE + 20, 20))
    turn_text = "Turn: White" if env.board.turn == chess.WHITE else "Turn: Black"
    turn_label = font.render(turn_text, True, BLACK)
    screen.blit(turn_label, (BOARD_SIZE + 20, 50))
    move_label = font.render("Move History:", True, BLACK)
    screen.blit(move_label, (BOARD_SIZE + 20, 90))

    offset_y = 120
    for i, move in enumerate(move_history[-10:]):
        move_text = f"{i + 1}: {move}"
        move_entry = font.render(move_text, True, BLACK)
        screen.blit(move_entry, (BOARD_SIZE + 20, offset_y))
        offset_y += 20

def main():
    # Create chess environment and renderer
    env = ChessEnv()
    renderer = ChessRenderer(screen, TILE_SIZE)

    # Initialize font
    font = pygame.font.SysFont(None, 24)

    # Initialize some variables for the game loop
    running = True
    selected_square = None  # None means no piece is selected
    possible_moves = []
    move_history = []
    
    state = env.reset()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                # If click inside the board area
                if x < BOARD_SIZE:
                    clicked_square = (y // TILE_SIZE) * 8 + (x // TILE_SIZE)  # Convert mouse click to square index
                    
                    # Check if a square is already selected
                    if selected_square is None:
                        piece = env.board.piece_at(clicked_square)
                        if piece is not None and piece.color == env.board.turn:
                            selected_square = clicked_square
                            possible_moves = [move for move in env.board.legal_moves if move.from_square == selected_square]
                    else:
                        action = None
                        for move in possible_moves:
                            if move.to_square == clicked_square:
                                action = move.uci()
                                break
                        
                        if action:
                            # Make a move
                            state, reward, done, _ = env.step(action)

                            # Append move to history
                            move_history.append(env.board.peek().uci())
                            
                            # Clear selection and possible moves
                            selected_square = None
                            possible_moves = []
                            
                            if done:
                                print("Game Over!")
                                running = False
                        else:
                            # Deselect if invalid move
                            selected_square = None
                            possible_moves = []

        # ====== Render the board and the pieces ======
        renderer.draw_board()
        renderer.draw_pieces(env.board)

        if selected_square is not None:
            renderer.highlight_square(selected_square)

        # ====== Render the info panel on the right ======
        draw_info_panel(screen, font, env, move_history)

        pygame.display.flip() #60 is okay

    pygame.quit()

if __name__ == "__main__":
    main()
