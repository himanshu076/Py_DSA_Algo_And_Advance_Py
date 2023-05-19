
# *processing & multi-Processing - when we are acessicing multiple program in operating system that time we are using processing or multi-processing.

# *Thread & Multi-Threading - When we are accessing multiple method that is not connected/ interlink with each other that time seperately assign particular thread for each method in single program that assigned threading to every method is Multi-Threading.


# *Creating thread.
from threading import Thread, current_thread, Lock, RLock, Semaphore, BoundedSemaphore
from time import sleep

# def disp(a, b):
#     for i in range(5):
#         print("Publish Video C")

# t = Thread(target=disp)
# t.start()

# for i in range(5):
#     print("Publish Video M")

# *Set and Get Thread Name.
# current_thread will return onject of the thread.
# def disp():
#     print("Default child thread name:", current_thread().name)
#     current_thread().name = 'Doc thread'
#     print("New child thread name:", current_thread().name)


# t = Thread(target=disp)
# t.start()

# print("Default Main Thread Name:", current_thread().name)
# current_thread().name = 'GeekyShows Thread'
# print("Default Main Thread Name:", current_thread().name)

# *Creating a thread by creating child class to thread class.
# class MyThread(Thread):
#     pass

# t = MyThread()
# print(t.name)

# start() - Once thread is created it should be started by calling start()
# run() - Every thread will run this method by default & we can overwrite it it needed.
# join() - This method is used to wait till the thread completely executes the run() method.

# class MyThread(Thread):
#     def run(self):
#         for i in range(5):
#             print("Run Method")

# t = MyThread()
# t.start()
# t.join()
# # print(t.name)

# for i in range(5):
#     print("Main Thread")

# *Thread child calss with constructor\
# class MyThread(Thread):
#     def __init__(self, a):
#         Thread.__init__(self)
#         print("Child Thread Constructor", a)

#     def run(self):
#         pass

# t = MyThread(10)
# t.start()
# print("Main Thread")

# *Creating a Thread without creating child class to thread class.
# class MyThread:
#     def disp(self, a, b):
#             print(a,b)

# myt = MyThread()

# t = Thread(target=myt.disp, args=(10, 20))
# t.start()

# *Single Tasking using a Thread.
# class MyExam:
#     def Solve_question(self):
#         self.q1()
#         self.q2()
#         self.q3()

#     def q1(self):
#         print("Squestion 1 Solved")
#         sleep(3)
#     def q2(self):
#         print("Squestion 2 Solved")
#         sleep(3)
#     def q3(self):
#         print("Squestion 3 Solved")
#         sleep(3)

# mye = MyExam()
# t = Thread(target=mye.Solve_question)
# t.start()

# *Multitasking using Multiple Thread
# class Hotel:
#     def __init__(self, t) -> None:
#         self.t = t

#     def food(self):
#         for i in range(1,6):
#             print(self.t, i)

# h1 = Hotel("Take order from table")
# h2 = Hotel("Serve order to table")

# t1 = Thread(target=h1.food)
# t2 = Thread(target=h2.food)
# t1.start()
# t2.start()

# *Thread Race Condition in python
# class Flight:
#     def __init__(self, available_seat):
#         self.available_seat = available_seat

#     def reserve(self, need_seat):
#         print(f'Available Seats: {self.available_seat}')
#         if(self.available_seat >= need_seat):
#             name = current_thread().name
#             print(f'{need_seat} seat is alloted for {name}')
#             self.available_seat -= need_seat

#         else:
#             print('Sorry! All seats has alloted')

# f = Flight(1)
# t1 = Thread(target=f.reserve, args=(1,), name="Rahul")
# t2 = Thread(target=f.reserve, args=(1,), name="Rahul")
# t1.start()
# t2.start()

# *Thread Syncronization Lock
'''Thread Syncronization is used to overcome the race condition'''
'''There are following techniques to do Thread Syncronization:
1. Using Locks
2. Using RLock(Re-Entrant Lock)
3. Using Semaphores
'''

# 1. Locks - It has two method.
    # i. acquire() - This method is used to Lock the thread until given timeout.
    # ii. Release()- This method is used to release the Lock. This method is called from any thread, not only by acquired thread.

# class Flight:
#     def __init__(self, available_seat):
#         self.available_seat = available_seat
#         self.l = Lock()

#     def reserve(self, need_seat):
#         self.l.acquire()
#         print(f'Available Seats: {self.available_seat}')
#         if(self.available_seat >= need_seat):
#             name = current_thread().name
#             print(f'{need_seat} seat is alloted for {name}')
#             self.available_seat -= need_seat

#         else:
#             print('Sorry! All seats has alloted')
#         self.l.release()

# f = Flight(2)
# t1 = Thread(target=f.reserve, args=(1,), name="Rahul")
# t2 = Thread(target=f.reserve, args=(1,), name="Sonam")
# t3 = Thread(target=f.reserve, args=(1,), name="Raj")
# t1.start()
# t2.start()
# t3.start()
# t1.join()
# t2.join()
# t3.join()

# 2. RLocks(Re-Entrant Lock) - It has two method.
    # i. acquire() - This method is used to Lock the thread until given timeout.
    # ii. Release()- This method is used to release the Lock. This method is called from any thread, not only by acquired thread.

# class Flight:
#     def __init__(self, available_seat):
#         self.available_seat = available_seat
#         self.l = RLock()
#         print(self.l)

#     def reserve(self, need_seat):
#         self.l.acquire()
#         print(self.l)
#         print(f'Available Seats: {self.available_seat}')
#         if(self.available_seat >= need_seat):
#             name = current_thread().name
#             print(f'{need_seat} seat is alloted for {name}')
#             self.available_seat -= need_seat

#         else:
#             print('Sorry! All seats has alloted')
#         self.l.release()

# f = Flight(2)
# t1 = Thread(target=f.reserve, args=(1,), name="Rahul")
# t2 = Thread(target=f.reserve, args=(1,), name="Sonam")
# t3 = Thread(target=f.reserve, args=(1,), name="Raj")
# t1.start()
# t2.start()
# t3.start()
# t1.join()
# t2.join()
# t3.join()


# 3. RLocks(Re-Entrant Lock) - It has two method.
    # i. acquire() - This method is used to Lock the thread until given timeout.
    # ii. Release()- This method is used to release the Lock. This method is called from any thread, not only by acquired thread.

class Flight:
    def __init__(self, available_seat):
        self.available_seat = available_seat
        self.l = BoundedSemaphore(2)
        print(self.l)

    def reserve(self, need_seat):
        self.l.acquire()
        print(self.l._value)
        print(f'Available Seats: {self.available_seat}')
        if(self.available_seat >= need_seat):
            name = current_thread().name
            print(f'{need_seat} seat is alloted for {name}')
            self.available_seat -= need_seat

        else:
            print('Sorry! All seats has alloted')
        self.l.release()

f = Flight(2)
t1 = Thread(target=f.reserve, args=(1,), name="Rahul")
t2 = Thread(target=f.reserve, args=(1,), name="Sonam")
t3 = Thread(target=f.reserve, args=(1,), name="Raj")
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()