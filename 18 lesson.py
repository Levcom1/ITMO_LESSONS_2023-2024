from turtle import *

print('--- 13.6 ---')
a = '8' * 68
while ('222' in a) or ('888' in a):
    if '222' in a:
        a = a.replace('222', '8', 1)
    else:
        a = a.replace('888', '2', 1)
print(a)

print('--- 13.8 ---')
for i in range(119, 1000):
    a = i * '3'
    while '33' in a:
        a = a.replace('33', '5', 1)
        a = a.replace('5555', '33', 1)
    if a == '5553':
        print(i)
        break

print('--- 13.9 ---')
maxi = 0
mini = 100000
for i in range(155, 1000):
    a = i * '1'
    while '111' in a:
        a = a.replace('111', '2', 1)
        a = a.replace('2222', '1', 1)
    if maxi < a.count('2'):
        maxi = a.count('2')
        mini = i
print(mini)

print('--- 13.10 ---')
for i in range(1, 100):
    for x in range(1, 100):
        a = '0' + i * '1' + x * '2'
    while '01' in a or '02' in a:
        a = a.replace('01', '220', 1)
        a = a.replace('02', '1110', 1)


def prost(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


mini = 1000000
for e in range(1, 100):
    for d in range(1, 100):
        s = '0' + e * '1' + d * '2'
        if len(s) <= 30:
            break
        sumA = 0
        for i in range(len(s)):
            sumA += int(s[i])
        while '01' in s or '02' in s:
            s = s.replace('01', '220', 1)
            s = s.replace('02', '1110', 1)
        sumB = 0
        for i in range(len(s)):
            sumB += int(s[i])
        if prost(sumB):
            mini = min(mini, sumA)
print(mini)

# turtle
'''
left(90)
for i in range(5):
    forward(10 * 25)
    right(90)
penup()
speed(0)
for x in range(-10, 10):
    for y in range(-10, 10):
        setpos(x * 25, y * 25)
        dot(4, 'red')
done()
'''

left(90)
for i in range(4):
    forward(5 * 25)
    right(90)
right(180)
for i in range(4):
    forward(5 * 25)
    right(90)
penup()
'''
speed(0)
for x in range(-10, 10):
    for y in range(-10, 10):
        setpos(x * 25, y * 25)
        dot(4, 'red')
'''
points = 0
for x in range(-10, 10):
    for y in range(-10, 10):
        setpos(x * 25, y * 25)
        dot(4, 'red')

for i in range(-10 * 25, 11 * 25):
    for j in range(-20 * 25, -21 * 25):
        if (i, j) != (0, 0) and -5 * 25 <= i <= 5 * 25 and -10 * 25 <= j <= 10 * 25:
            points += 1
print(points)
done()
