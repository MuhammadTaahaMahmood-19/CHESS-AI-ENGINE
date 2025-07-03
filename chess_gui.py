import pygame
import chess
import chess.engine
from chess_ai import get_best_move  # Make sure chess_ai.py is in the same folder

# --- Constants ---
WIDTH, HEIGHT = 640, 640
SQ_SIZE = WIDTH // 8
WHITE = (255, 255, 255)
GRAY = (125, 135, 150)
DARK = (100, 100, 100)
LIGHT = (240, 217, 181)
DARK_SQ = (181, 136, 99)
FPS = 60

# --- Setup ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Chess Engine")
clock = pygame.time.Clock()

# Load piece images
PIECES = {}
PIECE_NAMES = {
    'P': 'white_pawn.png',
    'N': 'white_knight.png',
    'B': 'white_bishop.png',
    'R': 'white_rook.png',
    'Q': 'white_queen.png',
    'K': 'white_king.png',
    'p': 'black_pawn.png',
    'n': 'black_knight.png',
    'b': 'black_bishop.png',
    'r': 'black_rook.png',
    'q': 'black_queen.png',
    'k': 'black_king.png',
}

for symbol, filename in PIECE_NAMES.items():
    PIECES[symbol] = pygame.transform.scale(
        pygame.image.load(f"assets/{filename}"), (SQ_SIZE, SQ_SIZE))

# --- Game State ---
board = chess.Board()
selected_square = None
legal_moves = []

def draw_board():
    colors = [LIGHT, DARK_SQ]
    for rank in range(8):
        for file in range(8):
            color = colors[(rank + file) % 2]
            pygame.draw.rect(screen, color,
                             pygame.Rect(file * SQ_SIZE, rank * SQ_SIZE, SQ_SIZE, SQ_SIZE))

def draw_pieces():
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            row = 7 - (square // 8)
            col = square % 8
            screen.blit(PIECES[str(piece)],
                        pygame.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))

def square_clicked(pos):
    col = pos[0] // SQ_SIZE
    row = 7 - (pos[1] // SQ_SIZE)
    return chess.square(col, row)

# --- Main Game Loop ---
running = True
while running:
    clock.tick(FPS)
    draw_board()
    draw_pieces()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and board.turn == chess.WHITE:
            square = square_clicked(pygame.mouse.get_pos())
            piece = board.piece_at(square)

            if selected_square is None:
                if piece and piece.color == chess.WHITE:
                    selected_square = square
                    legal_moves = [move for move in board.legal_moves if move.from_square == square]
            else:
                move = chess.Move(selected_square, square)
                if move in legal_moves:
                    board.push(move)
                    selected_square = None
                    legal_moves = []

                    # AI Move
                    if not board.is_game_over():
                        print("AI is thinking...")
                        ai_move = get_best_move(board, depth=2)
                        board.push(ai_move)
                else:
                    selected_square = None
                    legal_moves = []

pygame.quit()
