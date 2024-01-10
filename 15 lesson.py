print('--- 17 ---')
for a in range(1, 1000):
    counter = 0
    for x in range(3450):
        if ((x % a == 0) <= ((x % 15 == 0) or (x % 23 != 0))) and (x + a >= 150):
            counter += 1
    if counter == 3450:
        print(a)
        break

print('--- 18 ---')
print('x y z w')
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                F = (not x or y) and not (w <= z)
                if F:
                    print(x, y, z, w)
