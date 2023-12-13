print('--- 1 ---')
# 1
a = int(input())
b = int(input())
if a > b:
    print('a is bigger')
else:
    print('b is bigger')

print('--- 2 ---')
# 2
a = int(input())
b = int(input())
if a > 1:
    print('1')
elif b > 1:
    print('2')
else:
    print('3')

print('--- 3 ---')
# 3
a = int(input())
b = int(input())
if a > 2 or b < 4:
    print('1')
elif a < 2 and not b < 4:
    print('2')
else:
    print('3')

print('--- 4 ---')
# 4
a = int(input())
b = int(input())
print('1') if a > b else print('2')

print('--- 5 ---')
# 5
a = 11
b = 4
c = 15
if a > b < c:
    print('b is smallest')

print('--- 1 ---')
# 1
a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(a, b, c, d)

minimum = a
minplace = 1
if b < minimum:
    minimum = b
    minplace = 2
if c < minimum:
    minimum = c
    minplace = 3
if d < minimum:
    minimum = d
    minplace = 4
print(minimum, 'is smallest number, ', minplace, 'number')

maximum = a
maxplace = 1
if b > maximum:
    maximum = b
    maxplace = 2
if c > maximum:
    maximum = c
    maxplace = 3
if d > maximum:
    maximum = d
    maxplace = 4
print(maximum, 'is biggest number, ', maxplace, 'number')

print('--- 2 ---')
# N2
a = int(input())
b = int(input())
c = int(input())
d = b * b - 4 * a * c
if d > 0:
    print('x1 =', (- b + d ** 0.5) / (2 * a), '\n'
          'x2 =', (- b - d ** 0.5) / (2 * a))
elif d == 0:
    print('x =', - b / (2 * a))
else:
    print('No roots')

print('--- 3 ---')
# N3
a = int(input())
b = int(input())
c = int(input())
if b < a < b + c and a > c:
    print('YES')
elif a < b < a + c and b > c:
    print('YES')
elif a < c < b + a and c > b:
    print('YES')
else:
    print('NO')

print('--- 4 ---')
# N4
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if c > a and d > b:
    print('YES')
elif c > b and d > a:
    print('YES')
else:
    print('NO')

print('--- 5 ---')
# N5
a = int(input())
if a % 10 == 1:
    print(a, 'год')
elif 1 < a % 10 < 5:
    print(a, 'года')
else:
    print(a, 'лет')
