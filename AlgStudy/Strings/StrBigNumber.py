# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 22:39:22 2020

@author: guodx
"""

def bigNumberMulti(first:str, second:str)->str:
    result = [0 for _ in range(len(first)+len(second))]
    intFirst = [ord(ch)-ord('0') for ch in reversed(first)]
    intSecond = [ord(ch)-ord('0') for ch in reversed(second)]
    for i in range(len(intFirst)):
        for j in range(len(intSecond)):
            result[i+j] += intFirst[i]*intSecond[j]
            
    for i in range(len(result)-1):
        if result[i]<10:
            continue
        result[i+1] += result[i]//10
        result[i] = result[i]%10
        
    result.reverse()
    index = len(result)-1
    for i in range(len(result)):
        if result[i] != 0:
            index = i
            break
    print(result, index)
    strRes = [chr(n+ord('0')) for n in result[index:]]
    return ''.join(strRes)


if __name__=="__main__":
#    fun = bigNumberMulti
#    print(fun('0', '0'), 0*0)
#    print(fun('100006', '10006'), 100006*10006)
#    print(fun('123456789', '456123'), 123456789*456123)
#    print(fun('999999', '9999'), 999999*9999)
