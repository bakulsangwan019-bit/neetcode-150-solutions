# Minimum Window Substring
# Three Approaches


# ============================================================
# Approach 1: Check the whole required dictionary
# ============================================================

s = "OUZODYXAZV"
t = "XYZ"

ans = ""
dii1 = {}
dii2 = {}

for char in t:
    dii1[char] = dii1.get(char, 0) + 1

left = 0
right = 0

while right < len(s):

    dii2[s[right]] = dii2.get(s[right], 0) + 1
    right += 1

    valid = True

    for key in dii1:
        if key not in dii2 or dii2[key] < dii1[key]:
            valid = False
            break

    while valid:

        if s[left] not in dii1 or dii2[s[left]] > dii1[s[left]]:
            dii2[s[left]] -= 1

            if dii2[s[left]] == 0:
                del dii2[s[left]]

            left += 1

        else:
            current_window = s[left:right]

            if ans == "" or len(current_window) < len(ans):
                ans = current_window

            break

print("App 1:", ans)


# ============================================================
# Approach 2: have/need counts satisfied requirements
# ============================================================

s = "OUZODYXAZV"
t = "XYZ"

ans = ""
dii1 = {}
dii2 = {}

for char in t:
    dii1[char] = dii1.get(char, 0) + 1

left = 0

# Number of distinct character requirements
need = len(dii1)
have = 0

for right in range(len(s)):

    char = s[right]
    dii2[char] = dii2.get(char, 0) + 1


    if char in dii1 and dii2[char] == dii1[char]:
        have += 1


    while have == need:

        current_window = s[left:right + 1]

        if ans == "" or len(current_window) < len(ans):
            ans = current_window

        left_char = s[left]
        dii2[left_char] -= 1


        if left_char in dii1 and dii2[left_char] < dii1[left_char]:
            have -= 1

        if dii2[left_char] == 0:
            del dii2[left_char]

        left += 1

print("App 2:", ans)


# ============================================================
# Approach 3: have/need counts required character occurrences
# ============================================================

s = "OUZODYXAZV"
t = "XYZ"

ans = ""
dii1 = {}
dii2 = {}

for char in t:
    dii1[char] = dii1.get(char, 0) + 1

left = 0
current = 0

# Total required character occurrences
need = len(t)
have = 0


while current < len(s):

    char = s[current]
    dii2[char] = dii2.get(char, 0) + 1

    if char in dii1 and dii2[char] == dii1[char]:
        have += dii1[char]

    if have == need:
        ans = s[left:current + 1]
        break

    current += 1


if have == need:

    right = current + 1

    while right < len(s):

        char = s[right]
        dii2[char] = dii2.get(char, 0) + 1
        right += 1


        while (
            s[left] not in dii1
            or dii2[s[left]] > dii1[s[left]]
        ):

            dii2[s[left]] -= 1

            if dii2[s[left]] == 0:
                del dii2[s[left]]

            left += 1

        current_window = s[left:right]

        if len(current_window) < len(ans):
            ans = current_window

print("App 3:", ans)