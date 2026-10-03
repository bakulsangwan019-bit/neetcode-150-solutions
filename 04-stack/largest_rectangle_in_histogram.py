# ============================================================
# Approach 1: Brute Force - O(n^2)
# ============================================================

heights = [7, 1, 7, 2, 2, 4]

max_area = 0

for i in range(len(heights)):
    min_height = heights[i]

    if heights[i] > max_area:
        max_area = heights[i]

    right = i + 1

    while right < len(heights):
        min_height = min(min_height, heights[right])

        width = right - i + 1
        area = min_height * width

        if area > max_area:
            max_area = area

        right += 1

print("Brute Force:", max_area)


# ============================================================
# Approach 2: Monotonic Stack - O(n)
# ============================================================

heights = [7, 1, 7, 2, 2, 4]

stack = []
max_area = 0

for i in range(len(heights)):

    start = i

    while stack and heights[i] <= stack[-1][1]:

        old_start, old_height = stack.pop()

        width = i - old_start
        area = old_height * width

        if area > max_area:
            max_area = area


        start = old_start

    stack.append((start, heights[i]))



for start, height in stack:

    width = len(heights) - start
    area = height * width

    if area > max_area:
        max_area = area

print("Monotonic Stack:", max_area)