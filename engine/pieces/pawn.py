"""Pawn move generation."""


def add_pawn_moves(state, r, c, moves):
    if state.whiteToMove:
        if state.board[r - 1][c] == "--":
            moves.append(state._create_move((r, c), (r - 1, c)))
            if r == 6 and state.board[r - 2][c] == "--":
                moves.append(state._create_move((r, c), (r - 2, c)))

        if c - 1 >= 0:
            if state.board[r - 1][c - 1][0] == 'b':
                moves.append(state._create_move((r, c), (r - 1, c - 1)))
            elif (r - 1, c - 1) == state.enpassantPossible:
                moves.append(state._create_move((r, c), (r - 1, c - 1), isEnpassantMove=True))

        if c + 1 <= 7:
            if state.board[r - 1][c + 1][0] == 'b':
                moves.append(state._create_move((r, c), (r - 1, c + 1)))
            elif (r - 1, c + 1) == state.enpassantPossible:
                moves.append(state._create_move((r, c), (r - 1, c + 1), isEnpassantMove=True))
    else:
        if state.board[r + 1][c] == "--":
            moves.append(state._create_move((r, c), (r + 1, c)))
            if r == 1 and state.board[r + 2][c] == "--":
                moves.append(state._create_move((r, c), (r + 2, c)))

        if c - 1 >= 0:
            if state.board[r + 1][c - 1][0] == 'w':
                moves.append(state._create_move((r, c), (r + 1, c - 1)))
            elif (r + 1, c - 1) == state.enpassantPossible:
                moves.append(state._create_move((r, c), (r + 1, c - 1), isEnpassantMove=True))

        if c + 1 <= 7:
            if state.board[r + 1][c + 1][0] == 'w':
                moves.append(state._create_move((r, c), (r + 1, c + 1)))
            elif (r + 1, c + 1) == state.enpassantPossible:
                moves.append(state._create_move((r, c), (r + 1, c + 1), isEnpassantMove=True))
