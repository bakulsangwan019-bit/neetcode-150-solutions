# Permutation in String

s1 = "abc"
s2 = "lecabee"


# ---------------- Brute Force Approach ----------------

dii1 = {}

for i in s1:
    dii1[i] = dii1.get(i, 0) + 1

for i in range(len(s2) - len(s1) + 1):

    dii2 = {}

    for j in range(i, i + len(s1)):
        dii2[s2[j]] = dii2.get(s2[j], 0) + 1

    if dii1 == dii2:
        print("Brute Force: True")
        break
else:
    print("Brute Force: False")


# ---------------- Sliding Window Approach ----------------

dii1 = {}
dii2 = {}

for i in s1:
    dii1[i] = dii1.get(i, 0) + 1

# Build first window
current = 0

while current < len(s1):
    dii2[s2[current]] = dii2.get(s2[current], 0) + 1
    current += 1

right = current
left = 0

while right < len(s2):

    if dii1 == dii2:
        print("Sliding Window: True")
        break

    # Add new character
    dii2[s2[right]] = dii2.get(s2[right], 0) + 1

    # Remove old character
    dii2[s2[left]] -= 1

    if dii2[s2[left]] == 0:
        del dii2[s2[left]]

    left += 1
    right += 1

else:
    if dii1 == dii2:
        print("Sliding Window: True")
    else:
        print("Sliding Window: False")