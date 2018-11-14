# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 09:53:43 2018

@author: xugd
"""
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pa=pd.read_csv('d:/CSV/pa.CSV',header=0, index_col='date',names=['code','shortname','date','open','high','low','close','volume','amount','no'], encoding='gb2312')
pa.index=pd.to_datetime(pa.index)

pClose=pa.close
pd=pClose.describe()

min=math.floor(pd['min'])
max=math.ceil(pd['max'])
pri=np.linspace(min,max,5,dtype=int)

ary=[0,0,0,0]

'''
low=pd.iloc[4]
mid=pd.iloc[5]
high=pd.iloc[6]
'''

for i in pClose:
    if (i<pri[1]):
        ary[0] += 1
    elif (i<pri[2]):
        ary[1] += 1
    elif (i<pri[3]):
        ary[2] += 1
    else:
        ary[3] += 1
        
#plt.bar(pri[:-1], ary, 4)
xbar=plt.subplot(221)
xbar.bar(pri[:-1], ary, 4)
xbar.set_xlabel('价格')
xbar.set_ylabel('数量')
xbar.set_title('收盘价柱状图')
        
lb=[]
for i in range(len(pri)-1):
    lb.append("(%d,%d]" % (pri[i], pri[i+1]))

#plt.pie(ary, labels=lb, shadow=True)
xpie=plt.subplot(222)
xpie.pie(ary, labels=lb, shadow=True)
xpie.set_title("收盘价饼状图")

#plt.boxplot(pClose)

# plt.hist(pClose, bins=12)
#xhist=plt.subplot(212)
#xhist.hist(pClose)

xplot=plt.subplot(212)
xplot.plot(pClose, label='收盘价', c='y', linestyle='solid')
xplot.set_title(u'平安2018年收盘价曲线', loc='right')
xplot.set_xlabel(u'日期')
xplot.set_ylabel(u'价格')
xplot.grid(True,axis='both')
xplot.tick_params(axis='x', labelrotation=45)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.subplots_adjust(hspace=0.35)
        
plt.show()
