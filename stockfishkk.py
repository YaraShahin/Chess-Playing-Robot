from stockfish import  Stockfish

stockfish = Stockfish(r"C:\Program Files (x86)\stockfish_14.1_win_x64_avx2\stockfish_14.1_win_x64_avx2.exe")

stockfish.set_fen_position("rnbqkbnr/pppp1ppp/4p3/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2")

print(stockfish.get_best_move())