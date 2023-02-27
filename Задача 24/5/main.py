f = open('5.txt')
r = f.read()

count=1
cmax=0

for i in range(0, len(r)-1):
    if r[i]<=r[i+1] and r[i] in '13579' and r[i+1] in '13579':
        count+=1
        cmax=max(count, cmax)
    else:
        count=1

print(cmax)
