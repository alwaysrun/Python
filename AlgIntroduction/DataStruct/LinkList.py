# -*- coding: utf-8 -*-
'''
Linked-List: use guard-node, when only guard-node is empty
'''

class NodeData:
    def __init__(self, value):
        self.prev=self.next=self
        self.value=value
        
class LinkListData:
    def __init__(self):
        self.__guard = NodeData(None)
        
    def Insert(self, node:NodeData):
        self.__guard.next.prev = node
        node.next = self.__guard.next
        node.prev = self.__guard
        self.__guard.next = node

    def Delete(self, node:NodeData):
        if node == self.__guard:
            raise(OverflowError("guard can not delete"))
            
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def IsEmpty(self):
        return self.__guard.prev == self.__guard # and self.__guard.next == self.__guard
    
    def Output(self):
        n = self.__guard.next
        print('List-Ele[ ', end='')
        while n != self.__guard:
            print(n.value, end=' ')
            n = n.next
        print(']')
            

    def Search(self, value):
        nd = self.__guard.next
        while nd != self.__guard:
            if nd.value == value:
                return nd
            nd = nd.next
            
        # not found
        raise(LookupError("Not found"))

if __name__ == '__main__':
    import random
    ld = LinkListData()
    tmp = []
    print('To insert')
    for _ in range(20):
        ele = random.randint(1, 100)
        tmp.append(ele)
        print(ele)
        ld.Insert(NodeData(ele))
    ld.Output()   
    
    print('To search and delete')
    i = 0
    while not ld.IsEmpty():
        n = ld.Search(tmp[i])
        ld.Delete(n)
        print(n.value)
        ld.Output()  
        i += 1
        
