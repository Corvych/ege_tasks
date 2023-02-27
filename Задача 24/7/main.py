f=open('7.txt')
r=f.read()
count=2
cmax=0

for i in range(0, len(s)-2):
    if r[i]=='0' and r[i+1]=='0' and r[i+2]=='0':
        count=2
    else:
        count+=1
        cmax = max(count, cmax)

print(cmax)
