# ============================================================
# Approach 1: Using separate while conditions
# ============================================================

nums = [-1, 0, 2, 4, 6, 8]
target = 4

ans = -1
left = 0
right = len(nums) - 1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        ans = mid
        break

    while nums[mid] > target and left <= right:
        right = mid - 1

        if left > right:
            break

        mid = (left + right) // 2

        if nums[mid] == target:
            ans = mid
            break

    if ans != -1:
        break

    while nums[mid] < target and left <= right:
        left = mid + 1

        if left > right:
            break

        mid = (left + right) // 2

        if nums[mid] == target:
            ans = mid
            break

    if ans != -1:
        break

print(ans)


# ============================================================
# Approach 2: Clean if / elif binary search
# ============================================================

nums = [-1, 0, 2, 4, 6, 8]
target = 4

ans = -1
left = 0
right = len(nums) - 1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        ans = mid
        break

    elif nums[mid] > target:
        right = mid - 1

    else:
        left = mid + 1

print(ans)