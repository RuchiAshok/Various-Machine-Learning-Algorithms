# -*- coding: utf-8 -*-
"""NeuralNetwork_LinenarRegression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16h1VIVjnq0_VWOp4w98fINYbXSqO9UB3

**Importing Libraries**
"""

import torch
import torch.nn as nn 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""**Reading Dataset**"""

data = pd.read_csv("Advertising.csv")

"""**Seperating input feature and target labels**"""

X = data.TV.values
Y = data.Sales.values

"""**Normalizing the inputs between 0 to 1**"""

Y = (Y - np.min(Y))/(np.max(Y)-np.min(Y))
X = (X - np.min(X))/(np.max(X)-np.min(X))

"""**Converting NumPy To Torch**"""

X = X.astype(np.float32)
Y = Y.astype(np.float32)

X = torch.from_numpy(X).view(-1,1)
Y = torch.from_numpy(Y).view(-1,1)

"""**Creating Neural Network for Linear Regression**"""

class LinearRegressionNetwork(torch.nn.Module):
    def __init__(self):
        super(LinearRegressionNetwork, self).__init__()

        '''
        Number of input features =  1
        Total Hidden Layers used =1
        Activation Functions used = Relu, Sigmoid, Tanh
        '''

        self.layer1 = torch.nn.Linear(1, 1) 
        self.final_layer = nn.Linear(1, 1) 
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()
        self.tanh = nn.Tanh()
        self.dropout = nn.Dropout(p=0.1)
        self.batchnorm1 = nn.BatchNorm1d(1)

    def forward(self, x):
        #Y_pred = self.relu(self.layer1(x))
        #Y_pred = self.sigmoid(self.layer1(x))
        Y_pred = self.tanh(self.layer1(x))
        Y_pred = self.batchnorm1(x)
        Y_pred = self.dropout(x)
        Y_pred = self.final_layer(x)
        return Y_pred

"""**Training the Linear Model** """

model = LinearRegressionNetwork()
print(model)

l = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr =0.006 )

num_epochs = 200
for epoch in range(num_epochs):
    Y_pred = model(X.requires_grad_())
    loss= l(Y_pred, Y)

    #backward propagation
    loss.backward()

    #Weight Updation
    optimizer.step()
    optimizer.zero_grad()
    
    print('Epoch:  {} |  loss:  {}'.format(epoch, loss.item()))

predicted = model(X).detach().numpy()

"""**Plotting the Graph**"""

plt.scatter(X.detach().numpy()[:num_epochs] , y.detach().numpy()[:num_epochs])
plt.plot(X.detach().numpy()[:num_epochs] , predicted[:num_epochs] , "red")
plt.xlabel("TV")
plt.ylabel("Sales")
plt.show()