import gevent
from gevent.event import AsyncResult


a = AsyncResult()


def setter():
    gevent.sleep(3)
    a.set('Hello')


def getter():
    print(a.get())


gevent.joinall([
    gevent.spawn(setter),
    gevent.spawn(getter),
])
