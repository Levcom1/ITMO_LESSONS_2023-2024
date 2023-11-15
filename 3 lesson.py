# a = int(input('a '))
# b = int(input('b '))
# while a > b:
#     a += 1
#     print(a)
# print(b)
#########
# a = 10
# b = 100
# i = a
# while i <= b:
#     if i % 2 == 0:
#         print(i)
#     i += 1

print('--- 1 ---')
# 1
n = int(input())
i = 0
while n > 0:
    a = n % 10
    if a % 2 == 0:
        i += 1
    n //= 10
print(i)

print('--- 2 ---')
# 2
n = int(input())
i = 1
while i <= n:
    if i % 2 == 1 and n % i == 0:
        print(i)
    i += 1

print('--- 3 ---')
# 3
n = int(input())
i = 10
while 9 < i < 100:
    if i % n == 0 or i % 10 == n or i // 10 == n:
        print(i)
    i += 1

print('--- 4 ---')
# 4
n = int(input())
i = 0
while n > 0:
    i += n % 10
    n = n // 10
print(i)

print('--- 5 ---')
# 5
n = int(input())
i = 0
while i != 10:
    i = 0
    while n != 0:
        i += n % 10
        n //= 10
    print(i)
    if i != 10:
        n = int(input())

print('--- 6 ---')
# 6
n = int(input())
s = 2
while n != 1:
    if n % s == 0:
        print(s)
        n //= s
    else:
        s += 1

print('--- 7 ---')
# 7
n = int(input())
s = 2
d = 0
while n != 1:
    if n % s == 0 and d != s:
        if d != s:
            print(s)
        n //= s
        d = s
    else:
        s += 1

print('--- 8 ---')
# 8
n = int(input())
while n > 0:
    work = n
    a = ''
    while work > 0:
        a += str(work % 10)
        work //= 10
        if str(n) == a:
            print(n)
        n -= 1
