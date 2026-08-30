# 3Sum - LeetCode 15
#
# Find all unique triplets whose sum is 0.


# ============================================================
# Approach 1: Brute Force
# ============================================================
# Check every possible combination of 3 different indices.
#
# Time Complexity: O(n^3)
# Auxiliary Space: O(1)
# Output Space: depends on number of triplets
# ============================================================

def three_sum_brute(nums):

    result = []
    seen_triplets = set()

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):

                if nums[i] + nums[j] + nums[k] == 0:

                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))

                    if triplet not in seen_triplets:
                        seen_triplets.add(triplet)
                        result.append(list(triplet))

    return result


# ============================================================
# Approach 2: Hash Set
# ============================================================
# Fix one number nums[i].
#
# Then solve a Two Sum-like problem for the remaining numbers.
# Use a set for fast membership checking.
#
# Time Complexity: O(n^2)
# Auxiliary Space: O(n)
# ============================================================

def three_sum_hash(nums):

    result = set()

    for i in range(len(nums)):

        seen = set()

        for j in range(i + 1, len(nums)):

            needed = -(nums[i] + nums[j])

            if needed in seen:
                triplet = tuple(sorted([nums[i], nums[j], needed]))
                result.add(triplet)

            seen.add(nums[j])

    return [list(x) for x in result]


# ============================================================
# Approach 3: Sorting + Two Pointers
# ============================================================
#
# 1. Sort the array.
# 2. Fix x = arr[i].
# 3. Search for two numbers whose sum is -x.
# 4. Skip duplicate x values.
# 5. Skip duplicate left/right values.
#
# Time Complexity:
# sorting       -> O(n log n)
# outer loop    -> O(n)
# pointer scan  -> O(n) for each i
#
# Overall -> O(n^2)
#
# Auxiliary Space:
# Depends on sorting implementation.
# Ignoring sorting's internal memory -> O(1)
#
# Output Space: depends on answer
# ============================================================

def three_sum_two_pointers(arr):

    store = []
    arr.sort()

    for i in range(len(arr)):

        if i > 0 and arr[i] == arr[i - 1]:
            continue

        x = arr[i]

        left = i + 1
        right = len(arr) - 1

        while left < right:

            pair_sum = arr[left] + arr[right]

            if pair_sum < -x:
                left += 1

            elif pair_sum > -x:
                right -= 1

            else:
                store.append([x, arr[left], arr[right]])

                left += 1
                right -= 1

                # Skip repeated left values
                while left < right and arr[left] == arr[left - 1]:
                    left += 1

                # Skip repeated right values
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1

    return store


# ============================================================
# Approach 4: Same Two-Pointer Logic Using Two While Loops
# ============================================================
# This is NOT a faster algorithm.
#
# We simply replace:
#
#     for i in range(...)
#
# with:
#
#     while i < ...
#
# Time Complexity: O(n^2)
# ============================================================

def three_sum_two_whiles(arr):

    store = []
    arr.sort()

    i = 0

    while i < len(arr):

        # Skip duplicate fixed x
        if i > 0 and arr[i] == arr[i - 1]:
            i += 1
            continue

        x = arr[i]

        left = i + 1
        right = len(arr) - 1

        while left < right:

            pair_sum = arr[left] + arr[right]

            if pair_sum < -x:
                left += 1

            elif pair_sum > -x:
                right -= 1

            else:
                store.append([x, arr[left], arr[right]])

                left += 1
                right -= 1

                while left < right and arr[left] == arr[left - 1]:
                    left += 1

                while left < right and arr[right] == arr[right + 1]:
                    right -= 1

        i += 1

    return store


# ===========================Check=================================


nums = [-1, 0, 1, 2, -1, -4]

print("Brute Force :", three_sum_brute(nums.copy()))
print("Hash Set    :", three_sum_hash(nums.copy()))
print("Two Pointer :", three_sum_two_pointers(nums.copy()))
print("Two Whiles  :", three_sum_two_whiles(nums.copy()))