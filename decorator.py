import functools


def rtnWapperedFunc(f):
    def WapperedFunc(x):
        print('[Decorator]Calling', f.__name__)
        return f(x)

    return WapperedFunc


@rtnWapperedFunc
def func2(x):
    print('Printing x :', x)
    return 'Returning x : ' + str(x)


def func(x):
    print('Printing x :', x)
    return 'Returning x : ' + str(x)


fu = rtnWapperedFunc(func)

rst = fu(1)

print(rst)

print(func2(2))

###################################
print('########## Basic usage ############')


def decoratorFunction(name_of_func_to_be_decorated):
    def decoratedFunc(*args, **kwargs):  # (*args, **kw)使decoratedFunc()函数可以接受任意参数的调用。
        # decorating...
        print('[Decorator]')
        # decorator ended
        return name_of_func_to_be_decorated(*args, **kwargs)  # return的时候会调用原来的函数！是调用！

    return decoratedFunc


# Way 1:
@decoratorFunction  # decoratorFunction()返回装饰后的函数，只要写decoratorFunction不用写()
def originFunc(a):
    print('hello', a)
    return a


print(originFunc(666))


# Way 2:
def originFunc2(a):
    print('hello', a)
    return a


f = decoratorFunction(originFunc2)

print(originFunc2(666))
print(f(666))

####################################################

# Advanced

print('####### Advanced:Free to set msgs ######')


def oriFunc(message):
    print('msg{' + message + '} printed from oriFunc()')
    return 'msg{' + message + '} returned by oriFunc()'


def h(msg):
    def g(oriF):
        def f(*args, **kwargs):
            print(msg)
            return oriF(*args, **kwargs)

        return f

    return g


a = h('msg from h')
b = a(oriFunc)
c = b('purelove')
print('#c', c)

d = h('msg from h')(oriFunc)
e = d('PureLov3')
print(e)

i = h('msg from h')(oriFunc)('purelov3')
print(i)

print("######## using @ ########")


@h('[Decorator] msg from h using @')  # h()返回的不是装饰后的函数，而是一个能够生成返回装饰后函数的函数，而h('xxxxx')()才返回装饰后的函数，因此不写最后的(),只写h('xxxxx')
def ff(m):
    print('{', m, '} printed in function ff')
    # return '{', m, '} returned by function ff'    这么写返回的是一个tuple，而不是拼凑的字符串
    return '{ ' + m + ' } returned by function ff'


print(ff('msg from inside ff()'))

####################################################

print('########## about __name__ ##########')


def createDecoratedFuncs(oriFunc):
    def decoratedF(*args, **kwargs):
        print('[ Decorator ] decorated head')
        return oriFunc(*args, **kwargs)

    return decoratedF


@createDecoratedFuncs
def fff(str):
    print('[ msg printed in fff ]', str)
    return '[ msg returned by fff ] ' + str


rst = fff('purelove')
print(rst)
print('{ fff.__name__ : }', fff.__name__)


def createDecoratedFuncs2(oriFunc):
    @functools.wraps(oriFunc)
    def decoratedF(*args, **kwargs):
        print('[ Decorator ] decorated head')
        return oriFunc(*args, **kwargs)

    return decoratedF


# add @functools.wraps(oriF)
@createDecoratedFuncs2
def ggg(str):
    print('[ msg printed in ggg ]', str)
    return '[ msg returned by ggg ] ' + str


rst = ggg('purelove')
print(rst)
print('{ ggg.__name__ : }', ggg.__name__)


# 带参数的decorator：
def rtnCrtFunc(msg):
    def crtFunc(f):
        @functools.wraps(f)
        def decoratedFucn(*args, **kwargs):
            print('[Decorator msg] :', msg)
            return f(*args, **kwargs)

        return decoratedFucn

    return crtFunc


@rtnCrtFunc('message given as parameter')
def hhh(msg):
    print('[msg printed in hhh()]', msg)
    return '[msg returned by hhh()] ' + msg


print(hhh('purelove'))
print('hhh.__name :', hhh.__name__)



def a(msg):
    print('[msg printed in hhh()]', msg)
    return '[msg returned by hhh()] ' + msg


rst = rtnCrtFunc('this is msg given as parameter for function a()')(a)('this is msg given to function a()')
print(rst)
print(rtnCrtFunc('this is msg given as parameter for function a()')(a).__name__)
