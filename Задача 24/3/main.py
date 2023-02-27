f = open('3.txt')
r = f.read()

count = 0
cmax = 0

for i in range(0, len(r)-1):
    if r[i]<=r[i+1]:
        count+=1
        cmax = max(count, cmax)
    else:
        count=1

print(cmax)
