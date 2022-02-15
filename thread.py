import threading
import time

def thread_function (name):
    print (f'Thread {name} starting')
    time.sleep(1)
    print ('Pause')
    print (f'Thread {name} finished')


if __name__ =='__main__':
    th1 = threading.Thread(target=thread_function,args=('thread1',))
    
    print('Before starting')
    th1.start()
    
    print('After starting')