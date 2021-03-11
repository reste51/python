"""
    大O记法 - 时间复杂度

    注: python的指数计算是 ** ; 而不是 ^

    枚举法： 一个个数值去试。。  原始方法
    T(n) = k* g(n) +b
    T(n) = g(n)
    可以说 g(n) 是 T(n)的一个渐近函数； 大O表示法
"""
import time


# 例题: a + b + c = 1000; 且 a^2 + b^2 = c^2; 求出 a,b,c的组合？
def first():
    """
    for 三次 1000 -> 1000^3 * 10 -> 1000^3
    耗时时间：81.922998 秒 - 消耗资源过大，风扇转的快
    :return:
    """
    for a in range(1, 1001):
        for b in range(1, 1001):
            for c in range(1, 1001):
                if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                    print('符合条件的a: %d, b: %d, c: %d' % (a, b, c))


def optimize_t():
    """
    for 二次 1000 -> 1000^2 * 10 -> 1000^2
    耗时时间：0.939353 秒
    :return:
    """
    for a in range(1, 1001):
        for b in range(1, 1001):
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                print('符合条件的a: %d, b: %d, c: %d' % (a, b, c))


if __name__ == '__main__':
    start_seconds = time.time()
    # optimize_t()
    first()
    end_seconds = time.time()
    print('耗时时间：%f 秒' % (end_seconds - start_seconds))
