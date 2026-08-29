# Product of Array Except Self
# NeetCode 150 - Arrays & Hashing


# -------------------------
# Approach 1 - Brute Force
# -------------------------
# For each index, multiply every other element.
#
# Time Complexity: O(n^2)
# Auxiliary Space: O(1)
# Output Space: O(n)


def product_except_self_brute_force(arr):

    store = []

    for i in range(len(arr)):

        product = 1

        for j in range(len(arr)):

            if i != j:
                product *= arr[j]

        store.append(product)

    return store



# -----------------------------------
# Approach 2 - Prefix + Suffix
# -----------------------------------
# First pass:
# store[i] = product of everything to the LEFT
#
# Second pass:
# multiply by product of everything to the RIGHT
#
# Time Complexity: O(n)
# Auxiliary Space: O(1)
# Output Space: O(n)


def mult_all(arr):

    value = 1
    store = []

    # Prefix products
    for i in range(len(arr)):

        if i != 0:
            value *= arr[i - 1]

        store.append(value)

    value2 = 1

    # Suffix products
    for j in range(len(arr) - 1, -1, -1):

        if j != len(arr) - 1:
            value2 *= arr[j + 1]

        store[j] *= value2

    return store



# ---------------Check------------------


nums = [1, 2, 3, 4]

print("Brute Force:", product_except_self_brute_force(nums))
print("Prefix + Suffix:", mult_all(nums))