import random

d6 = []
d8 = []
d4 = []
d20 = []

for x in range(6):
    vd6 = [0,0,0,0]
    avgd6 = 0
    for i in range(6):
        for j in range(4):
            vd6[j] = random.randint(1, 6)
        scored6 = vd6[0] + vd6[1] + vd6[2] + vd6[3] - min(vd6)
        avgd6 += scored6
        d6.append(scored6)
    d6.append(avgd6/6)


for i in range(6):
    scored20 = 0
    vd20 = [0,0,0,0,0,0]
    while scored20 < 65:
        for j in range(6):
            vd20[j] = random.randint(1, 20)
        scored20 = sum(vd20)
    for item in vd20:
        d20.append(item)
    d20.append(scored20/6)


for i in range(6):
    avgd8 = 0
    for j in range (6):
        vd8 = [0, 0, 0, 0]
        for k in range(2):
            vd8[k] = random.randint(1, 8)
        vd8[2] = random.randint(1, 4)
        scored8 = vd8[0] + vd8[1] + vd8[2]
        d8.append(scored8)
        avgd8 += scored8
    d8.append(avgd8/6)

for c in range(6):
    avgd4 = 0
    for j in range (6):
        vd4 = [0, 0, 0, 0, 0, 0]
        for k in range(6):
            vd4[k] = random.randint(1, 4)
        scored4 = vd4[0] + vd4[1] + vd4[2] + vd4[3] + vd4[4] + vd4[5] - min(vd4)
        d4.append(scored4)
        avgd4 += scored4
    d4.append(avgd4/6)



for y in range(len(d20)):
    print(f"{d4[y]}     {d6[y]}     {d8[y]}     {d20[y]}            {min([d4[y], d6[y], d8[y], d20[y]])}    {max([d4[y], d6[y], d8[y], d20[y]])}    {(d4[y]+d6[y]+ d8[y]+ d20[y])/4}")
    if (y+1)%7 == 0:
        print("--------------------------------------------------------------------------------------------------------------------------------------------------")
            
