import gevent
import random


def task(pid):
    gevent.sleep(random.randint(0,2))
    print('Task', pid, 'done')


def sync():
    for i in range(10):
        task(i)


def async():
    threads = [gevent.spawn(task, i) for i in range(10)]
    gevent.joinall(threads)


print('sync')
sync()


print('async')
async()
