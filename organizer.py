import os
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler

fileList = []

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            if not file[0] == '.':
                fileList.append(file)
                os.rename(os.path.join(path,file),os.path.join(path, '.' + file))
    return fileList

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        files(path)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    event_handler = MyHandler()
    event_handler2 = LoggingEventHandler()
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.schedule(event_handler2, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
