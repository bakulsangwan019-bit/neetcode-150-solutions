# Longest Consecutive Sequence
# NeetCode 150 - Arrays & Hashing


# -----------------------------------
# Approach 1 - Sorting
# -----------------------------------
# Sort the numbers, then scan them and count
# consecutive values.
#
# Time Complexity: O(n log n)
# Auxiliary Space: depends on sorting implementation
# Output Space: O(1)


def longest_chain_sorting(arr):

    if not arr:
        return 0

    nums = sorted(arr)

    large = 1
    count = 1

    for i in range(1, len(nums)):


        if nums[i] == nums[i - 1]:
            continue

        if nums[i] == nums[i - 1] + 1:
            count += 1
        else:
            count = 1

        if count > large:
            large = count

    return large



# -----------------------------------
# Approach 2 - Using Set
# -----------------------------------
# Convert the array to a set for average O(1)
# membership checking.
#
# Only start a sequence when i - 1 does not exist.
#
# Time Complexity: O(n) average
# Auxiliary Space: O(n)
# Output Space: O(1)


def longest_chain(arr):

    seen = set(arr)
    large = 0

    for i in seen:

        if i - 1 not in seen:

            current = i
            count = 1

            while current + 1 in seen:
                current += 1
                count += 1

            if large < count:
                large = count

    return large



# --------------CHeck---------------------

nums = [100, 4, 200, 1, 3, 2]

print("Sorting:", longest_chain_sorting(nums))
print("Using Set:", longest_chain(nums))