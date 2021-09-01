from  mxnet import autograd,nd


X = nd.arange(4).reshape((4,1))
print(X)

# 为了求有关变量x的梯度，我们需要先调用attach_grad函数来申请存储梯度所需要的内存。
X.attach_grad()

# 下面定义有关变量x的函数。为了减少计算和内存开销，
# 默认条件下MXNet不会记录用于求梯度的计算。我们需要调用record函数来要求MXNet记录与求梯度有关的计算。
with autograd.record():
    y = 2 * nd.dot(X.T, X)

# 由于x的形状为（4, 1），y是一个标量。接下来我们可以通过调用backward函数自动求梯度。
# 需要注意的是，如果y不是一个标量，MXNet将默认先对y中元素求和得到新的变量，再求该变量有关x的梯度。

print(y.backward())

assert (X.grad - 4 * X).norm().asscalar() == 0
print(X.grad)

