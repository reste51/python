def foo():
    print('i am foo func ')

def decorator(func):
    print('this is a decorator func!')
    return func


# manually decorate
# foo = decorator(foo)
# foo()

@decorator
def bar():
    print('this is a bar func')

bar()


print('$'*100)

def hello(fn):
    # def wrapper():
    #     print( 'hello, %s ' % fn.__name__)
    #     fn()
    #     print( 'bye, %s ' % fn.__name__)
    print( 'bye, %s ' % fn.__name__)
    return fn

@hello
def foo():
    print(' i am foo')

foo()





