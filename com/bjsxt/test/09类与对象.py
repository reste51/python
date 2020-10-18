'''
类与对象
    1.__init__完成对象的初始操作，在对象被创建完成之后(__new__执行完毕),立刻被调用执行。
        隐式调用，创建对象时的 参数要跟init方法的参数保持一致
    2.__new__ 为构造方法，创建对象时，首先new ,必须要有返回值（创建的实例），参数必须跟创建对象传递的参数一致
    3.无论什么情况，init和new方法的参数都要保持一致

    1、__new__至少要有一个参数cls，代表要实例化的类，此参数在实例化时由Python解释器自动提供
    2、__new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，可以return父类__new__出来的实例，或者直接是object的__new__出来的实例
    3、__init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，__init__不需要返回值


'''

class Person(object):
    # self为初始化后的实例引用
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('init',name)
    # cls 为初始化的类
    def __new__(cls, *args, **kwargs):
        cls.name = '李勇' # 设置类属性的值
        cls.commonAttr = '通用属性值'
        # print('new_',args[0], args[1])
        return object.__new__(cls)

    slAttr = '实例属性'
    def run(self):
        print('实例方法: %s'%self.slAttr)


p = Person('力点',23)
print(p.name)

p2 = Person('利益',21)
print(p2.name,p2.age)

print('类属性值.', p.commonAttr, p2.commonAttr)
print('--'*100)

p.slAttr='p 更改值'
p.run()
p2.run()

