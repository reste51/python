"""
    变量也是一种OP, 再使用前需要进行初始化操作
"""
import tensorflow as tf

# 定义一个tensor常类
a = tf.constant([1, 2, 3, 4, 5, 6])

# 定义一个Var, trainable=True会随着训练过程(梯度下降)值会相应的改变
random_tensor = tf.random_normal([2, 3], mean=0.0, stddev=1.0)
var = tf.Variable(random_tensor, name='my-var')

# 初始化变量OP
init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    # 运行初始化变量
    sess.run(init_op)
    # 运行 变量后的tensor结果值
    print(sess.run(var))
    print(var.graph)

    # 将摘要写入 events 文件中, 在tensor-board显示
    # tensorboard --logdir=''
    fw = tf.summary.FileWriter('../events/tmp1/', graph=var.graph)



