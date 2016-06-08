import threading

class Messanger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())


x = Messanger(name="Send out messages")
y = Messanger(name="Receive messages")
x.start()
y.start()