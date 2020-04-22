# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 22:51:17 2020

@author: guodx
"""

def getAllRankRecursion(lstOri:list)->set:
    result = set()
    if not lstOri:
        return result
    
    def addResult(rank):
        get = ''.join(rank)
        result.add(get)
        print(get)
        
    def needSwap(rank, start, end)->bool:
        for i in range(start,end):
            if rank[i] == rank[end]:
                return False
        return True
            
    
    def helper(rank:list, start:int):
        if start==len(rank)-1:
            addResult(rank)
            return       
        
        helper(rank, start+1)
        for i in range(start+1, len(rank)):
            if(needSwap(rank, start, i)):
                rank[i], rank[start] = rank[start], rank[i]
                helper(rank, start+1)
                
                rank[i], rank[start] = rank[start], rank[i]
            
    helper(lstOri, 0)
    return result



def getAllRankWhile(rank:list)->set:
    def nextPermutation(rank:list)->bool:
        for i in range(len(rank)-1, 0, -1):
            if rank[i-1]<rank[i]:  # get the first Non-increase seq
                changed = i-1
                least = i
                for j in range(i+1, len(rank)):
                    if rank[changed]<rank[j] and rank[least]>=rank[j]:
                        least = j
                    
                # change the elements, and reverse
                rank[changed], rank[least] = rank[least], rank[changed]
                rank[i:] = rank[:i-1:-1]
                return True
            
        return False

    result = set()
    rank.sort()
    while True:
        get = ''.join(rank)
        print(get)
        result.add(get)
        
        if not nextPermutation(rank):
            break;
            
    return result
 
def getAllCombineRecursion(rank:list)->set:
    result = set()
    
    def getCom(com:list):        
        get = ''.join(com)
        print((get if get else '""'))
        result.add(get)
        
    def helper(rank:list, com:list):
        if not rank:            
            getCom(com)
            return
        
        com.append(rank[0])
        helper(rank[1:], com)
        
#        com.remove(rank[0])
        com.pop()
        helper(rank[1:], com)
        
        
    helper(rank, [])        
    return result
            

def getAllCombineBits(rank:list)->set:
    result = set()
    
    def getCom(com:list):        
        get = ''.join(com)
        print((get if get else '""'))
        result.add(get)
        
    for i in range(1, pow(2,len(rank))):
        com = []
        index = 0
        while i:
            if i&1:
                com.append(rank[index])
            i >>= 1
            index += 1
        getCom(com)
    
    return result

def getMCombine(rank:list, m:int)->set:
    result = set()
    
    def getCom(com:list):        
        get = ''.join(com)
        print((get if get else '""'))
        result.add(get)
        
    def helper(rank:list, count:int, com:list):
        if count==0:         
            getCom(com)
            return
        if not rank:   
            print('List empty: not enough char: ', count)
            return
        if count>len(rank):
            print('not enough char: ', count, len(rank))
            return
        
        com.append(rank[0])
        helper(rank[1:], count-1, com)
        
#        com.remove(rank[0])
        com.pop()
        helper(rank[1:], count, com)
        
        
    helper(rank, m, [])        
    return result

# first中不存在重复元素的情况，使用集合
def isContainRankSet(first:list, second:list)->bool:
    if len(first)>len(second): return False
    
    setFirst = set(first)    
    found = []
    for i in range(len(second)):
        if second[i] in setFirst:
            found.append(second[i])
            if len(found) == len(setFirst):
                setFound = set(found)
                if setFound == setFirst:
                    return True
                else: # remove the first
                    found = found[1:]
        else: # not in first
            found.clear()
            
    return False

# first中存在重复元素时，使用字典
def isContainRankMap(first:list, second:list)->bool:
    if len(first)>len(second): return False
    
    def buildDict(rank:list)->dict:
        con = {}
        for ele in rank:
            if ele in con:
                con[ele] += 1
            else:
                con[ele] = 1
        return con
        
    dFirst = buildDict(first)
    found = []
    for i in range(len(second)):
        if second[i] in dFirst:
            found.append(second[i])
            if len(found) == len(first):
                dFound = buildDict(found)
                if dFound == dFirst:
                    return True
                else: # remove the first
                    found = found[1:]
        else: # not in first
            found.clear()
            
    return False

if __name__=="__main__":
#    fun = getAllCombineBits
    fun = getAllCombineRecursion
    print(fun(['2', '1']))
    print()
    print(fun(['1','2','2']))
    print()
    print(fun(['1','2','3']))
    
#    fun = isContainRankSet
#    fun = isContainRankMap
#    print(fun([1,2], [2,3,4,5,6,4,3,2,1,3]))
#    print(fun([1,2,1], [2,3,4,5,6,4,3,2,1,3]))
#    print(fun([1,2], [2,3,4,5,6,4,3,1,3]))
#    print(fun(list('ab'), list('eidbaooo')))
#    print(fun(list('aba'), list('eidbaooo')))
#    print(fun(list('ab'), list('eidboaoo')))
    
#    fun = getMCombine
#    print(fun(['2', '1'], 1))
#    print()
#    print(fun(['1','2','2'], 2))
#    print()
#    print(fun(['1','2','3'], 2))