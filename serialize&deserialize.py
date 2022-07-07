import functools
import json
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
    # @log('init')
    def __init__(self, s):
        self.__name = s

    def sayHello(self):
        print('Hello', self.__name)


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
print('ccopy_reg\n_reconstructor\np0\n(c__main__\nMe\np1\nc__builtin__\nobject\np2\nNtp3\nRp4\n(dp5\nV_Me__name\np6\nVPureLov3\np7\nsb.')

print(pickle.dumps(123,protocol=0))
print(pickle.dumps('abc',protocol=0))
print(pickle.loads(pickle.dumps('abc',protocol=0)))









s = b'I16\n.'
s2 = b"(S'purelove'\nI16\nl."
print(pickle.loads(s2))