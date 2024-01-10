# n = 2 * 3 ** 30 + 2 * 3 ** 25 + 3 ** 6 + 7 * 3 ** 4 + 2 * 9 ** 2 + 1
#
#
# def counts(number, system):
#     s = ''
#     while number != 0:
#         s += str(number % system)
#         number //= system
#     return s[::]
#
#
# a = counts(n, 9)
# print(a.count('0'))
# print(a)

# for Е in range(2):
#     for Н in range(2):
#         for О in range(2):
#             for Т in range(2):
#                 F = (not L and not (not M or N)) <= (L or (not (M and K)))
#                 if F == 0:
#                     print(K, L, M, N)

# print(bin(148)[2:].zfill(8), bin(76)[2:].zfill(8), bin(112)[2:].zfill(8), bin(147)[2:].zfill(8))
# print(bin(148)[2:].zfill(8), bin(76)[2:].zfill(8), bin(112)[2:].zfill(8), bin(144)[2:].zfill(8))
# print(int('11111100', 2))

# a = {0: 'И', 1: 'П', 2: 'Т', 3: 'Ф'}
# k = 0
# for i in range(0, len(a)):
#     for n in range(0, len(a)):
#         for m in range(0, len(a)):
#             for j in range(0, len(a)):
#                 k += 1
#                 if k == 201:
#                     print(a[i], a[n], a[m], a[j])

# for x in range(15):
#     n1 = 1 * 15**4 + 3 * 15**3 + 5*15**2 + x * 15 + 7
#     n2 = 7 * 15**4 + x * 15**3 + 5 * 15**2 + 3 * 15 + 1
#     if (n1+n2) % 14 == 0:
#         print((n1+n2) // 14)
#         break

# for i in range(1000000):
#     s = bin(i)[2::]
#     s += str(s.count('1') % 2)
#     s += str(s.count('1') % 2)
#     if int(s, 2) > 335:
#         print(int(s, 2))
#         print(i)
#         break

# def check():
#     for x in range(0, 1000):
#         if ((not p + a) * (not q + a)) == 0:
#             return False
#     return True
#
#
# p = set(range(20, 32))
# q = set(range(17, 27))
# ans = float('inf')
# for l in range(0, 200):
#     for r in range(l + 1, 200):
#         a = set(range(l, r))
#         if check():
#             ans = min(ans, r - l)
# print(ans)

# for a in range(1, 500):
#     f = True
#     for x in range(1, 500):
#         if ((not (x % a == 0) or ((x % 15 == 0) or not(x % 23 == 0))) and (x + a >= 150)) == 0:
#             f = False
#     if f == True:
#         print(a)

print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((w <= y) and ((x <= z) == (y <= x))) == 0:
                    print(x, y, z, w, int((w <= y) and ((x <= z) == (y <= x))))
