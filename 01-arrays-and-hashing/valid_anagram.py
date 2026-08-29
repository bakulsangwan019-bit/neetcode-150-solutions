# Valid Anagram
# NeetCode 150 - Arrays & Hashing


# -----------------------------------
# Approach 1 - Brute Force
# -----------------------------------
# For every character, count how many times it
# appears in both strings and compare the counts.
#
# Time Complexity: O(n^2)
# Auxiliary Space: O(1)
# Output Space: O(1)


def check_anagram_brute_force(str1, str2):

    if len(str1) != len(str2):
        return False

    for i in str1:

        count1 = 0
        count2 = 0

        for j in str1:
            if i == j:
                count1 += 1

        for k in str2:
            if i == k:
                count2 += 1

        if count1 != count2:
            return False

    return True



# -----------------------------------
# Approach 2 - Frequency Dictionaries
# -----------------------------------
# Store the frequency of each character.
#
# Dictionary lookup is O(1) average,
# which removes the repeated searching.
#
# Time Complexity: O(n)
# Auxiliary Space: O(n)
# Output Space: O(1)


def check_anagram(str1, str2):

    if len(str1) != len(str2):
        return False

    dict1 = {}
    dict2 = {}

    for i in str1:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] += 1

    for j in str2:
        if j not in dict2:
            dict2[j] = 1
        else:
            dict2[j] += 1

    for k in dict1:
        if k not in dict2 or dict2[k] != dict1[k]:
            return False

    return True


# -------Check-----------

s = "anagram"
t = "nagaram"

print("Brute Force:", check_anagram_brute_force(s, t))
print("Using Dictionary:", check_anagram(s, t))