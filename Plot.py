import csv_parser as cv
import matplotlib.pyplot as plt
import numpy as np

def Plotbar(x, y, labelx, labely, title, fsize = 5):
    index = np.arange(len(x))
    plt.bar(index,y)
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.title(title)
    plt.xticks(index, x, rotation = 30, fontsize = fsize)
    plt.show()

def UServerIP(t):
    print(len(t.serverips))

def UClientIP(t):
    print(len(t.clientips))

def UTCPFlow(t):
    print(len(t.tcpflows))

def PlotFlow(t):
    
    #X-axis of the graph
    y = [0]*24
    x = range(24)

    tcpflow = t.tcpflows
    d = list(tcpflow.keys())

    for i in range(len(tcpflow)):
        for j in range(24):
            t = float(tcpflow[d[i]][0][1])/3600
            if(t < j+1 ):
                y[j] = y[j] + 1
                break
    
    # sum = 0
    # for i in range(24):
    #     sum = sum + x[i]
    #     print(i,"=>",x[i])
    # print(sum)

    Plotbar(x, y, "Time of Day", "Number of Connections", "Number of connections opened to any FTP server")       

def PlotConDur(t):

    # getting the list of keys
    temp = t.tcpflows
    d = list(temp.keys())

    y = []
    for i in range(len(d)):
        duration = t.generate_duration_flow(d[i])
        for j in range(len(duration)):
            y.append(duration[j])

    y.sort()
    max_x = int(y[len(y)-1]+100)
    x = range(max_x)

    n = len(y)

    yy = [0]*max_x

    for i in range(max_x):
        for j in range(n):
            if(y[j]>i):
                break
            else:
                yy[i] = yy[i] + 1
        yy[i] = yy[i]/n
    
    print(len(x), len(yy))
    print(y[len(y)-8])
    plt.plot(x, yy)
    plt.show()


temp = cv.fileReader("lbnl.anon-ftp.03-01-11.csv")

PlotConDur(temp)
