import pandas as pd
import matplotlib.pyplot as plt

pa=pd.read_csv('d:/CSV/pa.CSV',header=0, index_col='date',names=['code','shortname','date','open','high','low','close','volume','amount','no'], encoding='gb2312')
pa.index=pd.to_datetime(pa.index)
# delete the last column
#pa.drop('no',axis=1,inplace=True)
pa.dropna(axis=1, how='all', inplace=True)

pClose=pa.close
pOpen=pa.open
plt.plot(pClose, label='收盘价', c='y', linestyle='solid')
plt.plot(pOpen, label='开盘价', c='b', ls=':')
plt.legend()    # 显示图例
plt.xticks(rotation=45)
plt.title(u'平安2018年')
plt.xlabel(u'日期')
plt.ylabel(u'价格')
plt.grid(True,axis='both')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.show()