# Koko Eating Bananas

piles = [3, 6, 7, 11]
h = 8


# Brute Force - O(n * max(piles))

ans = max(piles)

for speed in range(1, max(piles) + 1):
    total_hour = 0

    for pile in piles:
        total_hour += (pile + speed - 1) // speed

    if total_hour <= h:
        ans = speed
        break

print("Brute Force:", ans)


# Binary Search - O(n * log(max(piles)))

left = 1
right = max(piles)
ans = right

while left <= right:
    mid = (left + right) // 2
    total_hour = 0

    for pile in piles:
        total_hour += (pile + mid - 1) // mid

    if total_hour > h:
        left = mid + 1
    else:
        ans = mid
        right = mid - 1

print("Binary Search:", ans)