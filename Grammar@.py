def f(func):
    print('[print] f')
    return func()

@f
def a():
    print('[print] a')
    return '[return value] a'
# @f相当于把@下一行定义的函数a的函数名当成f的参数传进f
# 就那么简单
