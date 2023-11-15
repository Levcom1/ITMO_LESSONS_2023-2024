print('--- 8 ---')
# 8
numbers = [i for i in range(2, 23, 2)]
print(numbers)
max_sum = 0
max_index = 0

for number in numbers:
    digit_sum = number % 10 + number // 10
    if digit_sum > max_sum:
        max_sum = digit_sum
        max_index = numbers.index(number)
print(max_index, 'Index of the maximum sum')

print('--- 9 ---')
# 9
numbers = [i for i in range(2, 23, 2)]
print(numbers)
max_sum = 0
max_elements = []

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        digit_sum = i % 10 + i // 10
        digit_sum2 = j % 10 + j // 10
        count = digit_sum + digit_sum2
        if count > max_sum:
            max_sum = count
            max_elements = (numbers[i], numbers[j])
print(max_elements, 'Two maximum elements')

"""
str1 = ['a', 'u', 'i', 'o']
str2 = ', '.join(str1)
print(str2)
"""

print('--- 1 ---')
# 1
a = input()
if a.count('a') > a.count('b'):
    print('More letters a')
elif a.count('a') == a.count('b'):
    print('Same')
else:
    print('More letters b')

print('--- 2 ---')
# 2
s = 'jksgkf ksdgf43 , . /'
a = input()
b = input()
print(a, s.count(a), b, s.count(b))
if a.count('a') > a.count('b'):
    print(b, 'реже')
elif a.count('a') == a.count('b'):
    print('Same')
else:
    print(a, 'реже')

print('--- 3.1 ---')
# 3.1
a = input()
print(len(a.split()))

print('--- 3.2 ---')
# 3.2
"""
a = input()
b = int(input())
word_len = len(a.split())
words = a.split()
for i in words:
    len_i = len(i)
    if len_i == b:
        print(i)
"""
