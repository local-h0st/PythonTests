from functools import reduce

digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': '.'}


def str2float(s):
    flag = 1
    count = 0

    def char2num(char):
        return digits[char]

    def add(a, b):
        print('a = ', a)
        print('b = ', b)
        nonlocal flag
        nonlocal count
        if b == '.':
            flag = 0
            return a
        elif flag == 0:
            count += 1
        return a * 10 + b

    def power(base, times):
        res = 1
        if times != 0:
            for i in range(times):
                res *= base
        return res

    return reduce(add, (map(char2num, s))) / power(10, count)


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
