print('--- 16.7 ---')
"""
f = open('21_16_7.rtf')
n, s = map(int, f.readline().split())
all1 = [int(f.readline()) for i in range(n)]


last = all1[0]
k = 0

while all1:
    count = 0
    ost = s - count
    count += last
    curli = last
    for j in range(len(all1), 0, -1):

        if count <= ost:
            k += 1
        if all1[j] > ost:
            break
        else:
            count += all1.pop(j)
print(k, count)
"""

print('--- 16.13 ---')
f = open('21_16_13.rtf')
n = int(f.readline())
s = list(map(int, f.readlines()))
s.sort(reverse=True)
print(sum(s[n//5:]))
print(sum(s) - sum(s[4::5]))

print('--- 16.18 ---')
f = open('21_16_18.rtf')
n = int(f.readline())
a = []
d = {}
for i in range(n):
    v = int(f.readline())
    a.append(v)
    d[v] = 1
minAvg = 2 * 10 ** 9
c = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        avg = (a[i] + a[j]) // 2
        if a[i] % 2 != 0 or a[j] % 2 != 0:
            continue
        if d.get(avg):
            c += 1
            minAvg = min(avg, minAvg)
print(c, minAvg)
