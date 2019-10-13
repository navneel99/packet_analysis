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

#Question number 6
def interarrivalCDF6(t):
    inter_arrival = t.new_connection_time

    y = []
    n = len(inter_arrival)
    for i in range(n-1):
        temp = float(inter_arrival[i+1][1]) - float(inter_arrival[i][1])
        y.append(temp)

    y.sort()

    sum = 0
    n = len(y)
    for i in range(n):
        sum = sum + y[i]

    mean = sum/n
    median = y[int(n/2)]

    print(mean)
    print(median)

    # Calculating CDF
    max_x = int(y[n-1] + 10)
    CDF = np.zeros(max_x)
    for i in range(max_x):
        count = 0
        for j in range(n):
            if(y[j]<=i):
                count = count + 1
            else:
                break
        CDF[i] = count

    x = range(max_x)
    plt.plot(x,CDF)
    plt.show()

    return y

# Question number 7
def interarrivalCDF7(t):
    inter_arrival, t = t.generate_server_inter_arrival_time()

    clist = []
    
    n = len(inter_arrival)
    for i in range(n):
        clist.append(float(inter_arrival[i][1]))
    
    clist.sort()

    y = []
    n = len(clist) - 1  
    for i in range(n):
        temp = clist[i+1] - clist[i]
        y.append(temp)

    y.sort()

    sum = 0
    n = len(y)
    print(y[n-1])
    for i in range(n):
        sum = sum + y[i]

    mean = sum/n
    median = y[int(n/2)]

    max_x = int(y[n-1] + 10)
    CDF = np.zeros(max_x)
    for i in range(max_x):
        count = 0
        for j in range(n):
            if(y[j]<=i):
                count = count + 1
            else:
                break
        CDF[i] = count

    x = range(max_x)
    plt.plot(x,CDF)
    plt.show()
    # print(sum)
    print(mean)
    print(median)

# Question number 8
def interarrivalCDF8(t):
    itemp, inter_arrival = t.generate_server_inter_arrival_time()

    clist = []
    
    n = len(inter_arrival)
    for i in range(n):
        clist.append(float(inter_arrival[i][1]))
    
    clist.sort()

    y = []
    n = len(clist) - 1  
    for i in range(n):
        temp = clist[i+1] - clist[i]
        y.append(temp)

    y.sort()

    sum = 0
    n = len(y)
    print(y[n-1])
    for i in range(n):
        sum = sum + y[i]

    mean = sum/n
    median = y[int(n/2)]

    max_x = int(y[n-1] + 10)
    CDF = np.zeros(max_x)
    for i in range(max_x):
        count = 0
        for j in range(n):
            if(y[j]<=i):
                count = count + 1
            else:
                break
        CDF[i] = count

    x = range(max_x)
    plt.plot(x,CDF)
    plt.show()
    # print(sum)
    print(mean)
    print(median)


def GLenIncoming(t):
    inter, itemp = t.generate_server_inter_arrival_time()

    clist = []
    n = len(inter)
    for i in range(n):
        clist.append(float(inter[i][5]))
    
    clist.sort()
    sum = 0
    n = len(clist)
    for i in range(n):
        sum = sum + clist[i]
    
    mean = sum/n
    median = clist[int(n/2)]
    print("Mean of Incoming Length of the packet is: ",mean)
    print("Median of Incoming Length of the packet is:", median)

    max_x = clist[n-1]
    x = range(max_x)




temp = cv.fileReader("lbnl.anon-ftp.03-01-11.csv")

GLenIncoming(temp)
