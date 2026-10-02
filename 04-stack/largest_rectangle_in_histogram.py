height = [7, 1, 7, 2, 2, 4]

max_area = 0

for i in range(len(height)):
    min_height = height[i]

    if height[i] > max_area:
        max_area = height[i]

    right = i + 1

    while right < len(height):
        min_height = min(min_height, height[right])

        width = right - i + 1
        area = min_height * width

        if area > max_area:
            max_area = area

        right += 1

print(max_area)