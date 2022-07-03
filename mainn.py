f = lambda x=3: 'purelov' + str(x)
print(f(1))


#####################################

def rtnlam(int, strr):
    return lambda i=int, s=strr: '[' + str(i) + '] ' + s


g = rtnlam(1, 'purelove')
print(g(2, 'dfghj'))
print(g())
