# Maximum Number of Vowels in a Substring of Length k


# Brute Force
# Time: O(n * k)
# Space: O(1)

def max_vowels_brute(s, k):
    largest = 0

    for i in range(len(s) - k + 1):
        current = 0

        for j in range(i, i + k):
            if s[j] in "aeiou":
                current += 1

        if current > largest:
            largest = current

    return largest


# Sliding Window
# Time: O(n)
# Space: O(1)

def max_vowels(s, k):
    current = 0

    for i in range(k):
        if s[i] in "aeiou":
            current += 1

    largest = current
    left = 0
    right = k

    while right < len(s):

        if s[left] in "aeiou":
            current -= 1

        if s[right] in "aeiou":
            current += 1

        if current > largest:
            largest = current

        left += 1
        right += 1

    return largest


s = "abciiidef"
k = 3

print(max_vowels_brute(s, k))  
print(max_vowels(s, k))        
