# Contains Duplicate
# NeetCode 150 - Arrays & Hashing


# -----------------------------------
# Approach 1 - Brute Force
# -----------------------------------
# Compare every element with the elements after it.
#
# Time Complexity: O(n^2)
# Auxiliary Space: O(1)


def duplicate_arr_brute_force(array):

    for i in range(len(array)):

        for j in range(i + 1, len(array)):

            if array[i] == array[j]:
                return True

    return False



# -----------------------------------
# Approach 2 - Using Set
# -----------------------------------
# Instead of comparing every pair,
# store elements that we have already seen.
#
# Set membership checking is O(1) average.
#
# Time Complexity: O(n)
# Auxiliary Space: O(n)
# Output Space: O(1)


def duplicate_arr(array):

    seen = set() # it make auxiliary space complexity O(n)

    for i in array: # it make time complexity O(n)
        
        if i in seen: # membership checking in set is O(1) avg.
            return True
        
        seen.add(i)

    return False



# -----------------------------------
# Test
# -----------------------------------

nums = [1, 2, 3, 1]

print("Brute Force:", duplicate_arr_brute_force(nums))
print("Using Set:", duplicate_arr(nums))