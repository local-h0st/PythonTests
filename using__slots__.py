from types import MethodType


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

base2 = Base()
# print(base2.name)   failed
# base2.changeInstanceName('new base2')    failed
# 说明后期绑定的仅对那个实例有效，而不是对类有效，太灵活了
# 解决办法：对class绑定方法

Base.name = 'Default'


def f(self, s):
    self.name = s


Base.func = f

print(base2.name)
base2.func('Base name setted')
print(base2.name)