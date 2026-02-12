def checkmate(board_text: str):
    # กระดาน
    board_rows = [row.replace(" ", "").upper() for row in board_text.splitlines()]
    board_size = len(board_rows)

    if any(len(row) != board_size for row in board_rows):
        print("Board must be square")
        return

    # หมาก
    allowed_pieces = set("KPRBQ.")

    cleaned_rows = []
    for row in board_rows:
        new_row = ""
        for piece in row:
            if piece in allowed_pieces:
                new_row += piece
            else:
                new_row += "."
        cleaned_rows.append(new_row)

    board_rows = cleaned_rows

    # ตำแหน่ง King
    king_positions = [
        (r, c)
        for r in range(board_size)
        for c in range(board_size)
        if board_rows[r][c] == "K"
    ]

    if len(king_positions) == 0:
        print("Where is your King?")
        return

    if len(king_positions) > 1:
        print("How did you manage to have more than one King?")
        return

    king_row, king_col = king_positions[0]
    
    #ชื่อหมากตอน checkmate
    piece_names = {
    "P": "Pawn",
    "R": "Rook",
    "B": "Bishop",
    "Q": "Queen"
}


    # ขอบกระดาน
    def korb_board(row, col):
        return 0 <= row < board_size and 0 <= col < board_size

    # pawn
    for col_offset in (-1, 1):
        pawn_row = king_row + 1
        pawn_col = king_col + col_offset

        if korb_board(pawn_row, pawn_col) and board_rows[pawn_row][pawn_col] == "P":
            print(f"Success checkmate by {piece_names['P']}")
            return

    # Scan (Rook / Bishop / Queen)
    def scan_directions(directions, target_pieces):
        for row_step, col_step in directions:
            scan_row = king_row + row_step
            scan_col = king_col + col_step

            while korb_board(scan_row, scan_col):
                piece = board_rows[scan_row][scan_col]

                if piece != ".":
                    if piece in target_pieces:
                        return piece   
                    else:
                        break

                scan_row += row_step
                scan_col += col_step

        return None   
    # Rook / Queen +
    attacker = scan_directions(
        directions=[(-1,0),(1,0),(0,-1),(0,1)],
        target_pieces="RQ"
    )
    if attacker:
         print(f"Success checkmate by {piece_names[attacker]}")
         return

    # Bishop / Queen X
    attacker = scan_directions(
        directions=[(-1,-1),(-1,1),(1,-1),(1,1)],
        target_pieces="BQ"
    )
    if attacker:
         print(f"Success checkmate by {piece_names[attacker]}")
    return

    print("Fail")
