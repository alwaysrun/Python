# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 13:32:09 2020

@author: guodx
"""

def getThreeSum(ary:list)->list:
    
    def nextIndex(low:int, high:int)->int:
        index = low+1
        while (index<high) and (ary[low]==ary[index]):
            index += 1
        return index
      
    def preIndex(low:int, high:int)->int:
        index = high-1
        while (low<index) and (ary[high]==ary[index]):
            index -= 1 
        return index     
    
    result = []    
    ary.sort()
    print(ary)
    end = len(ary)-1
    for i in range(len(ary)-2):
        if (i>0) and (ary[i]==ary[i-1]):
            continue
        
        diff = 0-ary[i]
        low = i+1
        high = end
        while low<high:
            tmp = ary[low] + ary[high]
            if(tmp == diff):
                three = [ary[i], ary[low], ary[high]]
                result.append(three)
                low = nextIndex(low, high)
                high = preIndex(low, high)
            elif tmp < diff:
                low = nextIndex(low, high)
            else: # tmp > diff
                high = preIndex(low, high)
                
    return result            
            


if __name__=="__main__":    
    fun = getThreeSum
    print(fun([-1, 0, 1, 2, 2, 1, -1, -4]))