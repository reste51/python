from huey import RedisHuey, crontab

# huey = RedisHuey('my-app', host='redis.myapp.com')
huey = RedisHuey('app',host='localhost')


@huey.task()
def add_numbers(a, b):
    return a + b





if __name__ == '__main__':
    res = add_numbers()
    print(res())
