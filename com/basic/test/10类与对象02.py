'''
    私有属性和方法:
        在类内部声明：  __name 或 __getSalary() 则外部不能访问
        可以通过暴露共有方法 def getName(self): return self.__name 访问
    继承：
        子类调用父类方法：
            super().__init__();  super(子类,子类实例).__init();  父类.__init__()
        子类不能继承 父类私有方法

    两个方法的注解：
    @classmethod  def getName(cls): cls.name='类属性值'
    @staticmethod  def getName(): Person.name='类属性值'

    特殊方法, 由解释器隐式调用：
        __str__()	self	和toString
        __del__()	self	对象回收时候回调
        __new__()	cls	    对象创建的回调方法
        __init__()  self    已经创建了对象，初始化对象回调方法

'''

class Animal(object):
    __name ='私有类属性'
    def __init__(self,age):
        self.age =age

    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    @classmethod
    def getName(cls):
        return '类私有属性： '+ cls.__name

    @staticmethod
    def getClsType(self):
        return Animal.mro()


    # 类似java toString()
    def __str__(self):
        return 'Animal, age=%d, name=%s'%(self.age,self.__name)

    def __del__(self):
        print('销毁对象的操作.....%d'%self.age)


# 尝试访问私有类属性
a = Animal(300)
print(a.getName())
print(a.age)
print('-'*100)

# 特殊方法测试
print(a)

a = Animal(10)

# 类或静态方法
print(Animal.getName())

# print(Animal.getClsType(a))
print(Animal.getClsType())

