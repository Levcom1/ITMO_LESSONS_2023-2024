def task(s, p):
    if s >= 50:
        return p % 2 == 0
    if p == 0:
        return 0
    oper = [task(s + 5, p - 1), task(s * 3, p - 1)]
    return any(oper) if (p - 1) % 2 == 0 else all(oper)


print('19a', [i for i in range(1, 50) if task(i, 1)])
print('19b', [i for i in range(1, 50) if task(i, 2)])
print('20', [i for i in range(1, 50) if task(i, 3) and not task(i, 1)])
print('21', [i for i in range(1, 50) if task(i, 4) and not task(i, 2)])

print('---')


def task(s1, s2, p):
    if s1 == s2:
        return p % 2 == 0
    if p == 0:
        return False
    if s1 < s2:
        oper = [task(s1 + 1, s2, p - 1), task(s1 + 3, s2, p - 1)]
    else:
        oper = [task(s1, s2 + 1, p - 1), task(s1, s2 + 3, p - 1)]
    return any(oper) if (p - 1) % 2 == 0 else all(oper)


print([i for i in range(1, 32) if task(17, i, 2)])
print([i for i in range(1, 32) if task(17, i, 3) and not task(17, i, 1)])
print([i for i in range(1, 32) if task(17, i, 4) and not task(17, i, 2)])
