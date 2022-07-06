class A(object):
    def __init__(self, n):
        self.__name = n
        self.__id = 0

    @property  # 把一个get方法变成属性 read-only
    def id(self):
        print('print() in function() read-only')
        return self.__id

    @id.setter  # 如果不定义setter那这个属性就是read-only，定义setter是为了修改属性
    def id(self, new_id):
        if not isinstance(new_id, int):
            raise ValueError('not a int')
        else:
            print('print() in setter')
            self.__id = new_id


a = A('class A object named \'a\'')
# a.id = 'fgh'      failed
print(a.id)
a.id = 6
print(a.id)
# @property本质是把函数调用包装成属性读取和赋值的方式，其实质和函数调用没有区别
# 通过只定义@property来定义常量! 常量懂吗! property后面那个函数名才是常量!

# a.id(66)
# a.id()
# 这两句可以print出来，但是都会报错


# 别限定了思想!来看可变常量
print('###############################')


class B(object):
    def __init__(self, x):
        self.__x = x  # 初始化时设定值
        self.__y = 0

    @property
    def get_y(self):
        return self.__y

    @get_y.setter
    def set_y(self, new):
        if not isinstance(new, int):
            raise ValueError('Give me an int !')
        else:
            self.__y = new
            return 'done'  # 我拿不到返回值 唉应该是可以拿到的但是我不会

    @property
    def sum_of_xy(self):
        return self.__x + self.__y


b = B(6)
print(b.get_y)  # initial 0
print(b.sum_of_xy)      # 6 + 0
# b.sum_of_xy = 7       AttributeError: can't set attribute      meaning a const
b.set_y = 9
print(b.get_y)  # set 9
print(b.sum_of_xy)      # 6 + 9       meaning a changeable 'const' !!

# 要特别注意：属性的方法名不要和实例变量重名。会造成无限递归，导致栈溢出报错RecursionError
