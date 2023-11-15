n = 97
result = bin(n)
print(result)

b = ''
while n > 0:
    b = str(n % 4) + b
    n = n // 4
print(b)

n2 = '1201'
result = int(n2, 4)
print(result)
