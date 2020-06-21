# -*- coding:utf-8 -*-
# @file : MarkHeader.py
# @date : 2016/6/21
# @author : guodxu@qq.com
# @desc :
# @version : 1.0
# -*- -*- -*- -*- -*- -*-

import os
import re
import shutil
import sys

global MaxLevel


def getHeader(vHeader, newHeader):
    global MaxLevel
    nLevel = len(newHeader)
    if nLevel > MaxLevel:
        return newHeader  # not regular header, just return the ori

    # Reset the Header-Level, and build the new-Header
    vHeader[nLevel - 1] += 1
    for i in range(nLevel, MaxLevel):
        vHeader[i] = 0

    return newHeader + '.'.join(str(item) for item in vHeader[:nLevel]) + ' '


def markFileOp(oriFile, newFile):
    global MaxLevel
    vHeader = [0, 0, 0, 0, 0, 0]
    MaxLevel = len(vHeader)

    reHeader = re.compile(r'^#+\s*[\.0-9]*\s*')
    reLevel = re.compile(r'^#+')
    with open(oriFile, 'r', encoding='utf-8') as rFile, open(newFile, 'w', encoding='utf-8') as wFile:
        for line in rFile:
            isHeader = reHeader.match(line)
            if isHeader:
                newHeader = getHeader(vHeader, reLevel.match(line).group())
                nRemove = isHeader.span()[1]
                line = newHeader + line[nRemove:]

            wFile.write(line)


if __name__ == "__main__":
    usage = '''Usage: MarkHeader.py markfile [replace]
    if give three-param, modify the ori-file,
    otherwise restore in markfile.bak 
    '''
    argCount = len(sys.argv)
    if argCount == 1:
        print(usage)
        # raw_input("Press any key, to exit:")
        exit(0)

    print(' '.join(sys.argv))
    oriFile = sys.argv[1]
    newFile = oriFile + '.bak'
    markFileOp(oriFile, newFile)
    if argCount > 2:
        shutil.copyfile(newFile, oriFile)
        os.remove(newFile)
        print('Add header complete of ' + oriFile)
    else:
        print('Add header complete to ' + newFile)
