# Valid Palindrome
# NeetCode 150 - Two Pointers


# -----------------------------------
# Approach 1 - Empty String
# -----------------------------------
# Keep only letters/numbers, convert to lowercase,
# then compare the string with its reverse.
#
# Time Complexity: O(n)
# Auxiliary Space: O(n)


def check_palindrome_clean(str1):

    clean = ""

    for char in str1:
        if char.isalnum():
            clean += char.lower()

    return clean == clean[::-1]



# -----------------------------------
# Approach 2 - Two Pointers
# -----------------------------------
# Start one pointer from each side.
# Skip characters that are not letters/numbers.
# Compare valid characters directly.
#
# Time Complexity: O(n)
# Auxiliary Space: O(1)
# Output Space: O(1)


def check_pail(str1):

    left = 0
    right = len(str1) - 1

    while left < right:

        if not str1[left].isalnum():
            left += 1

        elif not str1[right].isalnum():
            right -= 1

        else:
            if str1[left].lower() != str1[right].lower():
                return False

            left += 1
            right -= 1

    return True



# ----------------Check-------------------

s = "A man, a plan, a canal: Panama"

print("Clean String:", check_palindrome_clean(s))
print("Two Pointers:", check_pail(s))