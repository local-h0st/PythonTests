import functools
import time
from inspect import isfunction

# Question 1
print('######### Question 1 #########')


def metric(fn):
    rst = 0

    @functools.wraps(fn)
    def decoratedFunc(*args, **kwargs):
        nonlocal rst
        t1 = time.time()
        rst = fn(*args, **kwargs)
        t2 = time.time()
        print('%s executed in %s ms' % (fn.__name__, t2 - t1))
        return rst

    return decoratedFunc


@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

# Question 2
print('######### Question 2 #########')


def logger(f):
    rst = None
    functools.wraps(f)

    def decoratedF(*args, **kwargs):
        nonlocal rst
        print('[Decorator]', f.__name__, 'begin')
        rst = f(*args, **kwargs)
        print('[Decorator]', f.__name__, 'ended')
        return rst

    return decoratedF


@logger
def func(msg):
    print('[Func] :', msg)
    return '[Func] : ' + msg


print('Returning value :', func('purelove'))


# Question 3
print('######### Question 3 #########')


def log(parameter):
    if isfunction(parameter):
        @functools.wraps(parameter)
        def decoratedFunction(*args, **kwargs):
            print('[Decorator] Default msg')
            return parameter(*args, **kwargs)

        return decoratedFunction
    else:
        def createFunc(f):
            @functools.wraps(f)
            def decoratedFunction(*args, **kwargs):
                print('[Decorator]', parameter)
                return f(*args, **kwargs)

            return decoratedFunction

        return createFunc



@log
def f1(s):
    print('[Function 1][Print()]', s)
    return '[Function 1][Return value] ' + s


@log('PureLov3 created')
def f2(s):
    print('[Function 2][Print()]', s)
    return '[Function 2][Return value] ' + s


rst1 = f1('Function 1')
rst2 = f2('Function 2')

print(rst1)
print(rst2)

# Nice done!通过判断传入的是否是函数来实现不同的返回，通过这种方式支持两种语法!
