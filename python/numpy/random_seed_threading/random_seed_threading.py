import threading
import time
import numpy as np


class TestThreading(threading.Thread):
    def __init__(self, name, seed):
        super(TestThreading, self).__init__()
        self.name = name
        self.seed = seed
        np.random.seed(self.seed)

    def run(self):
        for i in range(10):
            print("thread: {}, i: {}, rand: {}".format(self.name, i, np.random.rand()))
            time.sleep(1)


if __name__ == "__main__":
    # 同じ乱数値が出力される
    th1 = TestThreading("th1", 0)
    th1.start()
    th1.join()

    th2 = TestThreading("th2", 0)
    th2.start()
    th2.join()

    # スレッド間でseed値が共有されていることがわかる
    th1 = TestThreading("th1", 0)
    th2 = TestThreading("th2", 0)

    th1.start()
    th2.start()

    th1.join()
    th2.join()
