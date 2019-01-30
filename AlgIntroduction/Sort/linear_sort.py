# -*- coding: utf-8 -*-
'''
@Description: counting sort(O(n+k), k is the range of sorted-data)
    sorted from small to large
    statble, not a comparison sort
    it is suitable for keys are small, it is often used as subroutine i other sort-alg.
    by counting the count of distinct-number, and use the count to determined the position of each key.
    Use more memory, not sort on ori-ary
    
    radix sort(O(n+k), k is the Number-digits of key)
@Author: guodxu@qq.com
'''

def CountingSort(ary:list)->list:
    if(len(ary)<2): return ary
    
    maxKey = max(ary)
    maxKey+=1   # maxKey must in the count-ary
    #import numpy as np
    #aryCount = np.zeros(maxKey, dtype=int)
    aryCount=[0 for _ in range(maxKey)]
    for i in range(len(ary)):
        aryCount[ary[i]] += 1
    for i in range(1,maxKey): # the count less than the pointed-key
        aryCount[i] += aryCount[i-1]
        
    sortedAry = [0 for _ in range(len(ary))]
    for i in range(len(ary)-1, -1, -1): # to reserver stable, from end to start
        sortedAry[aryCount[ary[i]]-1] = ary[i]
        aryCount[ary[i]] -= 1

    return sortedAry

class radix10Key:
    def __init__(self, ele):
        self.ele = ele
        self.div = 1
        self.key = None
# =============================================================================
#     def __repr__(self):
#         return "{}:{}".format(self.ele,self.key)
#     def __str__(self):
#         return "{}:{}".format(self.ele,self.key)
# =============================================================================
    def getKey(self):
        if self.key is None:
            self.key = self.ele // self.div % 10
        return self.key
    def getElement(self):
        return self.ele
    def resetDiv(self, div):
        self.div=div
        self.key=None
    
def radixSubInsertSort(ary:list):
    for i in range(1, len(ary)):
        tmp=ary[i]
        # insert ary[i] into the sorted sequence[0..i]
        j=i-1
        while j>=0 and ary[j].getKey()>tmp.getKey():
            ary[j+1] = ary[j]
            j -= 1
        ary[j+1]=tmp

def Radix10Sort(ary:list)->list:
    if(len(ary)<2): return ary
    
    radAry=[radix10Key(e) for e in ary]
    div=1
    maxEle = max(ary)
    while True:
        radixSubInsertSort(radAry)
        maxEle //= 10
        if maxEle<=0: break
    
        div *= 10
        # list(map(lambda e:e.resetDiv(div), radAry))
        [e.resetDiv(div) for e in radAry]
    
    return [i.getElement() for i in radAry]
    

if __name__ == '__main__':
    import numpy as np
    import Test_sort as ts
    
    nFailed = 0
    for i in range(20):
        ary=np.random.randint(10000, size=i)
        
        # ary=[91, 75, 42, 68, 6]
        print(i, ':', ary)
        # newAry=CountingSort(ary.copy())
        newAry=Radix10Sort(ary.copy())
        if not ts.CompareAry(ary, newAry):
            nFailed += 1
        if not ts.CheckSorted(newAry):
            nFailed += 1
    print()
    if nFailed==0:
        print("Great, all check success!")
    else:
        print(nFailed, "check Failed!!!");