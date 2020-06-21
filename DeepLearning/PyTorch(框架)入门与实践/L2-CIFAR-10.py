# -*- coding: utf-8 -*-
"""
Created on Sat Dec 1 2019

@author: guodxu@qq.com
"""

import torch as t
import torchvision as tv
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms
from torchvision.transforms import ToPILImage
from torch import optim
from torch.autograd import Variable

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16*5*5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = F.max_pool2d(F.relu(self.conv1(x)), (2,2))
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        x = x.view(x.size()[0], -1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

if __name__ == '__main__':
    ToImg = ToPILImage()
    
    transf = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])
    
    trainset = tv.datasets.CIFAR10(root='./Data/CIFAR-10',
        train=True,
        download=True,
        transform=transf
    )
    
    trainloader = t.utils.data.DataLoader(
        trainset,
        batch_size=4,
        shuffle=True,
        num_workers=2
    )
    
    testset = tv.datasets.CIFAR10(
        root='./Data/CIFAR-10',
        train=False,
        download=True,
        transform=transf
    )
    
    testloader = t.utils.data.DataLoader(
        testset,
        batch_size=4,
        shuffle=False,
        num_workers=2
    )
    
    classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')
    
    '''
    (data, label) = trainset[100]
    print(classes[label])
    #ToImg((data+1)/2).resize((100,100)).show()
    
    
    dataiter = iter(trainloader)
    images, labels = dataiter.next()
    print(' '.join('%11s'%classes[labels[j]] for j in range(4)))
    #ToImg(tv.utils.make_grid((images+1)/2)).resize((400, 100)).show()
    '''

    net = Net()
    print(net)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.95)
    # optimizer.zero_grad()

    for epoch in range(2):
        runningLoss = 0.0
        for i,data in enumerate(trainloader, 0):
            inputs, labels = data
            inputs, labels = Variable(inputs), Variable(labels)

            # zero-clear the grad
            optimizer.zero_grad()

            outputs = net(inputs)
            loss = criterion(outputs, labels)
            loss.backward()    

            optimizer.step()

            runningLoss += loss.item()
            if (i+1)%2000 == 0:
                print('[%d, %5d] loss: %.3f'%(epoch+1, i+1, runningLoss/2000))
                runningLoss = 0.0

    print('finished training')

    # check the training
    correct = 0
    total = 0
    for data in testloader:
        images, labels = data
        outputs = net(Variable(images))
        _, predicted = t.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum()
    print('%d tester, and the accuracy is %d %%' % (total, (100*correct/total)))
