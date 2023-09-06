import torch
import torchvision
import torch.nn as nn
import torch.optim as optim
#from torchsummary import summary
import torch.nn.functional as F
import math
import random

dtype = torch.float
device = torch.device("cpu")

randomList = []
randomList1 = []

for idx in range(0,2000):
    n = random.randint(1,2000)
    randomList.append(n)
    squared_n = n*n
    randomList1.append(squared_n)


xTrain = torch.Tensor(randomList)

yTrain = torch.tensor(randomList1)

print (xTrain)
print(yTrain)
# Randomly initialize weights
a = torch.randn((), device=device, dtype=dtype)
b = torch.randn((), device=device, dtype=dtype)
c = torch.randn((), device=device, dtype=dtype)
d = torch.randn((), device=device, dtype=dtype)
learning_rate = 1e-6

for t in range(2000):
    x = xTrain[t]
    y_pred = (a + b*xTrain[t] + c*(xTrain[t]**2) + d*(xTrain[t]**3))

    loss = (y_pred - yTrain[t]).pow(2).sum().item()

    if t%100 == 99:
        print(t,loss)
    
    # Backprop to compute gradients of a, b, c, d with respect to loss
    grad_y_pred = 2.0 * (y_pred - yTrain[t])
    
    grad_a = grad_y_pred.sum()
    grad_b = (grad_y_pred * x).sum()
    grad_c = (grad_y_pred * x ** 2).sum()
    grad_d = (grad_y_pred * x ** 3).sum()

    # Update weights using gradient descent
    a -= learning_rate * grad_a
    b -= learning_rate * grad_b
    c -= learning_rate * grad_c
    d -= learning_rate * grad_d

print(f'Result: y = {a.item()} + {b.item()} x + {c.item()} x^2 + {d.item()} x^3')