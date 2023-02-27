f=open('6.txt')
r=f.read()
count=1
cmax=0

for i in range(0, len(r)-1):
    if (r[i] in '123' and r[i+1] in 'ABC') or (r[i] in 'ABC' and r[i+1] in '123') :
        count+=1
        cmax=max(count, cmax)
    else:
        count=1

print(cmax)
