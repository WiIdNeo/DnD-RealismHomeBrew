import random

x = [0,0]
y = []

for i in range(100):
    x[0] = random.randint(1,20)
    x[1] = random.randint(1,20)
    y.append(x[0] - x[1])
    print(x)
print(y)