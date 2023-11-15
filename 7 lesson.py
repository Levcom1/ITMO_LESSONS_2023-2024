print('--- 2.25 ---')
# 2.25
ans = 0
for n in range(5, 1000):
    b = bin(n)
    if n % 3 == 0:
        r = str(b) + str(b)[-3:]
    else:
        d = bin(n % 3 * 3)
        r = str(b) + str(d)[2:]
    if 247 > int(r, 2) > ans:
        ans = int(r, 2)
print(ans)

print('--- 2.27 ---')
# 2.27
n = 8 ** 2015 + 32 ** 2010 - 1
b = bin(n)
print(b.count('1'))

print('--- 2.28 ---')
# 2.28
n = 27 ** 11 + 3 ** 19 - 9 ** 7 - 9


def counts(number, system):
    s = ''
    while number != 0:
        s += str(number % system)
        number //= system
    return s[::-1]


print(counts(n, 3))

print('--- 2.31 ---')
# 2.31
n = 4 * 3125 ** 9 + 5 * 625 ** 8 - 2 * 625 ** 7 + 7 * 125 ** 5 - 9 * 25 ** 4 - 2024


def counts(number, system):
    s = ''
    while number != 0:
        s += str(number % system)
        number //= system
    return s[::]


a = counts(n, 25)
print(a.count('0'))
print(a)
