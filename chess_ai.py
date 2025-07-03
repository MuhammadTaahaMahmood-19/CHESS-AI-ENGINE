import chess
import random

PIECE_VALUES = {
    chess.PAWN: 1,
    chess.KNIGHT: 3,
    chess.BISHOP: 3,
    chess.ROOK: 5,
    chess.QUEEN: 9,
    chess.KING: 0
}

def evaluate_board(board):
    if board.is_checkmate():
        return -9999 if board.turn else 9999
    if board.is_stalemate() or board.is_insufficient_material():
        return 0

    score = 0
    for piece_type in PIECE_VALUES:
        score += len(board.pieces(piece_type, chess.WHITE)) * PIECE_VALUES[piece_type]
        score -= len(board.pieces(piece_type, chess.BLACK)) * PIECE_VALUES[piece_type]
    return score

def minimax(board, depth, alpha, beta, maximizing):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)

    legal_moves = list(board.legal_moves)

    if maximizing:
        max_eval = -float('inf')
        for move in legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def get_best_move(board, depth):
    best_move = None
    best_value = -float('inf')
    for move in board.legal_moves:
        board.push(move)
        move_value = minimax(board, depth - 1, -float('inf'), float('inf'), False)
        board.pop()
        if move_value > best_value:
            best_value = move_value
            best_move = move
    return best_move

def play_game():
    board = chess.Board()
    print(board)

    while not board.is_game_over():
        if board.turn == chess.WHITE:
            move = input("Your move (e.g., e2e4): ")
            try:
                board.push_uci(move)
            except:
                print("Invalid move. Try again.")
                continue
        else:
            print("AI is thinking...")
            move = get_best_move(board, depth=2)
            print(f"AI plays: {move}")
            board.push(move)

        print(board)

    print("Game over:", board.result())

if __name__ == "__main__":
    play_game()
