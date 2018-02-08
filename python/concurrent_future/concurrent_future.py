"""test."""
import concurrent.futures
import time


def echo_msg_after_time(msg, t):
    time.sleep(t)
    return msg


def thread_pool_executer():
    MSGS = ["hoge", "fuga", "piyo"]
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        a = {executor.submit(echo_msg_after_time, msg, 10): msg for msg in MSGS}
        for future in concurrent.futures.as_completed(a):
            print(future.result())


if __name__ == '__main__':
    thread_pool_executer()
