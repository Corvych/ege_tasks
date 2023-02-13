def f(x, y, p):
    if x+y >= 77 and (p==3 or p==5): return True
    elif x+y < 77 and p==5: return False
    elif x+y >= 77 and p < 5: return False
    else:
        if p%2 == 0:
            return f(x + 1, y, p + 1) or f(x, y + 1, p + 1) or f(x * 2, y, p + 1) or f(x, y * 2, p + 1)
        else:
            return f(x + 1, y, p + 1) and f(x, y + 1, p + 1) and f(x * 2, y, p + 1) and f(x, y * 2, p + 1)

def f1(x, y, p):
    if x+y >= 77 and p==3: return True
    elif x+y < 77 and p==3: return False
    elif x+y >= 77 and p < 3: return False
    else:
        if p%2 == 0:
            return f1(x + 1, y, p + 1) or f1(x, y + 1, p + 1) or f1(x * 2, y, p + 1) or f1(x, y * 2, p + 1)
        else:
            return f1(x + 1, y, p + 1) and f1(x, y + 1, p + 1) and f1(x * 2, y, p + 1) and f1(x, y * 2, p + 1)

for s in range(1,70):
    if f(s, 7, 1):
        print(s)
for s in range(1,70):
    if f1(s, 7, 1):
        print(s)
