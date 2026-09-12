# Longest Repeating Character Replacement


# Brute Force
# Time: O(n^2)
# Space: O(1)

def character_replacement_brute(s, k):
    largest = 0

    for i in range(len(s)):
        freq = {}
        max_freq = 0

        for j in range(i, len(s)):
            char = s[j]
            freq[char] = freq.get(char, 0) + 1

            max_freq = max(max_freq, freq[char])
            window_len = j - i + 1

            if window_len - max_freq > k:
                break

            largest = max(largest, window_len)

    return largest


# Sliding Window - Exact max_freq
# Time: O(n)
# Space: O(1)

def character_replacement_exact(s, k):
    left = 0
    freq = {}
    largest = 0

    for right in range(len(s)):
        char = s[right]
        freq[char] = freq.get(char, 0) + 1

        max_freq = max(freq.values())
        window_len = right - left + 1

        while window_len - max_freq > k:
            freq[s[left]] -= 1
            left += 1

            window_len = right - left + 1
            max_freq = max(freq.values())

        largest = max(largest, window_len)

    return largest


# Optimized Sliding Window
# Time: O(n)
# Space: O(1)

def character_replacement(s, k):
    left = 0
    freq = {}
    max_freq = 0
    largest = 0

    for right in range(len(s)):
        char = s[right]
        freq[char] = freq.get(char, 0) + 1

        max_freq = max(max_freq, freq[char])

        while (right - left + 1) - max_freq > k:
            freq[s[left]] -= 1
            left += 1

        largest = max(largest, right - left + 1)

    return largest


s = "AABABBA"
k = 1

print(character_replacement_brute(s, k)) 
print(character_replacement_exact(s, k))  
print(character_replacement(s, k))        