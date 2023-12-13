print('--- 6.33 ---')
# 6.33
for a in range(0, 1000):
    k = 0
    for x in range(79):
        for y in range(157):
            if x + 3 * y < a or y > 2 * x or x > 78:
                k += 1
    if k == 79 * 157:
        print(a)
        break

print('--- 6.37 ---')
# 6.37
# for a in range(1000, 1, -1):
#     k = 0
#     for x in range(1, 301):
#         for y in range(1, 301):
#             if not (y - 2 * x == 7) or a < 8 * x ** 2 + 2 * y or a < y ** 2 - 40:
#                 k += 1
#     if k == 300 * 300:
#         print(a)
#         break

print('--- 6.39 ---')
# 6.39
for a in range(1, 1000):
    k = 0
    for x in range(1, 1001):
        if not (x & 25 != 0) or (not (x & 17 == 0) or (x & a != 0)):
            k += 1
    if k == 1000:
        print(a)
        break

print('--- 6.45 ---')
# 6.45
for a in range(1000, 1, -1):
    k = 0
    for x in range(1000):
        if x % a == 0 or (not (x % 6 == 0) or not (x % 9 == 0)):
            k += 1
    if k == 1000:
        print(a)
        break

print('--- 6.52 ---')
# 6.52
p = {i for i in range(27, 51)}
q = {i for i in range(35, 67)}
length = 68 - 26
for l in range(27, 67):
    for r in range(27, 67):
        a = {i for i in range(l, r)}
        c = 0
        for x in (26, 27, 34, 35, 49, 50, 65, 66, 67):
            if (x in p) <= (((x in q) and (not (x in a))) <= (not (x in p))):
                c += 1
        if c == 9 and length >= len(a):
            length = len(a)
            print(a, length)
