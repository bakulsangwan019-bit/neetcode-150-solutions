target = 10
position = [4, 1, 0, 7]
speed = [2, 2, 1, 1]

cars = []
stack = []


for i in range(len(position)):
    cars.append((position[i], speed[i]))


cars.sort(key=lambda x: x[0], reverse=True)

for position, speed in cars:
    time = (target - position) / speed


    if not stack or time > stack[-1]:
        stack.append(time)

print(len(stack))