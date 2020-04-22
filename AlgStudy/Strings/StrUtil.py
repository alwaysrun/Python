# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 20:52:01 2020

@author: guodx
"""

def swapStr(ori:str)->str:
    return ' '.join(reversed(ori.split()))

def simplifyPath(path:str)->str:
    dirs = path.split('/')
    result = []
    for d in dirs:
        if not d or d=='.':
            continue
        if d=='..': # parent dir
            if result:
                result.pop()
        else:
            result.append(d)
            
    
    return '/' + '/'.join(result)

def restoreIP(ipstr:str)->list:
    result = []
    
    def getIP(ips:list):
        print(ips)
        result.append('.'.join(ips))
    
    def helper(ips:list, ipstr:str):
        if not ipstr:
            return
        
        print(ips, ipstr)
        if len(ips)==3: # ipstr only contain the last part
            if len(ipstr)>1 and ipstr[0]=='0':  # error: zero can only as a seprate part
                return
            ipnum = int(ipstr)
            if ipnum<256:
                ips.append(ipstr)
                getIP(ips)
                ips.pop()
            return
        
        # recursion
        if ipstr[0] == '0':
            ips.append('0')
            helper(ips, ipstr[1:])
            ips.pop()
            return
        
        size = min(3, len(ipstr))
        for i in range(1,size+1):
            ipnum = int(ipstr[:i])
            if(ipnum<256):
                ips.append(ipstr[:i])
                helper(ips, ipstr[i:])
                ips.pop()
            
    helper([], ipstr)
    return result            
            
            
            


if __name__=="__main__":        
#    fun = swapStr
#    print(swapStr('the sky is blue'))
#    print(swapStr('a good   example'))
#    print(swapStr('  hello world!  '))
    
#    fun = simplifyPath
#    print(fun('/home/'), '<=>', '/home')
#    print(fun('/../.././../'), '<=>', '/')
#    print(fun('/home//foo/'), '<=>', '/home/foo')
#    print(fun('/a/../../b/../c//.//'), '<=>', '/c')
#    print(fun('/a//b////c/d//././/..'), '<=>', '/a/b/c')
    
    fun = restoreIP
    print(fun('12345'))