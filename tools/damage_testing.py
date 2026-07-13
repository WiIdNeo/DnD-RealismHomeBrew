import random

y = [[1, 2], [1, 2], [7, 3], [12, 4], [15, 5], [20, 6]]


for i in range(1):
    x = []
    x.append(random.randint(1, 6))
    x.append(random.randint(1, 8))
    x.append(random.randint(1, 10))
    x.append(random.randint(1, 12))
    for rands in x:
        hp = []
        for j in range(-5, 8):  
            for nums in y:
                print(f"------------Level {nums[0]}------------- ")
                print(j)
                print(f"Damage = {nums[1] + j + rands}\nFlat Damage = {j + nums[1]}\n")

# You should be able to survive raw hit of 3 - 4 Attacks

                hp.append(nums[1]+j+rands)

        print(hp)
        a = sum(hp)/(20*4)
        print(a)
        print(a*3.75)
    