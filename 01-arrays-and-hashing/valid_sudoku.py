# Valid Sudoku
# NeetCode 150 - Arrays & Hashing


# =========================================================
# Both are same VERSION
# In 1st one i just write some detail
# =========================================================

def check_rep(boa):
    for i in boa:# time - O(n)
        seen = set()
        for char in i:  # time - o(n)
            
            if char in seen and char != ".": #time - o(1)
                return False
            
            if char !=".": #time - O(1)
                seen.add(char) # aux - O(n) - worst case

        #time - O(n *n) = O(n^2) , aux = O(n)

    for j in range(len(boa)): #time - O(n)
        seen = set()
        for k in range(len(boa)): #time - O(n)
            if boa[k][j] in seen and boa[k][j] != ".":
                return False
            
            if boa[k][j] != ".":
                seen.add(boa[k][j]) #aux - O(n)

    for row in range(0 , len(boa) , 3): #time - O(n/3) - we can say this bcz we skip 3 step
        for col in range(0 , len(boa) , 3): #time - O(n/3)
            
            seen = set()

            for row_v in range(row , row+3): #time - O(3) - we can say O(3) bcz we know length - 9 
                for col_v in range(col , col+3): # time - O(3)
                    if boa[row_v][col_v] in seen and boa[row_v][col_v] != ".":
                        return False
                    seen.add(boa[row_v][col_v])

        # time - n/3*n/3*3*3 = n^2 , aux - O(n)

    return True


# so time complexity = 3n^2
# growth category = O(n^2)
#
# Peak auxiliary space for a generalized n x n board = O(n)
# because the sets are recreated and reused, not all stored together.
#
# Important:
# NeetCode Sudoku is ALWAYS 9 x 9.
# So technically for the exact problem:
# Time = O(1)
# Auxiliary Space = O(1)
#
# We use O(n^2) when thinking about a generalized board
# because it helps us understand how the algorithm scales.



# =========================================================
# CLEANER VERSION - SAME BASIC IDEA
# =========================================================
# Check:
# 1. Every row
# 2. Every column
# 3. Every 3 x 3 box
#
# Generalized Time Complexity: O(n^2)
# Generalized Auxiliary Space: O(n)
#
# For the fixed 9 x 9 Sudoku problem:
# Time Complexity: O(1)
# Auxiliary Space: O(1)


def valid_sudoku(board):

    # -------------------------
    # Check rows
    # -------------------------

    for row in board:

        seen = set()

        for value in row:

            if value == ".":
                continue

            if value in seen:
                return False

            seen.add(value)


    # -------------------------
    # Check columns
    # -------------------------

    for col in range(9):

        seen = set()

        for row in range(9):

            value = board[row][col]

            if value == ".":
                continue

            if value in seen:
                return False

            seen.add(value)


    # -------------------------
    # Check 3 x 3 boxes
    # -------------------------

    for start_row in range(0, 9, 3):

        for start_col in range(0, 9, 3):

            seen = set()

            for row in range(start_row, start_row + 3):

                for col in range(start_col, start_col + 3):

                    value = board[row][col]

                    if value == ".":
                        continue

                    if value in seen:
                        return False

                    seen.add(value)

    return True



# =========================================================
# TEST
# =========================================================

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]


print("My Version:", check_rep(board))
print("Cleaner Version:", valid_sudoku(board))