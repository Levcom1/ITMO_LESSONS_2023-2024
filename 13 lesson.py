print('--- 7.12 ---')
# 7.12
print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            if ((x and not y or z) and (y and z or not y)) == 0:
                print(x, y, z)

print('--- 7.13 ---')
# 7.13
print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            if (x and z or not y) and (y and not z or z):
                print(x, y, z)

print('--- 7.15 ---')
# 7.15
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (not w and y and (not z or w)) == 0:
                    print(x, y, z, w, int(not w and y and (not z or w)))

print('--- 7.16 ---')
# 7.16
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((x or y) and not (y == z) and not w) == 1:
                    print(x, y, z, w, int((x or y) and not (y == z) and not w))

print('--- 7.17 ---')
# 7.17
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((not (y <= z)) or (x == w) or x) == 0:
                    print(x, y, z, w, int(not (y <= z) or (x == w) or x))

print('--- 7.18 ---')
# 7.18
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((x and not y) or (x == z) or not w) == 0:
                    print(x, y, z, w, int((x and not y) or (x == z) or not w))
