'''
单例模式：
1. 私有化 单例属性
2. __new__ 中判断

__new__ 调用后 会调用 __init__方法
'''

class Singleton(object):
    __instance = None
    __is_init = False

    def __init__(self,name):
        if(not self.__is_init):
            self.name=name
            self.__is_init = True
        print('--------init------')
        pass
    def __new__(cls, *args, **kwargs):
        print('--------new------')
        # 为空 则初始化操作
        if(not cls.__instance):
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def show(self):
        print('show: %s'%self.name)

s = Singleton('liyong')
# print(id(s))
s.show()

s1 = Singleton('张三')
# print(id(s1))
s1.show()
