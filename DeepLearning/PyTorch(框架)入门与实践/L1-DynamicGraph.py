# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 22:50:17 2019

@author: guodxu@qq.com
"""

import torch as th
from torch.autograd import Variable

N, D, H  = 3, 4, 5

x=Variable(th.randn(N,D))
# print(x)
w1=Variable(th.randn(D, H))
w2=Variable(th.randn(D,H))

z = th.randint(10, [1])
print(z)

if(z[0]>5):
    y=x.mm(w1)
else:
    y=x.mm(w2)
    
print(y)
