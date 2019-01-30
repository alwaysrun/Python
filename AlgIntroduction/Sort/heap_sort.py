# -*- coding: utf-8 -*-
'''
@Description: heap sort(O(nlgn))
    sorted from small to large
    not statble
    build a bitree, then the root is the largest.
    Exchange root with the least-leaf, and rebuild the bitree(count-1),
    Repeat, until the bitree only one element.
@Author: guodxu@qq.com
'''

def parentIndex(i:int):
    return int(i/2)
def leftIndex(i:int):
    return i*2
def rightIndex(i:int):
    return i*2+1

# =============================================================================
# make ary[i..size] is a largest bi-tree:
# the input ary[i..size] is almost a bi-tree,
# except the root all leaves is bi-tree,
# then get the largest to the root, and make the rest maintain bi-tree
# =============================================================================
def maxHeapify(ary:list, size:int, i:int):
    left=leftIndex(i)
    right=rightIndex(i)
    if left<size and ary[left]>ary[i]:
        largest=left
    else:
        largest=i
    
    if right<size and ary[right]>ary[largest]:
        largest=right
        
    if largest != i:
        ary[largest], ary[i] = ary[i], ary[largest]
        maxHeapify(ary, size, largest)

# =============================================================================
# build largest bi-tree(root/ary[0] is the largest):
# From the mid-element(len/2) to first-elemnt(ary[0]),
# make sure it larger than it's leaves(2*i and 2*i+1)
# =============================================================================
def buildMaxheap(ary:list):
    if(len(ary)<2):
        return
    start=int((len(ary)-1)/2)
    for i in range(start, -1, -1):
        maxHeapify(ary, len(ary), i)
        
def HeapSort(ary:list)->list:
    if(len(ary)<2):
        return ary
    
    buildMaxheap(ary)
    for i in range(len(ary)-1, 0, -1):
        ary[i], ary[0] = ary[0], ary[i]
        maxHeapify(ary, i, 0)
    
    return ary

if __name__ == '__main__':
    import numpy as np
    import Test_sort as ts
    
    nFailed = 0
    for i in range(20):
        #ary=[ 3, 16, 33, 13, 89,  3,  2, 55, 82, 41,  7, 20,  5, 35, 81]
        ary=np.random.randint(10000, size=i)
        print(i, ':', ary)
        if not ts.CheckSorted(HeapSort(ary)):
            nFailed += 1
    print()
    if nFailed==0:
        print("Great, all check success!")
    else:
        print(nFailed, "check Failed!!!");
