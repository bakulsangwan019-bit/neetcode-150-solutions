blocks = "WBBWWBBWBW"
k = 2
current = 0

for i in range(k):
    if blocks[i] == "W":
        current += 1

largest = current
left = 0
right = k

while right < len(blocks):

    if blocks[right] == "W":
        current += 1
    
    if blocks[left] == "W":
        current -= 1

    if largest > current:
        largest = current

    left += 1
    right += 1

print(largest)