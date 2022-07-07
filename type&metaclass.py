# type()函数可以查看一个类型或变量的类型
class A(object):
    pass


a = A()
print(type(A))
print(type(a))
print(type(123))
print(type('abc'))

# type()也可以直接创建类，不通过class A(object)的方式
print('################')


def sayHello(self, s):
    print('hello', s)


H = type('Hello', (object,), dict(h=sayHello))

print(H.__name__)
print(H)
h = H()
print(h)
h.h('purelve')
print(h.h.__name__)
# 这个概念很简单、

print('########## metaclass ##########')
# metaclass生成class，class生成instance
