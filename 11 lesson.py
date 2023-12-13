print('--- 6.19 ---')
# 6.19
for K in range(2):
    for L in range(2):
        for M in range(2):
            for N in range(2):
                F = (not L and not (not M or N)) <= (L or (not (M and K)))
                if F == 0:
                    print(K, L, M, N)

print('--- 6.24 ---')
# 6.24
AL = {1, 2, 3, 4, 5, 6, 7, 8}
A = {1, 4, 5}
B = {2, 5, 6, 8}
C = {3, 4, 5, 6, 7}
not_A = AL - A
not_C = AL - C
not_B = AL - B
print((B & not_C) | C & ((A & B) | (not_A & not_B)))

print('--- 6.27 ---')
# 6.27
for x in range(0, 10000):
    if (x > 1) and ((x < 5) <= (x < 3)) is True:
        print(x)
        break

print('--- 6.33 ---')
# 6.33
for a in range(0, 10000):
    flag = True
    for x in range(0, 10000):
        for y in range(0, 10000):
            f = x + 3 * y < a or y > 2 * x or x > 78
            if f is False:
                flag = False
                break
        if f is False:
            flag = False
            break
    if flag is True:
        print(a)
        break
