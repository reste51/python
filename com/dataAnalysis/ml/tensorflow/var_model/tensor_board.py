"""
    TensorBoard 学习
    显示图中的 组件_ tensorboard --help / --logdir = path  注: path没有引号
"""

import tensorflow as tf

constant_a = tf.constant([[1, 2, 3], [4, 5, 6]],dtype=tf.float32, name='constant_a')
constant_b = tf.constant([[1.0], [2.2], [3.1]], name='constant_a')
matmul_op = tf.matmul(constant_a,constant_b, name='matmul_op')

var_b = tf.Variable(tf.random_normal([2, 3], mean=0.0, stddev=1.0), name='var_b')

# 初始化变量的操作
init_op = tf.global_variables_initializer()

with tf.Session() as sess:

    sess.run(init_op)

    # 输出变量的值
    print(var_b.eval())
    print('*'*100)
    print(matmul_op.eval())

    # print(sess.run(var_b))
    # 写入事件， 需要指定 写入图对象
    fw = tf.summary.FileWriter(logdir='../events/tmp2/', graph=sess.graph)
    fw.close()
