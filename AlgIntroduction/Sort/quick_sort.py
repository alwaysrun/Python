# -*- coding: utf-8 -*-
import random
'''
@Description: quick sort(avg: O(nlgn), worst: O(n^2))
    sorted from small to large
    not statble
    Partition array to two party (smaller<=barrier, barrier, larger>=barrier),
    Repeat untill all partitioned.
@Author: guodxu@qq.com
'''

def toPartition(ary:list, nStart:int, nEnd:int)->int:
    nTmp=random.randint(nStart,nEnd)
    barrier=ary[nTmp]   # use a random element as barrier
    ary[nTmp]=ary[nEnd]
    nLittle=nStart-1
    for i in range(nStart, nEnd):   #[start, end-1]
        if ary[i]<barrier:  # move to left(nLittle+1)
            nLittle += 1
            if nLittle != i:
                ary[nLittle], ary[i] = ary[i], ary[nLittle]
                
    nLittle += 1
    ary[nEnd] = ary[nLittle]
    ary[nLittle] = barrier
    
    return nLittle

def toQuick(ary:list, nStart:int, nEnd:int):
    if nStart>= nEnd:
        return
    
    nMiddle = toPartition(ary, nStart, nEnd)
    toQuick(ary, nStart, nMiddle-1)
    toQuick(ary, nMiddle+1, nEnd)
    
def QuickSort(ary:list)->list:
    if len(ary)>1:
        toQuick(ary, 0, len(ary)-1)
        
    return ary

if __name__ == '__main__':
    import numpy as np
    import Test_sort as ts
    
    nFailed = 0
    for i in range(20):
        ary=np.random.randint(10000, size=i)
        # ary=[40, 98, 81, 80]
        print(i, ':', ary)
        newAry=QuickSort(ary.copy())
        if not ts.CompareAry(ary, newAry):
            nFailed += 1
        if not ts.CheckSorted(newAry):
            nFailed += 1
    print()
    if nFailed==0:
        print("Great, all check success!")
    else:
        print(nFailed, "check Failed!!!");
