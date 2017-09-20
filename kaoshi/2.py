import random

random.randint(1,33)

lists = []
for i in range(6):
    st = random.randint(1,33)
    lists.append(st)
    if i > 0:
        for j in range(len(lists)-1):
            while True:
                if lists[i] == lists[j]:
                    lists[i] = random.randint(1,33)
                else:
                    break
lists.sort()
red = random.randint(1,16)
lists.append(red)
print lists
