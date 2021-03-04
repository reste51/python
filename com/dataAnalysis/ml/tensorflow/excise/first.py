"""
    tensorFlow 初步学习：
    角色： tensor: 张量， operation:操作, graph: 图，整体程序结构
           session: 可以运算程序的图

     图：,需要包含一组op和tensor， 分配一块内存。
         OP: 只要使用tensorflow的api定义的函数都是OP, tensor 指的是数据
         a = tf.constant(10)； a为OP, 10 为tensor

     Session:  run() -> 运行图的结构

"""
import tensorflow as tf

tf = tf.compat.v1

# 开启版本v1 兼容
tf.disable_eager_execution()

# a,b 为tensor 张量
a = tf.constant(10)
b = tf.constant(20)

# sum1 为operation
sum1 = tf.add(a, b)

aa = 100
# 操作符+重载为OP类型， 普通数值aa与OP操作, sum2 可以在run 中运行
sum2 = b + aa

# print(a, b, sum1)

# 创建一张新的图,需要包含一组op和tensor,与graph 不是同一块的内存
new_g = tf.Graph()
with new_g.as_default():  # 切换上下文，使用新建的图
    # 占位符 与 feed_dict 实时训练搭配使用. None代表不确定数量(样本数不确定)
    plt = tf.placeholder(tf.float32, shape=(None, 2))
    # c = tf.constant(11.0)
    # print(c.graph)
    with tf.Session() as s2:
        # 运行一个占位符，训练过程中才知道实际的数据
        ret = s2.run(plt, feed_dict={plt: [[1, 2], [3, 4], [5, 6], [5, 6]]})
        print(ret,plt)


print('*' * 100)

# 图默认已注册_ 为op 及 tensor 分配内存空间
graph = tf.get_default_graph()

# 开启会话，运行某一个个图
# with 开启session的上下文环境，结束后会默认调用 .close()函数
# log_device_placement -> 输出后端执行图的设备名称
with tf.compat.v1.Session(graph=graph,
                          config=tf.ConfigProto(log_device_placement=True)) as session:
    # 注: 错误: is not an element of this graph.  sum1是定义在 默认图中的
    # 不能运行c，因为c是定义在 new_g的图里; session运行的是graph图； 可以通过graph参数指定运行的图
    # run 说明运行图中的数据(多个使用 [] 传递), run 和eval 都需要有session的上下文环境;
    print(session.run([sum1, sum2]), sum1.eval())
    print(graph)
    # 获取 op / session/ tensor 所在的图, 输出的地址一致，因此他们所在的同一张图
    print(sum1.graph, session.graph, a.graph)







