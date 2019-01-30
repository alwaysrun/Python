# -*- coding: utf-8 -*-
import random
'''
@Description: Select the i-min ele(avg: O(n) )
    Partition array to two party (smaller<=barrier, barrier, larger>=barrier),
    Repeat untill i'th element partitioned.
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

def randomSelect(ary:list, nStart:int, nEnd:int, i:int)->int:
    if nStart == nEnd:
        return ary[nStart]
    
    mid = toPartition(ary, nStart, nEnd)
    offset = mid-nStart+1
    if offset == i: # it is the answer
        return ary[mid]
    elif i<offset:
        return randomSelect(ary, nStart, mid-1, i)
    else:
        return randomSelect(ary, mid+1, nEnd, i-offset)
    
def SelectI(ary:list, i:int)->int:
    if i>len(ary) or i<=0:
        raise(Exception('Invalid i: i must less or equal ary-len and large than zero'))
    if len(ary) == 1:
        return ary[0]
    return randomSelect(ary, 0, len(ary)-1, i)
    
if __name__ == '__main__':
    import numpy as np
    import Test_seq as ts
    
    nFailed = 0
    for i in range(1,20):
        ary=np.random.randint(100, size=i)
        sel = random.randint(1,i)
        print('{}: {}->{}'.format(i, sel, SelectI(ary, sel)))
        print(ary)
        if not ts.CheckSeqI(ary, sel):
            nFailed += 1
            
    print()
    if nFailed==0:
        print("Great, all check success!")
    else:
        print(nFailed, "check Failed!!!");

