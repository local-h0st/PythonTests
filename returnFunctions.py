def func(times):    # 相当于是一个函数的打包生产机器
    def f(str='Pure'):
        for i in range(times):
            print(str)
        return 'Lov3'

    return f


function = func(5)

print(function)
res = function()
print(res)

#################################################################
# 返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。 #
#        要么在外面套一层函数，把可能变化的变量通过形参的形式固定下来       #
#################################################################


def createCounter(initialnum):
    ini = initialnum - 1

    def counter():  # 外部变量可以被保存下来
        nonlocal ini
        ini += 1
        # print(ini)
        return ini

    return counter


c = createCounter(2)

print(c(), c(), c())