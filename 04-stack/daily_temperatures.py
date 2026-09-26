# Brute Force Approach
temperatures = [30, 38, 30, 36, 35, 40, 28]

answer = []

for i in range(len(temperatures)):
    current = 0

    for j in range(i + 1, len(temperatures)):
        if temperatures[i] < temperatures[j]:
            current = j - i
            break

    answer.append(current)

print("Brute Force:", answer)


# Monotonic Stack Approach
temperatures = [30, 38, 30, 36, 35, 40, 28]

stack = []
answer = [0] * len(temperatures)

for i in range(len(temperatures)):
    while stack and temperatures[i] > temperatures[stack[-1]]:
        answer[stack[-1]] = i - stack[-1]
        stack.pop()

    stack.append(i)

print("Monotonic Stack:", answer)