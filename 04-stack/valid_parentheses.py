# Valid Parentheses
# Time: O(n)
# Space: O(n)

def is_valid(s):
    if len(s) % 2 != 0:
        return False

    pair = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    stack = []

    for char in s:
        if char in "([{":
            stack.append(char)

        elif char in pair:
            if not stack or pair[char] != stack[-1]:
                return False

            stack.pop()

    return len(stack) == 0


s = "([])"
print(is_valid(s))