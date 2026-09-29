s = "OUZODYXAZV"
t = "XYZ"

ans = ""
dii1 = {}
dii2 = {}


for i in t:
    dii1[i] = dii1.get(i, 0) + 1

right = 0
left = 0

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

print(ans)