import os
from pathlib import Path

import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler


fileList = []

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            if not file[0] == '.':
                fileList.append(file)
                os.rename(file, '.' + file)
    return fileList



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    files(path)
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
