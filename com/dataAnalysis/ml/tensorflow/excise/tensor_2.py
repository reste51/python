"""
张量的学习

    三维的理解： (2, 2,3) ： 2张  2行3列的表
"""
import tensorflow as tf

ph = tf.placeholder(tf.float32, shape=(None, 2))
# 因为shape中存在None, 静态shape； 修改原值.set_shape()
ph.set_shape((3, 2))
# print(ph.get_shape())

# 注： 如果shape确定后就不能再次set, 因为是 静态shape的api
# ph.set_shape((3,2,10))  # ValueError

# 动态shape, 生成一个新的tensor;
#  注：是tf.reshape()不是tensor对象的api,元素总数要一致
# -1 is inferred; [-1] flatten 1-D; [] to a scalar（0维数字）
ph = tf.reshape(ph, shape=(3, 2))

with tf.Session() as s:
    ret = s.run(ph, feed_dict={ph: [[1, 1], [2, 2], [3, 3]]})
    print(ret, ph.graph, s.graph, sep='\n')
