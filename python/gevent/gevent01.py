import gevent


def foo():
    print('foo')
    gevent.sleep(1)
    print('foo end')


def bar():
    print('bar')
    gevent.sleep(1)
    print('bar end')


gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar)
])
