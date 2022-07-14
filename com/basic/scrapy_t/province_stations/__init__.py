def handle():
    class myClass(object):
        def __init__(self):    #对各种基本数据类型测试
            self.x = []        #列表
            self.y = None         #数值
            self.z = {}        #字典
            self.a = str()     #字符串
            self._handle()


        def _handle(self):
            self.x.append('hello')
            self.y = 1
            self.z['hello'] = 'world'
            self.a = "".join("hello")


    my_class = myClass()

    return my_class.x, my_class.y, my_class.z, my_class.a
    pass
if __name__ == '__main__':
    my_x, my_y, my_z, my_a = handle()
    print( my_x, my_y, my_z, my_a)


