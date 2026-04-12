"""Rook move generation."""


def add_rook_moves(state, r, c, moves):
    enemy_color = 'b' if state.whiteToMove else 'w'
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dr, dc in directions:
        step = 1
        while True:
            end_r = r + dr * step
            end_c = c + dc * step
            if not (0 <= end_r <= 7 and 0 <= end_c <= 7):
                break

            nxt_sq = state.board[end_r][end_c]
            if nxt_sq == "--":
                moves.append(state._create_move((r, c), (end_r, end_c)))
            else:
                if nxt_sq[0] == enemy_color:
                    moves.append(state._create_move((r, c), (end_r, end_c)))
                break
            step += 1
