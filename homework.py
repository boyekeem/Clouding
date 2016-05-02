import threading

class Kayode(threading.Thread):
    def run(self):
        for _ in range(120):
            print(threading.currentThread().getName())
a=Kayode(name='first chat\n')
b=Kayode(name='second chatt\n')

a.start()
b.start()