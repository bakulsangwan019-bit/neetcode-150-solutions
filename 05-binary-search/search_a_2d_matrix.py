# ============================================================
# Search a 2D Matrix
# Approach 1: Flatten Matrix + Binary Search
# Time: O(m * n)
# Space: O(m * n)
# ============================================================

matrix = [
    [1, 2, 4, 8],
    [10, 11, 12, 13],
    [14, 20, 30, 40]
]

target = 14

new = []

for row in matrix:
    for value in row:
        new.append(value)

left = 0
right = len(new) - 1
ans = False

while left <= right:
    mid = (left + right) // 2

    if new[mid] == target:
        ans = True
        break

    elif new[mid] > target:
        right = mid - 1

    else:
        left = mid + 1

print("Flatten + Binary Search:", ans)


# ============================================================
# Approach 2: Binary Search Directly on Matrix
# Time: O(log(m * n))
# Space: O(1)
# ============================================================

matrix = [
    [1, 2, 4, 8],
    [10, 11, 12, 13],
    [14, 20, 30, 40]
]

target = 14

rows = len(matrix)
cols = len(matrix[0])

left = 0
right = rows * cols - 1
ans = False

while left <= right:
    mid = (left + right) // 2

    row = mid // cols
    col = mid % cols

    if matrix[row][col] == target:
        ans = True
        break

    elif matrix[row][col] > target:
        right = mid - 1

    else:
        left = mid + 1

print("Direct Matrix Binary Search:", ans)