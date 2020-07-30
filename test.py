# print("hello from PC")
# $ scp test.py root@192.168.0.240:/home/root/test.py

# test for multithreading
import threading
import time

class MyThread(threading.Thread):
  def __init__(self, num):
    threading.Thread.__init__(self)
    self.num = num

  def run(self):
    print("job start")
    time.sleep(self.num)
    print("job end")

t = MyThread(0.1)

t.start()

print("main start")
time.sleep(2)
print("main end")

# wait until job finished then continue
t.join()

print("all end")