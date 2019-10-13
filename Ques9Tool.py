import csv_parser as cv
import matplotlib.pyplot as plt
import sys

def ReturnFlows(t):
    flow = t.tcpflows
    return flow

def SequenceNumberPlot(t, flow):
    d = t.sequence_number_generator(flow)
    keys = list(d.keys())
    
    x = []
    y1 = []
    y2 = []

    for i in range(len(keys)):
        temp = d[keys[i]]
        n = len(temp[0])
        m = len(temp[1])

        if(n == 1 and m == 1):
            y1.append(float(temp[0][1]))
            y2.append(float(temp[0]))

temp = cv.fileReader("lbnl.anon-ftp.03-01-11.csv")

