# -*- coding: utf-8 -*-


def CheckSeqI(ary:list, sel:int)->bool:
    if sel<1 or sel>len(ary): raise(Exception('Invalid Param'))
    
    sel -= 1  # ary is 0-start, while sel is 1-start
    for n in range(0, sel):
        if ary[n]>ary[sel]:
            print('{}th element {} larger than Seled'.format(n, ary[n]))
            return False
        
    for n in range(sel+1, len(ary)-1):
        if ary[n]<ary[sel]:
            print('{}th element {} less than Seled'.format(n, ary[n]))
            return False
            
    return True

if __name__ == '__main__':
    import sys
    import traceback
    try:
        CheckSeqI([], 0)
    except Exception:
        traceback.print_exception(*sys.exc_info())
    else:
        print("No exception")
    finally:
        print("complete")
