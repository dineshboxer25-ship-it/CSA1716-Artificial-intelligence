def solve(row, cols, diag1, diag2, board):
    if row == 8:
        for r in board:
            print(" ".join("Q" if c == r else "." for c in range(8)))
        return True

    for col in range(8):
        if col not in cols and row-col not in diag1 and row+col not in diag2:
            if solve(row+1, cols | {col}, diag1 | {row-col},
                     diag2 | {row+col}, board+[col]):
                return True
    return False

solve(0, set(), set(), set(), [])
