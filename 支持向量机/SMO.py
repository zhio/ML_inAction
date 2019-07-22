import matplotlib.pyplot as plt
import numpy as np
import random

def loadDataSet(fileName):
    dataMat = [];labelMat = []
    fr =  open(fileName)
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        dataMat.append([float(lineArr[0]),float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return dataMat,labelMat

def selectJrand(i,m):
    j = i
    while (j == i):
        j = int(random.uniform(0,m))
    return j
def clipAlpha(aj,H,L):
    if aj > H:
        aj = H
    if L > aj:
        aj = L
    return aj


def showDataSet(dataMat,labelMat):
    data_plus = []
    data_minus = []
    for i in range(len(dataMat)):
        if labelMat[i]>0:
            data_plus.append(dataMat[i])
        else:
            data_minus.append(dataMat[i])
    data_plus_np = np.array(data_plus)
    data_minus_np = np.array(data_minus)
    plt.scatter(np.transpose(data_plus_np)[0],np.transpose(data_plus_np)[1])
    plt.scatter(np.transpose(data_minus_np)[0],np.transpose(data_minus_np)[1])
    plt.show()

def smoSimple(dataMatIn,classLabels,C,toler,maxIter):
    dataMatrix = np.mat(dataMatIn);labelMat = np.mat(classLabels).transpose()
    b = 0;m,n = np.shape(dataMatrix)
    alphas = np.mat(np.zeros((m,1)))
    iter_num = 0
    while(iter_num<maxIter):
        alphaPairsChanged = 0
        for i in range(m):
            fXi = float(np.matrix)
if __name__ == '__main__':
    dataMat,labelMat = loadDataSet('testSet.txt')
    showDataSet(dataMat,labelMat)