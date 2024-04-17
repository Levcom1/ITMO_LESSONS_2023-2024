from turtle import *

'''
print('--- 13.15 ---')

left(90)
tracer(100)

for i in range(7):
    forward(10 * 25)
    right(90)
penup()
dots = 0

for x in range(-10, 11):
    for y in range(-30, 30):
        setpos(x * 25, y * 25)
        dot(5, 'red')
        if 0 <= x <= 10 and 0 <= y <= 10:
            dots += 1
print(dots)
done()
'''

print('--- 13.25 ---')


def count_pr(cur, fin):
    if cur == fin:
        return 1
    elif cur > fin:
        return 0
    else:
        return count_pr(cur + 1, fin) + count_pr(cur * 2, fin)


print(count_pr(1, 10) * count_pr(10, 20))

print('--- 13.29 ---')


def count_pr(cur, fin, sum3: list):
    if cur == fin:
        for i in range(2, len(sum3)):
            if (sum3[i] + sum3[i - 1] + sum3[i - 2]) % 17 == 0:
                return 1
    if cur > fin:
        return 0
    return count_pr(cur + 2, fin, sum3 + [cur]) + count_pr(cur * 3, fin, sum3 + [cur]) + count_pr(cur * 5, fin, sum3 + [cur])


print(count_pr(4, 556, []))

print('--- 13.27 ---')


def count_pr(cur, fin):
    if cur == fin:
        return 1
    elif cur > fin:
        return 0
    else:
        return count_pr(cur + 1, fin) + count_pr(cur * 2, fin)


print(count_pr(2, 14) * count_pr(14, 24) * count_pr(26, 29))

print('--- 13.28 ---')


def count_pr(cur, fin):
    if cur == 34:
        return 0
    if cur == fin:
        return 1
    elif cur > fin:
        return 0
    else:
        return count_pr(cur + 2, fin) + count_pr(cur * 2, fin)


print(count_pr(2, 18) * count_pr(18, 40))

print('---14.6 ---')
count = 0
max_el = 0
for i in range(1017, 7937 + 1, 3):
    if i % 7 != 0 and i % 17 != 0 and i % 19 != 0 and i % 27 != 0:
        count += 1
        max_el = max(max_el, i)
print(count, max_el)

print('--- 14. ---')
f = open('19_14_10.rtf')
nums = [int(i) for i in f]
max_square_sum = count = max_square = 0
for x in nums:
    if abs(x) % 10 == 3:
        max_square = max(max_square, x ** 2)
for i in range(len(nums) - 1):
    ch = (abs(nums[i] % 10 == 3) and abs(nums[i + 1] % 10 != 3)) or (abs(nums[i] % 10 != 3) and abs(nums[i + 1] % 10 != 3))
    if ch and nums[i] ** 2 + nums[i + 1] ** 2 >= max_square:
        count += 1
        max_square_sum = max(max_square_sum, nums[i] ** 2 + nums[i + 1] ** 2)
print(count, max_square_sum)
