import time
import redis
from flask import Flask
import setuptools
from distutils.core import setup
import  foo

app = Flask(__name__)
cache = redis.Redis(host='192.168.136.131', port=6379)


def get_hit_count():
    """
    当redis启动时 或在 集群中节点间短暂的中断 很有作用， 使app 更加有resilient（弹性）
    :return:
    """
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as ex:
            if retries ==0:
                raise ex
            retries -=1
            time.sleep(0.5)


@app.route('/hello')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)


if __name__ == '__main__':
    app.run(debug=True, port=9999)


