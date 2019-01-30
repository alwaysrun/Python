# -*- coding: utf-8 -*-
'''
@Description: insertion sort(O(n^2))
    sorted from small to large
    Stable
    Insert each element[i] to the sorted-array[0..i-1];
    Efficent for samll data sets;
@Author: guodxu@qq.com
'''

def InsertionSort(ary:list) -> list:
    if len(ary)<2:  # only 0 or 1 elment, its must sorted.
        return ary
    
    for i in range(1, len(ary)):
        tmp=ary[i]
        # insert ary[i] into the sorted sequence[0..i]
        j=i-1
        while j>=0 and ary[j]>tmp:
            ary[j+1] = ary[j]
            j -= 1
        ary[j+1]=tmp
        
    return ary

if __name__ == '__main__':
    import numpy as np
    import Test_sort as ts
    # err = (1,2,3)
    # ret = InsertionSort(err)
    for i in range(20):
        ary=np.random.randint(100, size=i)
        print(i, ':')
        print(ary)
        ts.CheckSorted(InsertionSort(ary))