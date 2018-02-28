import gevent
from gevent import Greenlet


class MyGreenlet(Greenlet):
    def __init__(self, message, n):
        self.message = message
        self.n = n

    def _run(self):
        print(self.message)
        gevent.sleep(self.n)


g = MyGreenlet('Hi', 3)
g.start()
g.join()
