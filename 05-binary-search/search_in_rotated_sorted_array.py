# Search in Rotated Sorted Array


# Approach 1: Brute Force - O(n)

nums = [3, 4, 5, 6, 1, 2]
target = 6

ans = -1

for i in range(len(nums)):
    if nums[i] == target:
        ans = i
        break

print("Brute Force:", ans)


# Approach 2: Binary Search - O(log n)

nums = [3, 4, 5, 6, 1, 2]
target = 6

left = 0
right = len(nums) - 1
ans = -1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        ans = mid
        break

    # Right half is sorted
    if nums[mid] <= nums[right]:
        if nums[mid] < target <= nums[right]:
            left = mid + 1
        else:
            right = mid - 1

    # Left half is sorted
    else:
        if nums[left] <= target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

print("Binary Search:", ans)