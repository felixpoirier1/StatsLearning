#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  8 23:54:50 2022

@author: felix
"""
from kmean import createLine
import numpy as np
from random import shuffle, randrange
import matplotlib.pyplot as plt
import os


x1 = randrange(0, 100)
y1 = randrange(0, 100)
cluster1 = []

x2 = randrange(0, 100)
y2 = randrange(0, 100)
cluster2 = []

for i in range(20):
    x_1 = x1 + np.random.normal()*2
    y_1 = y1 + np.random.normal()*2
    
    cluster1 += [[x_1, y_1]]

    x_2 = x2 + np.random.normal()*2
    y_2 = y2 + np.random.normal()*2
    
    cluster2 += [[x_2, y_2]]

clusters = cluster1 + cluster2
shuffle(clusters)

Kmeans = createLine((clusters))
print(Kmeans)

# 100 linearly spaced numbers
x = np.linspace(max(min(x1, x2)-5, 0),max(x1, x2)+5,50)

# the function, which is y = x^2 here
y = Kmeans['b'] + Kmeans['a']*x
       
x_cluster_1 = np.asarray([couple[0] for couple in cluster1])
y_cluster_1 = np.asarray([couple[1] for couple in cluster1])
x_cluster_2 = np.asarray([couple[0] for couple in cluster2])
y_cluster_2 = np.asarray([couple[1] for couple in cluster2])

# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_xlim([0,100])
ax.set_ylim([0,100])
# plot the function
plt.scatter(x_cluster_1, y_cluster_1,c="red")
plt.scatter(x_cluster_2, y_cluster_2,c="blue")
plt.plot(x,y, color='black')
os.getcwd()

randrange(0, 100)