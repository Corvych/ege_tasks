f = open('2.txt')
r = f.read()

count = 0
cmax = 0

for i in range(0, len(r)):
    if r[i] == "Z":
        cmax = max(count, cmax)
        count = 0
    else:
        count += 1

print(cmax)
