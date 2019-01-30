# -*- coding: utf-8 -*-

def CheckSorted(ary:list):
    print(ary, end=' -> ')
    
    if(len(ary)<2):
        print("Sorted")
        return True
    
    for i in range(len(ary)-1):
        if ary[i]>ary[i+1]:
            print(i, "th Element", ary[i], "not sorted!!!")
            return False;
            
    print("Sorted")
    return True

def CompareAry(ori:list, ary:list)->bool:
    if len(ori) != len(ary):
        print("Len diff: ori->", len(ori), ", new->", len(ary))
        return False
    
    for i in range(len(ori)):
        if ori[i] not in ary:
            print(i, "th element", ori[i], "lost!!")
            return False
        
    return True


if __name__ == '__main__':
    CompareAry([40, 98, 81, 80], [40, 81, 81, 81])