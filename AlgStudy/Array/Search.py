# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 22:52:37 2020

@author: guodxu@qq.com
"""

def searchInShiftArray(ary:list, ele:int)->int:
    def bisearch(ary, start, end):
        if start>end:
            return -1
        mid = (start+end)//2
        if ary[mid] == ele:
            return mid
        
        if ary[mid]>ele:
            return bisearch(ary, start, mid-1)
        else: 
            return bisearch(ary, mid+1, end)
        
        
    def search(ary, start, end):
#        print(start, end)
        if start>end:
            return -1
        mid = (start+end)//2
        if ary[mid] == ele:
            return mid
        
        if ary[mid]<ele:            
            if ary[start]>ary[mid]: # mid在旋转点后，
                if ary[end]>=ele:
                    return bisearch(ary, mid+1, end)
                return search(ary, start, mid-1)
            # mid在旋转点前
            return search(ary, mid+1, end)
        else: # ary[mid]>ele
            if ary[start]>ary[mid]: # mid在旋转点后，
                return search(ary, start, mid-1)
            # mid在旋转点前
            if ary[start]<=ele:
                return bisearch(ary, start, mid-1)
            return search(ary, mid+1, end)
            
    return search(ary, 0, len(ary)-1)  

def findPivotPoint(ary:list)->tuple:
    if ary[0]<ary[len(ary)-1]:
        return (False, 0, ary[0])
    
    def findPoint(ary:list, start, end):
        if start == end:
            return start
        
        mid = (start+end)//2
        if ary[mid]>ary[end]:
            return findPoint(ary, mid+1, end)
        else: #
            if ary[mid]<ary[mid-1]:
                return mid
            else:
                return findPoint(ary, start, mid-1)
      
    index = findPoint(ary, 0, len(ary)-1)
    return (True, index, ary[index])

def longestIncrSeq(ary:list)->int:
    if not ary:
        return 0
    
    
    longest = 1
    cur = 1
    for i in range(1, len(ary)):
        if ary[i]>ary[i-1]:
            cur += 1
        else:
#            if cur > longest:
#                longest = cur
            longest = max(longest, cur)
            cur = 1
    longest = max(longest, cur)
#    if cur > longest:
#        longest = cur
            
    return longest
        

if __name__=="__main__": 
#    fun = searchInShiftArray
#    print(fun([4,5,6,7,0,1,2], 0))
#    print(fun([4,5,6,7,0,1,2], 1))
#    print(fun([4,5,6,7,0,1,2], 2))
#    print(fun([4,5,6,7,0,1,2], 3))
#    print(fun([4,5,6,7,0,1,2], 4))
#    print(fun([4,5,6,7,0,1,2], 5))
#    print(fun([4,5,6,7,0,1,2], 6))
#    print(fun([4,5,6,7,0,1,2], 7))
#    print(fun([4,5,6,7,0,1,2], 8))
    
#    fun = findPivotPoint
    fun = longestIncrSeq
    print(fun([4,5,6,7,0,1,2]))
    print(fun([4,5,6,7,0,2]))
    print(fun([4,5,6,7,0]))
    print(fun([4,5,0,1,2]))
    print(fun([5,0,1,2]))
    print(fun([0,1,2]))