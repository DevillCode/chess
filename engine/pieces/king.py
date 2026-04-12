"""King move generation."""


def add_king_moves(state, r, c, moves):
    enemy_color = 'b' if state.whiteToMove else 'w'
    directions = [
        (-1, 1), (0, 1), (1, 1), (1, 0),
        (1, -1), (0, -1), (-1, -1), (-1, 0),
    ]

    for dr, dc in directions:
        end_r = r + dr
        end_c = c + dc
        if not (0 <= end_r <= 7 and 0 <= end_c <= 7):
            continue

        nxt_sq = state.board[end_r][end_c]
        if nxt_sq == "--" or nxt_sq[0] == enemy_color:
            moves.append(state._create_move((r, c), (end_r, end_c)))
