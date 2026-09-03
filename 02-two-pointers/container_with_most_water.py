# Container With Most Water


# Approach 1 - Brute Force
# Check every possible pair

def max_area_brute(height):

    largest_area = 0

    for i in range(len(height)):
        for j in range(i + 1, len(height)):

            width = j - i
            usable_height = min(height[i], height[j])

            area = width * usable_height

            if area > largest_area:
                largest_area = area

    return largest_area


# Time Complexity: O(n^2)
# Auxiliary Space: O(1)



# Approach 2 - Two Pointers

def max_area(height):

    left = 0
    right = len(height) - 1

    largest_area = 0

    while left < right:

        width = right - left
        usable_height = min(height[left], height[right])

        area = width * usable_height

        if area > largest_area:
            largest_area = area

        if height[left] < height[right]:
            left += 1

        else:
            right -= 1

    return largest_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

print(max_area(height))


# Time Complexity: O(n)
# Auxiliary Space: O(1)