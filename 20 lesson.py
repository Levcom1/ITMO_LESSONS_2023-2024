import re

print('--- 14.10 ---')
f = open('17_14_10.rtf')
f = [int(i) for i in f]
max_el = max(el for el in f if abs(el) % 10 == 3)
k = 0
max_sum = 0
for j in range(len(f) - 1):
    if (abs(f[j]) % 10 == 3) != (abs(f[j + 1]) % 10 == 3) and (f[j] ** 2 + f[j + 1] ** 2) >= max_el ** 2:
        k += 1
        max_sum = max(max_sum, f[j] ** 2 + f[j + 1] ** 2)
print(k, max_sum)

print('--- 14.15 ---')
s = [int(s) for s in open('17_14_15.rtf')]
mn = 10 ** 6
res = []
for i in s:
    if len(str(i)) == 3 and i % 10 == 1:
        mn = min(mn, i)
for j in range(len(s) - 1):
    if (len(str(s[j])) == 2) != (len(str(s[j + 1])) == 2):
        if (s[j] + s[j + 1]) % mn == 0:
            res.append(s[j] + s[j + 1])
print(len(res), min(res))

print('--- 14.16 ---')
f = open('17_14_16.rtf', 'r')
f = [int(i) for i in f]
max_sum = 0
k = 0
for i in range(2, len(f)):
    a = 99 < f[i] < 1000 and f[i] % 2 == 0
    b = 99 < f[i - 1] < 1000 and f[i - 1] % 2 == 0
    c = 99 < f[i - 2] < 1000 and f[i - 2] % 2 == 0
    if ((a != b) != c) and (((a and b) and c) == 0):
        k += 1
        max_sum = max(max_sum, f[i] + f[i - 1] + f[i - 2])
print(k, max_sum)

print('--- 14.22 ---')


def col_del(n):
    deli = []
    for x in range(2, n):
        if n % x == 0:
            deli.append(x)
    return deli


for i in range(174457, 174506):
    d = col_del(i)
    if len(d) == 2:
        print(*d)

print('--- 14.32 ---')
for i in range(2024, (10 ** 10) + 1, 2024):
    if re.fullmatch('1\d{1}2239\d*4', str(i)):
        print(i, i // 2024)
