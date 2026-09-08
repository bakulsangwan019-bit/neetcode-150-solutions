# Maximum Average Subarray I


# Brute Force
# Time: O(n * k)
# Space: O(1)

def max_average_brute(nums, k):
    largest = None

    for i in range(len(nums) - k + 1):
        current = 0
        left = i
        right = i + k - 1

        while left <= right:
            current += nums[left]
            left += 1

        if largest is None or current > largest:
            largest = current

    return largest / k


# Sliding Window
# Time: O(n)
# Space: O(1)

def max_average(nums, k):
    current = 0

    for i in range(k):
        current += nums[i]

    largest = current

    left = 0
    right = k

    while right < len(nums):
        current = current - nums[left] + nums[right]

        if current > largest:
            largest = current

        left += 1
        right += 1

    return largest / k


nums = [1, 12, -5, -6, 50, 3]
k = 4

print(max_average_brute(nums, k)) 
print(max_average(nums, k))        