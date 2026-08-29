# Encode and Decode Strings
# NeetCode 150 - Arrays & Hashing
#
# Approach - Length Prefix
#
# Each word is stored as:
# length#word
#
# Example:
# "hello" -> "5#hello"


def encode(str1):

    new = ""

    for i in str1:
        l = len(i)
        new += str(l)
        new += "#"
        new += i

    return new


def decode(lis):

    left = 0
    store = []

    while left < len(lis):

        move = left

        while lis[move] != "#":
            move += 1

        le = int(lis[left:move])

        a = lis[move + 1: le + move + 1]

        store.append(a)

        left = move + le + 1

    return store


strs = ["hello", "python", "DSA"]

a = encode(strs)
d = decode(a)

#------------Check-------------

print(d)