from threading import Thread

tong = 0

class MyThread(Thread):
    def __init__(self, _name, _begin, _end):
        super(MyThread,self).__init__()
        self.name = _name
        self.begin = _begin
        self.end = _end
    def run(self):
        global tong
        print("Bat dau chay %s" % ( self.name ))
        for i in range(int(self.begin), int(self.end)+1):
            tong+=i

if __name__ == "__main__":
    n = int(input("Nhap so nguyen duong n: "))
    thread1 = MyThread("thread1",0,n/2)
    thread2 = MyThread("thread2",n/2+1,n)
    try:
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()
        print("Tong la: %d" % ( tong ))
    except:
        print("Error!")