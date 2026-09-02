# Fixed Size Sliding Window
# Problem:
# Find the maximum sum of any subarray of size k.


# -------------------------------------------------
# Approach 1: Brute Force
# Time Complexity: O(n * k)
# Auxiliary Space: O(1)
# -------------------------------------------------

def max_sum_brute(nums, k):
    largest = None

    for i in range(len(nums) - k + 1):
        left = i
        right = i + k - 1
        current_sum = 0

        while left <= right:
            current_sum += nums[left]
            left += 1

        if largest is None or current_sum > largest:
            largest = current_sum

    return largest


nums = [4, 2, 1, 7, 8, 1, 2, 8]
k = 3

print(max_sum_brute(nums, k))   


# -------------------------------------------------
# Approach 2: Sliding Window
# First version using j for the initial window
# Time Complexity: O(n)
# Auxiliary Space: O(1)
# -------------------------------------------------

def max_sum_sliding(nums, k):
    current = 0

    left = 0
    right = left + k

    j = left

    # Cal first window
    while j <= right - 1:
        current += nums[j]
        j += 1

    largest = current


    while right < len(nums):

        current = current - nums[left] + nums[right]

        if current > largest:
            largest = current

        left += 1
        right += 1

    return largest




print(max_sum_sliding(nums, k)) 


# -------------------------------------------------
# Approach 3: Clean Sliding Window
# Time Complexity: O(n)
# Auxiliary Space: O(1)
# -------------------------------------------------

def max_sum_sliding_clean(nums, k):
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

    return largest


print(max_sum_sliding_clean(nums, k))   