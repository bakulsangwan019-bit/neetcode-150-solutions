# Two Sum II - Input Array Is Sorted
# LeetCode 167


# =========================================================
# Approach 1: Brute Force
# =========================================================
# Check every possible pair.
#
# Time Complexity: O(n^2)
# Auxiliary Space: O(1)
# =========================================================

def two_sum_brute_force(numbers, target):

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):

            if numbers[i] + numbers[j] == target:
                return (i + 1, j + 1)

    return "Not Found"


# =========================================================
# Approach 2: Hash Map
# =========================================================
# Store each number with its index.
#
# For every number:
#     needed = target - current number
#
# If needed was already seen, we found the pair.
#
# This works in O(n) time, but requires O(n) extra space.
# It does NOT take advantage of the fact that the array
# is already sorted.
#
# Time Complexity: O(n)
# Auxiliary Space: O(n)
# =========================================================

def two_sum_hashmap(numbers, target):

    seen = {}

    for i, num in enumerate(numbers):

        needed = target - num

        if needed in seen:
            return (seen[needed] + 1, i + 1)

        seen[num] = i

    return "Not Found"


# =========================================================
# Approach 3: Two Pointers
# =========================================================
# Because the input array is sorted, we can use its order.
#
# Start:
#     left  -> smallest value
#     right -> largest value
#
# If sum < target:
#     move left forward because we need a larger sum.
#
# If sum > target:
#     move right backward because we need a smaller sum.
#
# If sum == target:
#     return the positions.
#
# This gives the same O(n) time as hashing without
# requiring an extra hash map.
#
# Time Complexity: O(n)
# Auxiliary Space: O(1)
# =========================================================

def two_sum_two_pointers(numbers, target):

    left = 1
    right = len(numbers)

    while left < right:

        current_sum = numbers[left - 1] + numbers[right - 1]

        if current_sum < target:
            left += 1

        elif current_sum > target:
            right -= 1

        else:
            return (left, right)

    return "Not Found"


# ========================Check=================================


numbers = [2, 7, 11, 15]
target = 9

print("Brute Force :", two_sum_brute_force(numbers, target))
print("Hash Map    :", two_sum_hashmap(numbers, target))
print("Two Pointers:", two_sum_two_pointers(numbers, target))