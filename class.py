################################ 最开始我自己写的实验版本 ####################################
print('####### Start ########')


class AA(object):
    def __init__(self, description_str):
        self.__description = description_str

    def printDes(self):
        print(self.__description)


a = AA('this is an instance of class AA')

# print(a.__description) 不可访问
a.printDes()
print(a._AA__description)
a._AA__description = 'purelove'  # 直接修改private变量
a.printDes()
print(a._AA__description)
# __开头的变量是private，不能通过外部访问，但是Python对__开头的变量只是做了一个重命名的处理，命名成了_classname__varname
# 因此外部可以通过访问_classname__varname直接修改private变量
# 避免通过这种方式来访问和修改__private变量

a.__name = 'Me'     # 貌似这样不能创建一个private变量
print(a.__name)     # 可以访问，Pycharm只会不停提示让我在class AA的__init__里面添加self.__name = None
# 廖雪峰的教程里面提到:如果在class里面设置了__name被自动修改成了_classname__name,类外再定义的a.__name的__name和class里面的private的__name不是同一个东西!
# 只要在外面设置的变量都是public?反正只是一个普通的成员变量而已

############################# Pycharm 魔改版本 #################################
print('############################')


class A(object):
    def __init__(self, description_str):
        self._A__description = None     # 这是Pycharm自己加的，删掉也不影响
        self.__description = description_str

    def printDes(self):
        print(self.__description)

    @property                           # 这也是Pycharm自己加的
    def A__description(self):           # 这也是Pycharm自己加的
        return self._A__description     # 这也是Pycharm自己加的


a = A('this is an instance of class A')
a.printDes()
print(a.A__description)                 # 这写法没见过啊
a._A__description = 'purelove'  # 直接修改private变量
a.printDes()

##########################################################################
print('##############################')


class B(object):
    def __init__(self,s):
        self.__des = s

    def createPrivateVar(self):
        self.__var = 'This is private __var'


b = B('des')

print(b._B__des)
# print(b._B__var) 报错，说明执行createPrivateVar()前不存在private变量__var
b.createPrivateVar()
print(b._B__var)
# print(b.__var)  报错，说明是private
# 以上测试说明Python允许在非__init__函数里面增添private变量，尽管最好还是先在__init__函数里面set None比较好