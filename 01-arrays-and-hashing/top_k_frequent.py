# Top K Frequent Elements
# NeetCode 150 - Arrays & Hashing


# -----------------------------------
# Approach 1 - First Idea
# -----------------------------------
# First idea was to manually find the elements
# with the largest frequencies.
#
# This can work when k is very small (like k = 2),
# but it does not scale well for arbitrary k.


def top_two_frequent(arr):

    dic = {}

    for i in arr:
        dic.setdefault(i, 0)
        dic[i] += 1

    largest = None
    second_largest = None

    for key in dic:

        if largest is None or dic[key] > dic[largest]:
            second_largest = largest
            largest = key

        elif second_largest is None or dic[key] > dic[second_largest]:
            second_largest = key

    return [largest, second_largest]


# -----------------------------------
# Approach 2 - Dictionary + Sorting
# -----------------------------------
# 1. Count frequency of every number.
# 2. Sort dictionary items using frequency.
# 3. Take the first k elements.
#
# Frequency counting: O(n)
# 
#
# Auxiliary Space: O(n)
# Output Space: O(k)


def k_frequency(arr, take):

    dic = {}
    store = []

    for i in arr:
        dic.setdefault(i, 0)
        dic[i] += 1

    a = sorted(dic.items(), key=lambda x: x[1], reverse=True)

    for j in a:

        if len(store) < take:
            store.append(j[0])

    return store


# -------------Check----------------------


nums = [1, 1, 1, 2, 2, 3]
k = 2

print("First Idea:", top_two_frequent(nums))
print("Sorting Approach:", k_frequency(nums, k))