# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 09:29:38 2020

@author: guodx
"""

import random

def findKthLargest(nums: list, k: int) -> int:
    
    def toPartition(nums:list, start:int, end:int)->int:
        if start==end:
            return start
        
        nTmp = random.randint(start, end)
        barrier = nums[nTmp]
        
        left = start
        right = end
        nums[nTmp] = nums[left]
        while left < right:
            while nums[right]<barrier and left<right:
                right -= 1
            nums[left] = nums[right]
            
            while nums[left]>=barrier and left<right:
                left += 1                
            nums[right] = nums[left]
              
        nums[left] = barrier
        return left
    
    def getKPartition(nums:list, start:int, end:int, k:int)->int: 
        if start>end:
            raise(Exception('start must less than end'))
            
        mid = toPartition(nums, start, end)
        nth = mid+1-start
        if nth == k:
            return nums[mid]
        
        if nth>k:
            return getKPartition(nums, start, mid-1, k)
        else:
            return getKPartition(nums, mid+1, end, k-nth)
        
        
    # get now
    return getKPartition(nums, 0, len(nums)-1, k)

if __name__=="__main__": 
    fun = findKthLargest
    print(fun([4,5,6,7,0,1,2], 1))
    print(fun([4,5,6,7,0,1,2], 2))
    print(fun([4,5,6,7,0,1,2], 3))
    print(fun([4,5,6,7,0,1,2], 4))
    print(fun([4,5,6,7,0,1,2], 5))
    print(fun([4,5,6,7,0,1,2], 6))
    print(fun([4,5,6,7,0,1,2], 7))