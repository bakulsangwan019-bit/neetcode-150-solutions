nums = [4, 2, 1, 7, 8, 1, 2, 8]
k = 3
largest = 0
store = []

left = 0
right = left + k 

while len(store) < k:
    store.append(nums[left : right])

print(store)