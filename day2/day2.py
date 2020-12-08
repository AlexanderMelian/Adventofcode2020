import re

entry_temp = []
entry = []
with open('day2.txt', 'r+') as f:
    for line in f.readlines():
        entry_temp.append(line)
for i in entry_temp:
    entry.append(i.strip())

contfinal = 0
contfinal2 = 0
for i in entry:
    cont = 0
    x = re.split("[\- \s]", i)
    for j in x[3]:
        if (x[2][0] == j):
            cont = cont + 1

    if cont>=int(x[0]) and cont<=int(x[1]):
        contfinal = contfinal + 1

print(contfinal)

for i in entry:
    cont = 0
    x = re.split("[\- \s]", i)
    if ((x[2][0] == (x[3][int(x[0])-1])) ^ (x[2][0] == (x[3][int(x[1])-1]))):
        contfinal2 = contfinal2 + 1
    
print(contfinal2)