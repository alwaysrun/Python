# -*- coding: utf-8 -*-
'''
@Description: bubble sort[best(has sorted) O(n), worst O(n^2)]
    sorted from small to large
    Each time, the smallest elements 'bubble' to the head [i..len-1]
    Once all elements sorted(no exchange in a while), breaked.
@Author: guodxu@qq.com
'''

def BubbleSort(ary:list) -> list:
    if len(ary)<2:  # only 0 or 1 elment, its must sorted.
        return ary
    
    for i in range(0, len(ary)-1):
        isSorted=True
        for j in range(len(ary)-1, i, -1):  # Set the smallest ele to first
            if ary[j]<ary[j-1]:
                ary[j],ary[j-1]=ary[j-1],ary[j]
                isSorted = False
                
        if isSorted: # has sorted
            print(i, 'test: has sorted')
            break
        
    return ary

if __name__ == '__main__':
    import numpy as np
    import Test_sort as ts
    # err = (1,2,3)
    # ret = BubbleSort(err)
    for i in range(20):
        ary=np.random.randint(100, size=i)
        print(i, ':')
        print(ary)
        ts.CheckSorted(BubbleSort(ary))

