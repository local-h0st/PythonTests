from types import MethodType

print('########## 给实例绑定方法 ##########')
class Base(object):
    pass


base = Base()
base.name = 'Base class'


def changeName(self, newname):
    self.name = newname


base.changeInstanceName = MethodType(changeName, base)

print(base.name)
base.changeInstanceName('Base class name changed')
print(base.name)
print(base.changeInstanceName)  # <bound method changeName of <__main__.Base object at 0x000001F8C82A1FD0>>

print('########### 给类绑定方法 #############')

base2 = Base()
# print(base2.name)   failed
# base2.changeInstanceName('new base2')    failed
# 说明后期绑定的仅对那个实例有效，而不是对类有效，太灵活了
# 解决办法：对class绑定方法

Base.name = 'Default'


def f(self, s):
    self.name = s   # 这是设置一个新的实例属性name，不是修改Base.name

def g(self,s):
    Base.name = s


Base.func = f
Base.func2 = g

print(base2.name)
base2.func('Fake Base name setted')
print(base2.name)
print(Base.name)

base2.func2('Base name changed')
print(Base.name)

print('############# __slots__ ##############')

class Base2(object):
    __slots__ = 'name'
    pass


t = Base2()

t.name = 'ttttt'
print(t.name)
Base2.name = 'Base 2'
print(t.name)

# __slots__ 差不多就是对类里面的成员变量声明的意思，不用__slots__完全可以，但是用了比较规范