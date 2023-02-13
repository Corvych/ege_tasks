def f(x, y, p):
    if x+y >= 77 and p<4: return False
    elif x+y >= 77 and p==4: return True
    elif x+y < 77 and p==4: return False
    else:
        if p % 2 != 0:
            return f(x + 1, y, p + 1) or f(x, y + 1, p + 1) or f(x * 2, y, p + 1) or f(x, y * 2, p + 1) # Вышли победителем!
        else:
            return f(x + 1, y, p + 1) and f(x, y + 1, p + 1) and f(x * 2, y, p + 1) and f(x, y * 2, p + 1) # Проиграли...

for s in range(1,70):
    if f(s, 7, 1) == True:
        print("Ответ", s)
