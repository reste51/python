'''
工厂模式：工厂模式是我们最常用的实例化对象模式了，是用工厂方法代替new操作的一种模式。
    分为 简单和抽象的工厂方式。


'''


class Axe(object):
    # def __init__(self,name):
    #     self.name = name
    # 砍树方法, 子类重写该方法
    def cur_tree(self):
        print('斧头开始砍树了')
        # print('%s开始砍树了。。。。'%self.name)

class StoneAxe(Axe):
    def cur_tree(self):
        print('石斧砍树了。。。。')

class SteelAxe(Axe):
    def cur_tree(self):
        print('钢斧砍树了。。。。')

class CopperAxe(Axe):
    def cur_tree(self):
        print('铜质砍树了。。。。')

class Person(object):
    def __init__(self,name):
        self.name = name

    def work(self,axeType):
        print('%s_开始工作了...'%self.name)
        # 使用特定斧头 砍树
        # axe = StoneAxe()
        # axe = SteelAxe()

        # 调用 工厂方法根据 axeType返回不同的实例
        axe = AxeFactory.createAxe(axeType)
        if(axe):
            axe.cur_tree()

class AxeFactory(object):
    # 根据axeType类型创建 不同的斧头实例并返回
    @staticmethod
    def createAxe(axeType):
        if(axeType=='stone'):
            return StoneAxe()
        elif(axeType=='steel'):
            return SteelAxe()
        elif(axeType=='copper'):
            return CopperAxe()
        else:
            print('传入参数出错！')

p = Person('原始人')
# p.work('stone')
# p.work('steel')
p.work('copper1')






