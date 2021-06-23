import os
import threading

class MyThread(threading.Thread):
    def run(self):
        os.system("/prp/PRP.sh")
        pass

thread = MyThread()
thread.daemon = True
thread.start()