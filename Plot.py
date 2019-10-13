import csv_parser as cv
import matplotlib.pyplot as plt
import numpy as np
import sys
import os

def Plotbar(x, y, labelx, labely, title, save, fsize = 5):
    index = np.arange(len(x))
    plt.bar(index,y)
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.title(title)
    plt.xticks(index, x, rotation = 30, fontsize = fsize)
    plt.savefig(save)
    plt.close()

def Plot(x, y, labelx, labely, title, save, fsize = 5):
    index = np.arange(len(x))
    plt.plot(index,y)
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.title(title)
    plt.xticks(index, x, rotation = 30, fontsize = fsize)
    plt.savefig(save)
    plt.close()


# Question Number 1
def UServerIP(t):
    print("Unique Number Server IPs are: ",len(t.serverips))

def UClientIP(t):
    print("Unique Number Client IPs are: ",len(t.clientips))

# Question Number 2
def UTCPFlow(t):
    print("Unique Number TCP Flows are: ",len(t.tcpflows))

# Question Number 3
def PlotFlow(t, save):
    
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
    Plotbar(x, y, "Time of Day", "Number of Connections", "Number of connections opened to any FTP server", save)       

# Question Number 4
def PlotConDur(t, save):

    # getting the list of keys
    temp = t.tcpflows
    d = list(temp.keys())

    y = []
    for i in range(len(d)):
        duration = t.generate_duration_flow(d[i])
        for j in range(len(duration)):
            y.append(duration[j])

    y.sort()
    max_x = int(y[len(y)-1]+5)
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
        print(yy[i])
        if(yy[i] > 0.995):
            break
    
    Plot(x, yy, "P(Conn. Duration < X)", "Connection Duration (sec)", "CDF of the connection duration", save)

#Question number 6
def interarrivalCDF6(t, save):
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
    Plot(x, CDF, "P(inter-arrival time<X)", "Inter arrival Time(sec)", "CDF of Inter Arrival time", save)

    return y

# Question number 7
def interarrivalCDF7(t, save):
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

    print(mean)
    print(median)

    x = range(max_x)
    Plot(x, CDF, "P(inter-arrival time<X)", "Inter arrival Time(sec)", "CDF of Inter Arrival time", save)

# Interarrival time of outgoing packet
def interarrivalCDF8(t, save):
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

# Question Number 8
def GLenIncoming(t, save):
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
    print("Mean of Incoming Packet Length is: ",mean)
    print("Median of Incoming Packet Length is: ", median)

    max_x = int(clist[n-1]) + 10
    x = range(max_x)
    y = []

    for i in range(max_x):
        sum = 0
        for j in range(n):
            if(clist[j] <= x[i]):
                sum = sum + 1
            else:
                break
        y.append(sum)
    
    Plot(x, y, "P(inter-arrival time<X)", "Inter arrival Time(sec)", "CDF of Inter Arrival time of Incoming Packet", save)    
            
def GLenOutgoing(t, save):
    itemp, inter = t.generate_server_inter_arrival_time()

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
    print("Mean of Outgoing Packet Length is: ",mean)
    print("Median of Outgoing Packet Length is: ", median)

    max_x = int(clist[n-1]) + 10
    x = range(max_x)
    y = []

    for i in range(max_x):
        sum = 0
        for j in range(n):
            if(clist[j] <= x[i]):
                sum = sum + 1
            else:
                break
        y.append(sum)
    
    Plot(x, y, "P(inter-arrival time<X)", "Inter arrival Time(sec)", "CDF of Inter Arrival time of Outgoing Packet", save)    


program_name = sys.argv[0]
n = int(sys.argv[1])
m = int(sys.argv[2])
if n == 1:
    temp = cv.fileReader("lbnl.anon-ftp.03-01-11.csv")
else:
    if n == 2:
        temp = cv.fileReader("lbnl.anon-ftp.03-01-14.csv")
    else:
        temp = cv.fileReader("lbnl.anon-ftp.03-01-18.csv")

if m == 1 :
    #Qestion Number 1
    UServerIP(temp)
    print("------------------------------")
    UClientIP(temp)
    print("------------------------------")

if m == 2:
    #Question Number 2
    UTCPFlow(temp)
    print("------------------------------")

if m == 3:
    #Question Number 3
    save = "Q3"+str(n)+".png"
    PlotFlow(temp, save)
    print("------------------------------")

if m == 4:
    # Question Number 4
    print(4)
    save = "Q4"+str(n)+".png"
    PlotConDur(temp, save)
    print("------------------------------")

if m == 5:
    # Question Number 5
    print("------------------------------")
    

if m == 6:
    # Question Number 6
    save = "Q6"+str(n)+".png"
    interarrivalCDF6(temp, save)
    print("------------------------------")

if m == 7:
    # Question Number 7
    save = "Q7"+str(n)+".png"
    interarrivalCDF7(temp, save)
    print("------------------------------")

if m == 8:
    # Question Number 8
    save = "Q8"+str(n)+"1.png"
    GLenIncoming(temp, save)
    print("------------------------------")
    save = "Q8"+str(n)+"2.png"
    GLenOutgoing(temp, save)
    print("------------------------------")

