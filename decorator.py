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

def decoratorFunction(name_of_func_to_be_decorated):
    def decoratedFunc(*args, **kwargs):
        # decorating...
        print('[Decorator]')
        # decorator ended
        return name_of_func_to_be_decorated(*args, **kwargs)

    return decoratedFunc


# Way 1:
@decoratorFunction
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

#################################
