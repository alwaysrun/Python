# -*- coding: utf-8 -*-

class headData:
    def __init__(self):
        self.head = None
        self.tail = None
        
class nodeData:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class QueueData:
    def __init__(self):
        self.header = headData()
        
    def Enqueue(self, value):
        nd = nodeData(value)
        if self.header.tail: # not empty
            self.header.tail.next = nd
            self.header.tail = nd
        else: # is empty
            self.header.head = self.header.tail = nd
            
    def Dequeue(self):
        if not self.header.head: # is empty
            raise(LookupError('No more data'))
            
        nd = self.header.head
        if self.header.head == self.header.tail: #only one ele
            self.header.head = self.header.tail = None
        else:
            self.header.head = nd.next
            
        return nd.value
    
    def IsEmpty(self):
        return not self.header.head
    
if __name__ == '__main__':
    import random
    qd = QueueData()
    for _ in range(3):
        print("To enqueue")
        for i in range(20):
            ele = random.randint(1, 100)
            print(ele)
            qd.Enqueue(ele)
            
        print("To dequeue")
        while not qd.IsEmpty():
            print(qd.Dequeue())
        
        