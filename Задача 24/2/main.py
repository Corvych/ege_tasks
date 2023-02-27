f = open('2.txt')
r = f.read()

count = 0
cmax = 0

for i in range(0, len(r)):
    if r[i] != "Z":
        count+=1
        cmax = max(count, cmax)

print(cmax)
