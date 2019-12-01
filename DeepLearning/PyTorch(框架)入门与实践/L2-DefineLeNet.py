# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 2019

@author: guodx
"""

import torch as th
import torch.nn as nn
import torch.nn.functional as tfun
import torch.optim as optim
from torch.autograd import Variable

class Net(nn.Module):
    def __init__(self):
        # run the parent's init
        super(Net, self).__init__()

        # 卷积层‘1’表示输入图片为单通道，‘6’表示输出通道数
        # ‘5’表示卷积核为5*5
        self.conv1 = nn.Conv2d(1, 6, 5)
        # 卷积层
        self.conv2 = nn.Conv2d(6, 16, 5)
        # 仿射层/全连接层，y=Wx+b
        self.fc1 = nn.Linear(16*5*5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        # 卷积 - 激活 - 池化
        x = tfun.max_pool2d(tfun.relu(self.conv1(x)), (2,2))
        x = tfun.max_pool2d(tfun.relu(self.conv2(x)), 2)
        # reshape, '-1'表示自适应
        x = x.view(x.size()[0], -1)
        x = tfun.relu(self.fc1(x))
        x = tfun.relu(self.fc2(x))
        x = self.fc3(x)
        return x

net = Net()
print(net)

# print(list(net.parameters()))
for name, para in net.named_parameters():
    print(name, ":", para.size())


input = Variable(th.randn(1,1,32,32))

'''
print(input)
out = net(input)
print(out.size())
#print(out)

net.zero_grad() # 所有参数的梯度清零
out.backward(Variable(th.ones(1,10)))
print(out)
'''

output = net(input)
target = Variable(th.arange(0,10, dtype=th.float32)).view(1,-1)
print('traget: ', target)

'''
criterion = nn.MSELoss()
loss = criterion(output, target)
print("loss:", loss)

print("backward before:", net.conv1.bias.grad)
net.zero_grad()
loss.backward()
print("backward after:", net.conv1.bias.grad)
'''

optimizer = optim.SGD(net.parameters(), lr=0.01)
optimizer.zero_grad()
criterion = nn.MSELoss()
loss = criterion(output, target)
print("loss before: ", loss)
print("backward before:", net.conv1.bias.grad)
loss.backward()
optimizer.step()
print("loss after: ", loss)
print("backward after:", net.conv1.bias.grad)

