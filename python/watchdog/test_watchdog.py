"""test watchdog."""
import os
import time
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class SomeHandler(FileSystemEventHandler):
    def on_created(self, event):
        # ファイル作成時に呼ばれる。ファイルを開いた時にも呼ばれる。
        print("created")

    def on_modified(self, event):
        # ファイル更新時に呼ばれる。ファイル作成、ファイル消去の後にも呼ばれる。
        print("modified")

    def on_deleted(self, event):
        # ファイル消去時に呼ばれる。
        print("deleted")

if __name__ == "__main__":
    observer = Observer()
    # observer.daemon = True
    observer.schedule(SomeHandler(), BASEDIR, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
