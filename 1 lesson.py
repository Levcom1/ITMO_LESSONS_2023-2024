print('--- 1 ---')
# 1
a = int(input())
b = a // 1024
c = b // 1024
d = a / 1024
e = d / 1024

print(a, 'byte = ', c, 'Mbyte,', b, 'Kbyte and', a, 'byte')
print(a, 'byte = ', b, 'Kbyte = ', e, 'Mbyte')

print('--- 2 ---')
# 2
a = int(input())
b = a // 1000
c = a // 100 % 10
d = a // 10 % 10
e = a % 10
print(b + c + d + e)

print('--- 3 ---')
# 3
a = int(input())
b = a // 1000 % 2
c = a // 100 % 10 % 2
d = a // 10 % 10 % 2
e = a % 10 % 2
print(4 - (b + c + d + e))

print('--- 4 ---')
# 4
a = int(input())
b = a // 1000
c = a % 10
print(b - c)

print('--- 5 ---')
# 5
a = int(input())
b = a // 100 % 10
c = a // 10 % 10
d = a % 10
print(b, c, d)
