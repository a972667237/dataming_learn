'''
Created on Nov 22, 2010

@author: Peter
'''
from numpy import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def plotVector(data, label, suppVec, w, b):
    xcord0 = []
    ycord0 = []
    xcord1 = []
    ycord1 = []
    markers =[]
    colors =[]
    for i, fea in enumerate(data):
        xPt = float(fea[0])
        yPt = float(fea[1])
        l = int(label[i])
        if (l == -1):
            xcord0.append(xPt)
            ycord0.append(yPt)
        else:
            xcord1.append(xPt)
            ycord1.append(yPt)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord0,ycord0, marker='s', s=90)
    ax.scatter(xcord1,ycord1, marker='o', s=50, c='red')
    plt.title('Support Vectors Circled')

    for vec in suppVec:
        circle = Circle((vec[0], vec[1]), 0.5, facecolor='none', edgecolor=(0,0.8,0.8), linewidth=3, alpha=0.5)
        ax.add_patch(circle)

    x_min, y_min = np.array(data).min(axis=0)
    x_max, y_max = np.array(data).max(axis=0)
    x = arange(x_min, x_max, 0.1)
    y = (-w[0]*x - b)/w[1]
    ax.plot(x,y.T)
    ax.axis([x_min-0.5,x_max+0.5,y_min-0.5, y_max+0.5])
    plt.show()
    