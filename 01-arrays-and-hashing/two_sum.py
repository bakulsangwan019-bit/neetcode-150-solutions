# Two Sum
# NeetCode 150 - Arrays & Hashing


# -----------------------------------
# Approach 1 - Brute Force
# -----------------------------------
# Try every possible pair and check whether
# their sum equals the target.
#
# Time Complexity: O(n^2)
# Auxiliary Space: O(1)
# Output Space: O(1)


def two_sums_brute_force(arr, targ):

    for i in range(len(arr)):

        for j in range(i + 1, len(arr)):

            if arr[i] + arr[j] == targ:
                return (i, j)



# -----------------------------------
# Approach 2 - Using Dictionary
# -----------------------------------
# For every number:
# complement = target - current number
#
# Check whether the complement was already seen.
# Dictionary lookup is O(1) average.
#
# Time Complexity: O(n)
# Auxiliary Space: O(n)
# Output Space: O(1)


def two_sums(arr, targ):

    dic = {}
    index = 0

    for i in arr:

        x = targ - i

        if x not in dic:
            dic[i] = index

        else:
            return (dic[x], index)

        index += 1



# ----------------Check------------------


nums = [2, 11, 7, 15]
target = 9

print("Brute Force:", two_sums_brute_force(nums, target))
print("Using Dictionary:", two_sums(nums, target))