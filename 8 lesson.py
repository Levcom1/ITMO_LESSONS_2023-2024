from itertools import *

print('--- 2.36 ---')
# 2.36
for x in range(8):
    a1 = 2 * 8 ** 4 + 7 * 8 ** 3 + 3 * 8 ** 2 + x * 8 + 5
    a2 = 1 * 8 ** 4 + x * 8 ** 3 + 2 * 8 ** 2 + 4 * 8 + 3
    if (a1 + a2) % 7 == 0:
        print((a1 + a2) // 7)

print('--- 3.15 ---')
# 3.15
a = {0: 'И', 1: 'М', 2: 'О', 3: 'Т'}
k = 0
for i in range(0, len(a)):
    for n in range(0, len(a)):
        for m in range(0, len(a)):
            for j in range(0, len(a)):
                k += 1
                if a[i] + a[n] + a[m] + a[j] == 'ИТМО':
                    print(k)

print('--- 3.17 ---')
# 3.17
a = {0: 'И', 1: 'П', 2: 'Т', 3: 'Ф'}
k = 0
for i in range(0, len(a)):
    for n in range(0, len(a)):
        for m in range(0, len(a)):
            for j in range(0, len(a)):
                k += 1
                if k == 201:
                    print(a[i], a[n], a[m], a[j])

print('--- 3.19 ---')
# 3.19
a = {0: 'А', 1: 'Б', 2: 'И', 3: 'К', 4: 'П', 5: 'Р'}
k = 0
for i in range(0, len(a)):
    for n in range(0, len(a)):
        for m in range(0, len(a)):
            for j in range(0, len(a)):
                for x in range(0, len(a)):
                    k += 1
                    if a[i] == 'К':
                        print(k)
                        break  # exit()

print('--- 3.20 ---')
# 3.20
a = 'КОРУ'
k = 0
for i in a:
    for n in a:
        for m in a:
            for j in a:
                k += 1
                if (i + n + m + j).count('К') == 0 and (i + n + m + j).count('ОО') == 0:
                    print(k)
                    break  # exit()

print('--- 3.29 ---')
# 3.29
kol = 0
for i in product('012345678', repeat=5):
    s = ''.join(i)
    if s[0] != '0' and s.count('6') >= 1 and '00' not in s \
            and '11' not in s and '22' not in s and '33' not in s \
            and '44' not in s and '55' not in s and '66' not in s \
            and '77' not in s and '88' not in s:
        kol += 1
print(kol)
