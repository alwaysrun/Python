# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 20:36:30 2020

@author: guodx
"""

import os,sys,getopt
import stat,glob,shutil

def readonlyHandle(func, fPath, execInfo):
    os.chmod(fPath, stat.S_IWRITE)
    func(fPath)
    
def rmDirRecurse(fPath, fFilter):
    fRoot = os.path.join(fPath, '**', fFilter)
    print('To find:', fRoot)
    
    files = glob.glob(fRoot, recursive=True)
    if not files:
        print('No file found')
        return
    
    for f in files:
        if os.path.isdir(f):
            print('to del-dir:', f)
            shutil.rmtree(f, onerror=readonlyHandle)
        else:
            print('to del-file', f)
            os.chmod(f, stat.S_IWRITE) # ensure we can del readonly-file
            os.remove(f)
            
if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hp:f:', ['path=', 'filter='])
    except getopt.GetoptError:
        print('rmDirs -p <Path to find> -f <filter>')
        sys.exit(2)
        
    fPath = None
    fFilter = []
    for op, v in opts:
        if op in ('-p', '--path'):
            fPath = v
        if op in ('-f', 'filter'):
            fFilter.append(v)
            
    if not fPath or not fFilter:
        print('rmDirs -p <Path to find> -f <filter>')
        sys.exit(2)
    
    for f in fFilter:
        rmDirRecurse(fPath, f)
    