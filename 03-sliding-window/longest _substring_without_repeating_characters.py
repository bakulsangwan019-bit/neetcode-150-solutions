s = "abcabcbb"

seen = set()
tot = 1
left = 0
right = left + 1
seen.add(s[left])
largest = tot

while right < len(s):


    if s[right] not in seen:
        tot += 1
        seen.add(s[right])
        right += 1

    else:
        seen.remove(s[left])
        left += 1
        tot -= 1

    if largest < tot:
        largest = tot

    
print(largest)



#Brute Force
s = "abcabcbb"

largest = 0


for i in range(len(s)):
    s = "abcabcbb"

seen = set()
tot = 1
left = 0
right = left + 1
seen.add(s[left])
largest = tot

while right < len(s):


    if s[right] not in seen:
        tot += 1
        seen.add(s[right])
        right += 1

    else:
        seen.remove(s[left])
        left += 1
        tot -= 1

    if largest < tot:
        largest = tot

    
print(largest)



#Brute Force

s = "abcabcbb"

largest = 0

for i in range(len(s)):

    seen = set()

    for j in range(i,len(s)):
        if s[j] in seen:
            break

        seen.add(s[j])

    largest = max(largest , len(seen))

print(largest)       
