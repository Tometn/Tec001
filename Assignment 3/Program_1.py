#Numbers devidable by three from 1-1000
n = 1
while n < 1001:
    if n % 3 == 0:
        print(n)
        n += 3
    n += 1