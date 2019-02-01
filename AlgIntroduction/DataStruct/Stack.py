# -*- coding: utf-8 -*-

class StackData:
    def __init__(self):
        self.__data = []
        
    def IsEmpty(self):
    # =============================================================================
    #         if self.__data:  # not empty
    #             return False
    #         else:
    #             return True
    # =============================================================================
        return not self.__data
    
    def Peek(self):
        if not self.__data:
            raise(LookupError('No more data'))
        return self.__data[len(self.__data)-1]
    
    def Size(self):
        return len(self.__data)
    
    def Push(self, item):
        self.__data.append(item)
        
    def Pop(self):
        if not self.__data:
            raise(OverflowError('No __data'))
        return self.__data.pop()

if __name__ == '__main__':
    import random
    sd = StackData()
    print("To push")
    for i in range(20):
        sd.Push(random.randint(1, 100))
        print(sd.Peek())
        
    print("To pop")
    while sd.Size():
        print(sd.Pop())

    try:
        sd.Pop()
    except Exception as err:
        print("Exception:", err)
