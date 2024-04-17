print('--- 17.1 ---')
# 1
f = open('22_27_1.rtf')
n = int(f.readline())
line = [int(i) for i in f.readline().split()]
left = 0
right = line.index(0)
maxlen = 0
for j in range(line.index(0), len(line)):
    if line[j] == 0:
        maxlen = max(maxlen, left + right)
        left = right
        right = 0
    else:
        right += 1
print('1.', maxlen)

# 2
f = open('22_27_1.rtf')
n = int(f.readline())
a = [i for i in f.readline().split()]
s = ''.join(a).split('0')
maxS = 0
for i in range(len(s)-1):
    maxS = max(len(s[i] + s[i + 1]), maxS)
print('2.', maxS)

print('--- 17.2 ---')
f = open('22_27_2.rtf')
n, k = [int(i) for i in f.readline().split()]
numbers = [int(i) for i in f.readline().split()]
line_sum = 0
sums = [0]
count = 0
for j in numbers:
    line_sum += j
    sums.append(line_sum)
    if line_sum - k in sums:
        count += 1
print(count)

print('--- 17.3 ---')
f = open('22_27_3.rtf')
n, k = [int(i) for i in f.readline().split()]
set1 = [int(i) for i in f.readline().split()]
set2 = [int(i) for i in f.readline().split()]
res = []
for num in set1:
    if num in set2 and num not in res:
        res += min(set1.count(num), set2.count(num)) * [num]
res.sort()
print(set1)
print(set2)
print(res)
