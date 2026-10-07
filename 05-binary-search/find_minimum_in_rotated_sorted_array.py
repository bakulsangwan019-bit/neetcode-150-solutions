# Find Minimum in Rotated Sorted Array


# Approach 1: Linear Search - O(n)

nums = [4, 5, 6, 7, 0, 1, 2]

for i in range(len(nums)):
    if i == 0 or nums[i] > nums[i - 1]:
        continue
    else:
        print("Linear Search:", nums[i])
        break
else:
    print("Linear Search:", nums[0])


# Approach 2: Binary Search with ans - O(log n)

nums = [4, 5, 6, 7, 0, 1, 2]

left = 0
right = len(nums) - 1
ans = None

while left <= right:
    mid = (left + right) // 2

    if nums[mid] > nums[right]:
        left = mid + 1
    else:
        right = mid - 1

    if ans is None or nums[mid] < ans:
        ans = nums[mid]

print("Binary Search with ans:", ans)


# Approach 3: Binary Search without ans - O(log n)

nums = [4, 5, 6, 7, 0, 1, 2]

left = 0
right = len(nums) - 1

while left < right:
    mid = (left + right) // 2

    if nums[mid] > nums[right]:
        left = mid + 1
    else:
        right = mid

print("Binary Search without ans:", nums[left])