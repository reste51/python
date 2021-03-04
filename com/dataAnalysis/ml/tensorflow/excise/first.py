"""
    tensorFlow 初步学习：
    角色： tensor: 张量， operation:操作, graph: 图，整体程序结构
           session: 可以运算程序的图
"""
import tensorflow as tf

# 开启版本v1 兼容
tf.compat.v1.disable_eager_execution()

# a,b 为tensor 张量
a = tf.constant(10)
b = tf.constant(20)

# sum1 为operation
sum1 = tf.add(a,b)

# print(a, b,sum1)

# 开启会话，运行整个图; 兼容 .compat.v1.的版本；
# with 开启session的上下文环境，结束后会默认调用 .close()函数
with tf.compat.v1.Session() as session:
    print(session.run(sum1))



