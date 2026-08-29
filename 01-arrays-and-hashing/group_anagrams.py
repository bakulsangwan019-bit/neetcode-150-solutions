# Group Anagrams
# NeetCode 150 - Arrays & Hashing


# -----------------------------------
# Approach 1 - Sorting
# -----------------------------------
# Anagrams become identical after sorting.
#
# Example:
# "eat" -> "aet"
# "tea" -> "aet"
#
# Time Complexity: O(n * k log k)
# Auxiliary Space: O(n * k)
#
# n = number of strings
# k = average/max string length


def group_anagram_sorting(words):

    dic = {}

    for word in words:

        key = "".join(sorted(word))


        if key not in dic:
            dic[key] = []

        dic[key].append(word)

    return list(dic.values())



# -----------------------------------
# Approach 2 - Character Frequency
# -----------------------------------
# Count occurrences of each letter a-z.
# Strings with identical counts are anagrams.
#
# tuple(count) is used because lists cannot
# be dictionary keys.
#
# Time Complexity: O(n * k)
# Auxiliary Space: O(n * k)


def group_anagram(same):

    dic = {}

    for i in same:

        count = [0] * 26

        for word in i:
            j = ord(word) - ord("a")
            count[j] += 1

        a = tuple(count)

        if a not in dic:
            dic[a] = []

        dic[a].append(i)

    return list(dic.values())



# -----------------Check------------------


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print("Using Sorting:", group_anagram_sorting(strs))
print("Using Frequency Count:", group_anagram(strs))