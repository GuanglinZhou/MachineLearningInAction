#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def file2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())  # get the number of lines in the file
    returnMat = np.zeros((numberOfLines, 3))  # prepare matrix to return
    classLabelVector = []  # prepare labels return
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        # classLabelVector.append(int(listFromLine[-1]))//convert is incorrectly
        if listFromLine[-1] == 'largeDoses':
            classLabelVector.append(3)
        elif listFromLine[-1] == 'smallDoses':
            classLabelVector.append(2)
        else:
            classLabelVector.append(1)
        index += 1
    return returnMat, classLabelVector


def main():
    type1_x = []
    type1_y = []
    type2_x = []
    type2_y = []
    type3_x = []
    type3_y = []
    datingDataMat, datingLabels = file2matrix("datingTestSet.txt")
    for i in range(len(datingLabels)):
        if datingLabels[i] == 1:
            type1_x.append(datingDataMat[i][0])
            type1_y.append(datingDataMat[i][1])
        elif datingLabels[i] == 2:
            type2_x.append(datingDataMat[i][0])
            type2_y.append(datingDataMat[i][1])
        else:
            type3_x.append(datingDataMat[i][0])
            type3_y.append(datingDataMat[i][1])

    fig = plt.figure();
    fig.add_subplot(111)
    plt.scatter(type1_x, type1_y, c='r', label='didntLike')
    plt.scatter(type2_x, type2_y, c='b', label='smallDoses')
    plt.scatter(type3_x, type3_y, c='g', label='largeDoses')
    plt.xlabel('Flight miles')
    plt.ylabel('video game time percent')
    plt.legend(loc=1)
    plt.show()


if __name__ == '__main__':
    main()
