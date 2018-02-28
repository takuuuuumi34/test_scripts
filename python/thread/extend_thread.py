import threading
import time


class MyThread(threading.Thread):
    def __init__(self, i):
        super(MyThread, self).__init__()
        self.i = i
        self.stop_event = threading.Event()
        self.setDaemon(True)

    def stop(self):
        self.stop_event.set()

    def run(self):
        print('START {}'.format(self.i))
        i = 0
        while not self.stop_event.is_set():
            print('I am no.{}'.format(self.i))
            time.sleep(self.i)
        print('END {}'.format(self.i))


if __name__ == '__main__':
    th1 = MyThread(1)
    th2 = MyThread(2)
    th1.start()
    th2.start()
    print(dir(th1))
    time.sleep(3)
    th1.stop()
    th2.stop()
