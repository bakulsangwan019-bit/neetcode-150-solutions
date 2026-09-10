nums = [2, 3, 1, 2, 4, 3]
target = 7

mini = None
left = 0 
current = 0

for right in range(len(nums)):
    current += nums[right]


    while current >= target:
        window_len = right -left + 1

        if mini is None or mini > window_len:
            mini = window_len
        
        current -= nums[left]
        left += 1

if mini is None:
    print(0)
else:    
    print(mini)


# 2 while + while

nums = [2, 3, 1, 2, 4, 3]
target = 7

mini = None
left = 0
right = 0
current = 0

while right < len(nums):
    current += nums[right]
    right += 1

    while current >= target:
        window_len = right - left

        if mini is None or window_len < mini:
            mini = window_len

        current -= nums[left]
        left += 1

if mini is None:
    print(0)
else:
    print(mini)