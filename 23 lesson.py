print('--- 17.7 ---')
f1 = open('23_27_7_A.rtf')
f2 = open('23_27_7_B.rtf')
n1 = int(f1.readline())
n2 = int(f2.readline())
ost = [0] * 11
nums1 = [int(f1.readline()) for i in range(17)]
nums2 = [int(f2.readline()) for g in range(17)]
k = 0
cnt = 0
for i in range(17, n1):
    tmp = int(f1.readline())
    ost[nums1[i - 17] % 11] += 1
    k += ost[(11 - tmp % 11) % 11]
    nums1.append(tmp)

for g in range(17, n2):
    tmp = int(f2.readline())
    ost[nums2[g - 17] % 11] += 1
    cnt += ost[(11 - tmp % 11) % 11]
    nums2.append(tmp)
print(k, cnt)

print('--- 17.8 ---')
f1 = open('23_27_7_A.rtf')
f2 = open('23_27_7_B.rtf')
n1 = int(f1.readline())
n2 = int(f2.readline())
ost1 = [[0] * 23 for i in range(23)]
ost2 = [[0] * 23 for g in range(23)]
k = 0
cnt = 0
for i in range(n1):
    tmp1 = int(f1.readline())
    for j in range(23):
        k += ost1[j][(i - j) % 23 - tmp1 % 23]
    ost1[i % 23][tmp1 % 23] += 1

for g in range(n2):
    tmp2 = int(f2.readline())
    for a in range(23):
        cnt += ost2[a][(g - a) % 23 - tmp2 % 23]
    ost2[g % 23][tmp2 % 23] += 1
print(k, cnt)

print('--- 17.9 ---')
f1 = open('23_27_8_A.rtf')
f2 = open('23_27_8_B.rtf')
n1, k1 = [int(i) for i in f1.readline().split()]
n2, k2 = [int(g) for g in f2.readline().split()]
ost1 = [int(f1.readline()) for i in range(2 * k1)]
ost2 = [int(f2.readline()) for g in range(2 * k2)]
first1 = 0
first2 = 0
second1 = 0
second2 = 0
third1 = 0
third2 = 0
for i in range(2 * k1, n1):
    first1 = max(first1, ost1[i - 2 * k1])
    second1 = max(second1, ost1[i - k1])
    ost1.append(int(f1.readline()))
    third1 = max(third1, ost1[-1])

for g in range(2 * k2, n2):
    first2 = max(first2, ost2[g - 2 * k1])
    second2 = max(second2, ost2[g - k1])
    ost2.append(int(f2.readline()))
    third2 = max(third2, ost2[-1])
print(first1 * second1 * third1, first2 * second2 * third2)

print('--- 17.11 ---')
f = open('23_27_9_B.rtf')
n = int(f.readline())
ost = [[0] * 6 for i in range(6)]
k = 0
for i in range(n):
    tmp = int(f.readline())
    two = 0
    five = 0
    while tmp % 2 == 0 or tmp % 5 == 0:
        if tmp % 2 == 0:
            two += 1 if two < 5 else 0
            tmp //= 2
        if tmp % 5 == 0:
            five += 1 if five < 5 else 0
            tmp //= 5
    if two <= 4 and five <= 4:
        k += ost[4 - two][4 - five]
    if two <= 4:
        for j in range(4 - five + 1, 6):
            k += ost[4 - two][j]
    if five <= 4:
        for k in range(4 - two + 1, 6):
            k += ost[k][4 - five]
    ost[two][five] += 1
print(k)

print('--- 17.16 ---')
f = open('23_27_9_B.rtf')
n = int(f.readline())
ost = [0] * 71
cur_sum = 0
k = 0
for i in range(n):
    tmp = int(f.readline())
    ost[cur_sum % 71] += 1
    cur_sum += tmp
print(k)

print('--- ---')
f = open('')
n = int(f.readline())
p = []
for i in f.readline():
    tmp = [int(j) for j in i.split()]
    tmp[1] = tmp[1] % 36 if tmp[1] % 36 == 0 else tmp[1] % 36 == 1
    p.append(tmp)
p.sort()

res = [0] * n
res[0] = p[0][1]
for i in range(1, n):
    res[i] = res[i - 1] + p[i][1]

s = 0
for i in range(n):
    s += abs(p[0][0] - p[i][0] * p[i][1])

minsum = s
for i in range(1, n):
    diff = p[i][0] - p[i - 1][0]
    s = s + diff * res[i - 1] - diff * (res[n - 1] - res[i - 1])
    minsum = min(minsum, s)
