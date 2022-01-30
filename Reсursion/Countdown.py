def countdown(i):
    print(i)        # базовый случай
    if i<=1:
        return
    else:           # рекурсивный случай
        countdown(i-1)

#countdown(5)

def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)

print(fact(3))

