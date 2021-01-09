# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 09:03:42 2020

@author: guodxu@qq.com
"""


def getMaxArea(area: list) -> int:
    def getCount(graph, nRow, nCol, maxCols) -> int:
        if graph[nRow][nCol] == 0:
            return 0

        count = 1
        graph[nRow][nCol] = 0  # avoid re-calculate
        if nRow > 0:
            count += getCount(graph, nRow - 1, nCol, maxCols)  # up
        if nRow < len(graph) - 1:
            count += getCount(graph, nRow + 1, nCol, maxCols)  # down
        if nCol > 0:
            count += getCount(graph, nRow, nCol - 1, maxCols)  # left
        if nCol < maxCols:
            count += getCount(graph, nRow, nCol + 1, maxCols)  # right
        return count

    maxCount = 0
    maxCols = len(area[0]) - 1
    for i, row in enumerate(area):
        for j, col in enumerate(row):
            if col == 1:
                count = getCount(area, i, j, maxCols)
                print('[', i, j, ']: ', count)
                if count > maxCount:
                    maxCount = count

    return maxCount


if __name__ == "__main__":
    fun = getMaxArea
    graph = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
             [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
             [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    print(fun(graph))
    print(fun([[0, 0, 0, 0, 0, 0, 0, 0]]))
