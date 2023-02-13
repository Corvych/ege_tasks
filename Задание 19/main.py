def f(x, y, p):
    if x+y >= 77 and p==3: return False
    elif x+y < 77 and p==3: return False

    return f(x + 1, y, p + 1) or f(x, y + 1, p + 1) or f(x * 2, y, p + 1) or f(x, y * 2, p + 1)

arr_num = []
for s in range(1,70):
    if f(s, 7, 1):
        arr_num.append(s)
print("Ответ:", s)
