# 定制类嘛 个性化我最喜欢了 一般就是通过特殊变量__xxx__来整
# __len__
# __str__ 和 __repr__
# __iter__ 和 __next__
# __getitem__
# __getattr__
# __call__
# 这不就是魔术方法吗!!反序列化要来啦!!
# 也很像C++的运算符重载
import functools
from collections.abc import Iterable, Iterator


# 自定义装饰器
def log(msg):
    def rtnWrappedFunc(f):
        @functools.wraps(f)
        def wrappedFunc(*args, **kwargs):
            print('[log decorator] calling', msg)
            return f(*args, **kwargs)

        return wrappedFunc

    return rtnWrappedFunc


class A(object):
    def __init__(self, s):
        self.__description = s
        self.__x = 1
        self.__y = 1

    @property
    def desc(self):
        return self.__description

    @desc.setter
    def desc(self, new_desc):
        self.__description = new_desc

    @log('__len__')
    def __len__(self):
        return 16

    @log('__str__')
    def __str__(self):
        return 'this is a instance of class A(by __str__)'

    @log('__repr__')
    def __repr__(self):
        return 'this is a instance of class A(by __repr__)'

    @log('__iter__')
    def __iter__(self):
        # return list(range(5))    list好像不行 因为没有next()方法，有next的应该是yield
        # 但是很奇怪啊 for in 循环的只要是iterable就行
        # print(isinstance([1, 2, 3], Iterable))    True
        # print(isinstance([1, 2, 3], Iterator))    False
        # 凡是可作用于next()函数的对象都是Iterator类型
        # __iter__必须返回一个可迭代对象，并且for in会调用next()，因此，返回的必须是Iterator！

        # return (x*x for x in range(5))    成功!输出0 1 4 9 16
        # def g():
        #     string = ''
        #     for x in range(5):
        #         string += str(x)
        #         yield 'string yielded : ' + string
        #
        # return g()                        成功!
        return self  # 返回自己，在这之后for会一直去调用__next__()，就不用接着管__iter__()了

    @log('__next__')
    def __next__(self):  # 因为是函数调用，所以用的是return而不是yield
        self.__x, self.__y = self.__y, self.__x + self.__y
        if self.__x > 50:
            raise StopIteration()
        return self.__x

    @log('__getitem__')
    def __getitem__(self, item):  # 可以和__item__ __next__ 搭配组合拳，也可以完全不相关 毕竟本质是一个函数调用而已
        # []里面传入的东西就是item 我甚至可以传入一个类的实例，加一个isinstance的判断就行，就像是传入的slice就是一个对象只不过大概是做了简化而已，写法简化了但实际上是一个slice对象
        # 如果我要写得和上面两个魔法方法一样的话 我就再写一遍fib的计算式，计算到第item个之后return就行
        # 这东西可以用来模拟下标和切片操作，可以做边界检查，也可以搞一些完全不相干的东西
        # 比如完全没关系的例子：
        if isinstance(item, int):
            return 'like a list or tuple , item : ' + str(item)
        elif isinstance(item, slice):
            # 可以干点正事但是我不想
            # return {'start': slice.start, 'end': slice.stop, 'step': slice.step}      {'start': <member 'start' of 'slice' objects>, 'end': <member 'stop' of 'slice' objects>, 'step': <member 'step' of 'slice' objects>}
            return {'start': item.start, 'end': item.stop, 'step': item.step}
            # 从输出可以看到，传入的slice对象的参数没有合理性判断，start stop step全都没有限制
        elif isinstance(item, str):
            return 'look it as a dict with index ' + item
        else:
            raise RuntimeError('collapsed at __getitem__ else clause')

    @log('__setitem__')
    def __setitem__(self, key, value):  # 看成dict需要
        pass

    @log('__delitem__')
    def __delitem__(self, key):  # 看成dict需要
        pass


    # 尝试调用不存在的属性时才会调用该函数
    @log('__getattr__')
    def __getattr__(self, item):
        if item == 'func':
            return lambda s: 'lambda function value returned by __getattr__ with argument : ' + s
        elif item == 'gunc':
            return lambda s: print('gunc() with argument :', s)
        elif item == 'id':
            return 123456
        else:
            # raise AttributeError('you make no sense calling attr ', item, 'just change your attr')
            # 如果要只响应几个属性，对其他的要报错的话就在最后的else里面return换成raise，如果不需要报错的话变回return就行
            return 'just anything else , you are trying to get attr : ' + item



a = A('default desc')
print(a.desc)
a.desc = 'set desc'
print(a.desc)
print(len(a))
print(a)
for i in a:
    print(i)
# print(next(a))
# print(next(a))
# 直接调用next()也是可以的，不会调用__iter__函数
# 因此完全可以在__iter__里面返回一个毫不相干的generator，__next__里面定义自己的函数，两者完全分开也是可以的
print(a[6])
print(a['purelove'])
print(a[1:6])
print(a[5:2])
print(a[3:8:10])

print()
print(a.id)
print(a.func)
print(a.func('localh0st'))
f = a.func
print(f)
print(f.__name__)
test = lambda: 'test function test()'
print(test.__name__)
a.gunc('purelove')
print(a.gunc)
print(a.gunc('dfghj'))
print(a.gunc.__name__)
print(a.nonsense)

print('########### __getattr__的链式调用 ###############')


class Path(object):
    count = 0

    @log('__init__')
    def __init__(self, path='/'):
        Path.count += 1
        self.__path = path
        print(self)

    @log('__del__')
    def __del__(self):
        print('delete', str(id(self)))
        pass

    @log('__getattr__')
    def __getattr__(self, item):
        if isinstance(item, str):
            return Path(self.__path + item + '/')
        else:
            raise RuntimeError('path invalid')

    @log('__str__')
    def __str__(self):
        return 'Position at ' + str(id(self)) + '  Path : ' + self.__path

    __repr__ = __str__



# p1 = Path()
# p2 = p1.etc
# p3 = p2.passwd
# 分开写可以发现三个返回地址都不一样

# Path().etc.passwd
# 这样写却会发现第三个返回地址和第一个一样？？

# Path().A.B.C.D
# 发现一直在两个地址之间横跳
# 猜测可能是上一个对象销毁了导致那一块地址被重复利用

# 修改一下代码，添加 __del__
# 实验成功！说明就是这样！
# Path().etc.passwd

print(Path().etc.passwd)
print(Path.count)
# print一个对象和在类里面print self是同一个东西
# 能看出创建了三次不同的对象

print('############### 带参数的链式调用 #################')

class PathAdvanced(object):
    @log('__init__')
    def __init__(self,path = '/'):
        self.__path = path

    @log('__getattr__')
    def __getattr__(self, item):
        if isinstance(item, str):
            return PathAdvanced(self.__path + item + '/')
        else:
            raise RuntimeError('path invalid')

    @log('__call__')
    # def __call__(self, *args, **kwargs):      仅写支持传入一个参数的
    def __call__(self, arg):
        if isinstance(arg,str):
            return PathAdvanced(self.__path[:len(self.__path)-1] + ':' + arg + '/')
        else:
            raise RuntimeError('invalid arg')

    @log('__str__')
    def __str__(self):
        return 'Path : ' + self.__path


print(PathAdvanced().usr('PureLov3').bin.cat('testing success!').hhhhhhh)

# 通过callable()函数，我们可以判断一个对象是否是“可调用”对象。可以是函数，也可以是带有__call__()方法的对象