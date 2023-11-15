"""
for i in range(1, 10):
    if i == 5:
        break
    print(i)
"""

"""
a = 5
while a < 10:
    if a % 2 == 0:
        a += 1
        continue
    print(a)
    a += 1
"""

"""
a = str('123456')
b = a[-1::]
print(b)
"""

"""
S = 'Hello, world!'
print(S.find('ll'))
print(S[-8:-2])
"""

"""
S = 'abababababab'
print(S.replace('a', 'A'))
print(S.replace('a', 'A', 4))
"""

"""
n = int(input())
i = 21
while i <= n:
    if str(i) == str(i)[::-1]:
        print(i)
    i += 1
"""

"""
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list[5])
print(list[-2])
print(list[2:6])
print(list[:6])
print(list[6:])
print(list[2:8:2])
"""

"""
f = open('input.txt', 'r')
for line in f:
    list.append(int(line.rstrip()))

# strip() - убирает служебные символы
"""

print('--- 1 ---')
# 1
count = 0
for i in range(10):
    n = int(input())
    if n % 2 == 0:
        count += n
print(count)

print('--- 2 ---')
# 2
n = int(input())
for i in range(10, 100):
    if i % n == 0 or i % 10 == n or i // 10 == n:
        print(i)
