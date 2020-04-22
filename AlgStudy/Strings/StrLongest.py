# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 21:35:22 2020

@author: guodx
"""

def LongestSubStringList(strFull):
    subLen = 0
    subStr = []
    for s in strFull:
        try:
            i = subStr.index(s)
            subStr = subStr[i+1:]
            subStr.append(s)
        except ValueError:
            subStr.append(s)
            if subLen<len(subStr):
                subLen = len(subStr)
                
    return subLen

def LongestSubStringIndex(strFull:str)->int:
    if not strFull:
        return 0
    
    subLen = 1
    start = 0
    i = -1
    for cur in range(1, len(strFull)):
        i = strFull.find(strFull[cur], start, cur)
        if i == -1:
            count = cur-start+1
            if count>subLen:
                subLen = count
        else: #found
            start = i+1
        
    return subLen

def LongestSubStringDict(strFull:str)->int:
    if not strFull:
        return 0
    
    subLen = 1
    start = 0
    chIndex = {}
    for i in range(0, len(strFull)):
        ch = strFull[i]
        if (ch in chIndex) and (chIndex[ch]>=start):
            start = chIndex[ch]+1
        else:
            subLen = max(subLen, i-start+1)
            
        chIndex[ch] = i # set the character's index
        
    return subLen

def longestCommonPrefix(lstAll : [str])->str:
    if not lstAll:
        return ''
    if len(lstAll) == 1:
        return lstAll[0]
    
    size = min([len(s) for s in lstAll])    
    for i in range(size):
        pre = set()
        for s in lstAll:
            pre.add(s[i])
        if(len(pre)>1):
            return lstAll[0][:i]        
        
    return lstAll[0][:size] 

def longestCommonPrefixZip(lstAll : [str])->str:
    if not lstAll:
        return ''
    
    sub = []
    for s in zip(*lstAll):
        if len(set(s)) == 1: # All same
            sub += s[0]
        else:
            break
        
    return ''.join(sub)
        

if __name__=="__main__":
#    print(LongestSubStringDict("abcabcbb"))
#    print(LongestSubStringDict("bbbbbb"))
#    print(LongestSubStringDict("pwwkew"))
#    print(LongestSubStringDict("aaab"))
#    print(LongestSubStringDict("tmmzuxt"))
    
    print(longestCommonPrefix(["flower","flow","flight"]))
    print(longestCommonPrefix(["dog","racecar","car"]))
    print(longestCommonPrefix(["dog","dogOne","dog123"]))
    print(longestCommonPrefix(["flower","flow"]))
    
    