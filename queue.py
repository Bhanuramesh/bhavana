import sys
from array import *
queue=array('i',[])
def enqueue():
    element=int(input("enter the elements:"))
    queue.append(element)
    print("element is added to queue")
def dequeue():
    if not queue:
        print("queue is empty")
    else:
        e=queue.pop(0)
        print("removed element is",e)
def display():
    print("the element in queue is")
    for i in queue:
        print(i)
while True:
    print("select the operation 1.add 2.remove 3.show 4.quit")
    choice=int(input("enter your choice:"))
    if choice==1:
       enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break;
    else:
        print("enter correct operation")