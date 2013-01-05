import threading
import time as _time

def start_bottle_server(app, port):
    server_thread = ServerThread(app, port)
    server_thread.daemon = True
    server_thread.start()
    _time.sleep(0.1)

class ServerThread(threading.Thread):
    def __init__(self, app, port):
        threading.Thread.__init__(self)
        self.app = app
        self.port = port
    
    def run(self):
        self.app.run(host='localhost', port=self.port)

# http://code.activestate.com/recipes/106033-deep-list-to-convert-a-nested-tuple-of-tuples/
def listit(t):
    return list(map(listit, t)) if isinstance(t, (list, tuple)) else t
