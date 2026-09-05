# Container With Most Water


# Approach 1 - Brute Force

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
largest = 0

for i in range(len(height)):
    for j in range(i+1 , len(height)):
        width = j - i
        height_che = min(height[i] , height[j])

        wsable_height = width * height_che

        if wsable_height > largest:
            largest = wsable_height

print(largest)


# Time Complexity: O(n^2)
# Auxiliary Space: O(1)



# Approach 2 - Two Pointers

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
largest = 0

left = 0
right = len(height) - 1

while left < right:

    width = right - left
    u_height = min(height[left] , height[right])

    height_ch = u_height * width

    if u_height == height[left]: # or we directly use if height[left] < height[right]
        left += 1

    if u_height == height[right]:
        right -= 1

    if height_ch > largest:
        largest = height_ch

print(largest)


# Time Complexity: O(n)
# Auxiliary Space: O(1)