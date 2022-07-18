import multiprocessing
import time
import counter_backup
import sustractor
  
  
class Process(multiprocessing.Process):
    def __init__(self, id):
        super(Process, self).__init__()
        print("I'm the process with id: {}"+"sustractor")
        sustractor
                 
    def run(self):
        time.sleep(1)
        counter_backup
        #print("I'm the process with id: {}".format(self.id))
        print("I'm the process with id: {}"+"counter")
  
if __name__ == '__main__':
    p = Process(0)
    p.start()
    p.join()
    p = Process(1)
    p.start()
    p.join()