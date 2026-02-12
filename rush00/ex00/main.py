from checkmate import checkmate


def main():
    print("=== Test 1: Rook checking King ===")
    board1 = """\
.R..
.K..
....
....\
"""
    checkmate(board1)

    print("=== Test 2: No check ===")
    board2 = """\
R...
....
..K.
....\
"""
    checkmate(board2)

    print("=== Test 3: Bishop check ===")
    board3 = """\
B...
....
..K.
....\
"""
    checkmate(board3)

    print("=== Test 4: Pawn check ===")
    board4 = """\
....
....
.k..
..p.\
"""
    checkmate(board4)

    print("=== Test 5: Blocked attack ===")
    board5 = """\
R.P.
.K..
....
....\
"""
    checkmate(board5)


if __name__ == "__main__":
    main()
