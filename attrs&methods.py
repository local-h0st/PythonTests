print(type('s'))
print(isinstance((1, 2), (list, tuple)))
print(dir('attrs and methods of str'))
print('###################')


class A():
    def __init__(self):
        self.time = '2022.4.7'
        self.__var = 'this is the private __var setted by __init__()'

    def __len__(self):
        print('calling self.__len__()')
        # return 'this is the return value of __len__ and it is not a int but a string'       failed , cannot return str
        return 999

    def f(self):
        print('calling self.f()')


a = A()
rst = len(a)
print(rst)
print('obj a hasattr time :', hasattr(a, 'time'))
print('get attr time :', getattr(a, 'time'))

print('setting a new attr description  ...')
setattr(a, 'description', 'attr description is setted using setattr()')
print('obj a hasattr description :', hasattr(a, 'description'))
print('get attr description :', getattr(a, 'description'))

print('setting a private attr __name  ...')
setattr(a, '__name', 'this is a private attr called __name')
print('obj a hasattr __name :', hasattr(a, '__name'))
print('get attr __name :', getattr(a, '__name'))

print(a.__name)
# print(a._A__name) failed
# print(a.__var)    failed
print(a._A__var)
# 这四行证明了即使通过setattr()也不能设置一个private变量，setattr()无论是否以__开头都是普通变量

print('obj a hasattr f :', hasattr(a, 'f'))
print('getting attr f :', getattr(a, 'f'))
fn = getattr(a, 'f')
fn()
a.f()

##################### class attrs #########################
print('###########################')


class B(object):
    name = 'class B'

    def __init__(self, n):
        self.objName = n


b = B('object b')
print(B.name)
print(b.name)
print(b.objName)
print(hasattr(b, 'name'))  # True
print(hasattr(B, 'name'))  # True
b.name = 'b name'  # 新增name属性与类属性同名，在访问b.name的时候会优先访问到实例name属性而不是类属性
print(b.name)
print(B.name)
del b.name
print(b.name)
print(B.name)

########################################
print('################################')


class C(object):
    count = 0

    def __init__(self):
        self.count += 1
        print(self.count)


c1 = C()
c2 = C()
c3 = C()

print('count of', C.__name__, C.count)


# class C 是错误示范，在__init__中的self.count不是修改类属性，而是新增一个实例属性，与类属性同名也叫count，并且初始化为0 执行++操作变成1
# 正确示范为：

class D():
    count = 0

    def __init__(self):
        D.count += 1
        print(self.count)  # 访问到的是类属性count 因为这个语句不是赋值语句，在实例属性中找不到count就去类属性里找count
        print(D.count)  # 正统写法


d1 = D()
d2 = D()
d3 = D()

print('count of d2.count', d2.count)
print('count of', D.__name__, D.count)

# 静态方法和类方法都要用装饰器修饰，实例方法是最常见和普遍的，魔术方法就涉及到反序列化了