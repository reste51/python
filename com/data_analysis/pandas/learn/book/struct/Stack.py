''''
 模拟栈结构, LIFO( last in first out, 后进先出)， 类似放在桌子上的书, a -> b ->c , 先取得也是 c ->b ->a ; 可以模拟浏览器 回退过程，也就是出栈.
 使用 list来模拟，尾部是 栈的顶端
'''

class Stack:
    # 初始化示例属性 items为一个list
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items ==[]

    # 添加到列表的尾部
    def push(self,item):
        self.items.append(item)

    # 出栈, 返回 尾部的第一个元素
    def pop(self):
        return self.items.pop()

    # 查看尾部的 一个元素, 不做任何操作
    def peek(self):
        return self.items[len(self.items)-1]

    # 返回栈内的元素个数
    def size(self):
        return len(self.items)



s = Stack()
s.isEmpty()

s.push(4)
s.push('Dog')

print(s.peek(), s.isEmpty())  # Dog

s.push(8.4)
print(s.pop())
