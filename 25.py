def f(n):
    a = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            a.add(i)
            a.add(n//i)
    return a
k = 0
for s in range(700000, 800000):
    a = f(s)
    a = [item for item in a if item % 10 == 7 and item != 7 ]
    if a:
        print(s, min(a))
        k+=1
        if k == 5:
            break