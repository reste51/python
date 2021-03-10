"""
    自己实现一个线性回归的模型
    1.准备特征值和目标值
        100个特征值 [100,1]; y = 0.7*x + 0.8
    2.建立模型_随机初始化一个权重w 和 偏置b
        y_predict = w* x + b
    3.求损失值_均方误差(最小二乘法)
        (y_p-y)^2 + .....+(y_pn-y_n)^2  /  100 (样本数)
    4.使用梯度下降的方式_训练weight和bias的目标参数值
        指定学习率，训练 Variable：w 和 b

    梯度爆炸： 指 学习率过大(一般在 0.1 -1之间， 大于1可能出现)， 数值会成 指数成长;  ^2  ^6  ^8

    使用变量的作用域(返回的是context-manager 使用with)，会使 在tensorboard中更加清晰

"""
import tensorflow as tf

# 1.准备特征和目标值;
with tf.variable_scope('prepare_f_t_data'):
    X_op = tf.random_normal((100, 1), mean=1.75, stddev=1.0, name='x_data')
    y_true = tf.matmul(X_op, [[0.7]]) + 0.8  # 假设真实的w=0.7, b=0.8

# 2.建立线性回归模型， 1个特征， 1个权重，1个偏置 y = wx+b
# 随机给一个权重和偏置的值，让他计算损失， 然后再当前状态下优化 w和b(均是Variable类型的)
with tf.variable_scope('model'):
    random_w = tf.random_normal((1, 1), mean=2, stddev=0.2)
    weight_v = tf.Variable(random_w, dtype=tf.float32, name='weight')
    bias_v = tf.Variable(0.0, dtype=tf.float32, name='bias')
    y_predict = tf.matmul(X_op, weight_v) + bias_v

# 3.求损失值  (y_p-y)^2 + .....+(y_pn-y_n)^2  /  100
with tf.variable_scope('loss'):
    square = tf.square(y_predict - y_true)
    loss = tf.reduce_mean(tf.square(y_predict - y_true))

# 4.梯度下降优化损失值(也就是 优化 w和b)
# 学习率一般在 0.1 -1之间， 大于1则容易造成梯度爆炸(数据过大超过精度)
with tf.variable_scope('gradient_optimizer'):
    gradient = tf.train.GradientDescentOptimizer(learning_rate=0.1)
    g_op = gradient.minimize(loss, var_list=[weight_v, bias_v])

init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run([init_op])
    print(f'初始化值: weight={weight_v.eval()}, bias={bias_v.eval()}')
    # 重复训练_ 300次_ 已经贴合原值 0.7 / 0.8
    for i in range(300):
        sess.run(g_op)
        print(f'第{i+1}次优化: weight={weight_v.eval()}, bias={bias_v.eval()}')

    tf.summary.FileWriter(graph=sess.graph,logdir='../events/regression')
