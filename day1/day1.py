entry_temp = []
entry = []
with open('day1.txt', 'r+') as f:
    for line in f.readlines():
        entry_temp.append(line)

for i in entry_temp:
    entry.append(int(i.strip()))

x, y = 0, 0
for i in entry:
    x =+ 1
    y = 0
    for j in entry:
        y =+1
        if not(y < x):
            if (i+j) == 2020:
                print(i*j)

x, y, z = 0, 0, 0
for i in entry:
    x =+ 1
    y = 0
    for j in entry:
        y =+1
        z = 0
        for k in entry:
            if not(j < k):
                if (i+j+k) == 2020:
                    print(i*j*k)