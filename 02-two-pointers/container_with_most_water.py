height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
largest = 0

left = 0
right = len(height) - 1

while left < right:
    
    width = right - left
    u_height = min(height[left] , height[right])


    if u_height == height[left]:
        height_ch = u_height * width

        left += 1

    if u_height == height[right]:
        height_ch = u_height * width

        right -= 1
    
    
    
    
    if height_ch > largest:
        largest = height_ch

print(largest)

    
