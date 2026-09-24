import operator


# ============================================================
# Evaluate Reverse Polish Notation - Classic if/elif
# ============================================================

tokens = ["1", "2", "+", "3", "*", "4", "-"]

seen = {"+", "-", "*", "/"}

stack = []

for i in tokens:
    if i not in seen:
        stack.append(int(i))

    else:
        a = stack.pop()
        b = stack.pop()

        if i == "+":
            current = b + a
        elif i == "-":
            current = b - a
        elif i == "*":
            current = b * a
        elif i == "/":
            current = b / a

        stack.append(current)

print("Classic approach:", stack)


# ============================================================
# Evaluate Reverse Polish Notation - operator module
# ============================================================

tokens = ["1", "2", "+", "3", "*", "4", "-"]

seen = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}

stack = []

for i in tokens:
    if i not in seen:
        stack.append(int(i))

    else:
        a = stack.pop()
        b = stack.pop()

        current = seen[i](b, a)

        stack.append(current)

print("Operator module approach:", stack)