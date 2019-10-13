import csv_parser as cv
import matplotlib.pyplot as plt
import sys


def ReturnFlows(t):
    flow = t.tcpflows
    return flow

# Returns  Max ans Second Max of the 
def SelectFlow(t):
    flow = ReturnFlows(t)
    keys = list(flow.keys())

    max = 0
    maxvalue = 0
    smax = 0
    for i in range(len(keys)):
        temp, server_temp, client_temp = t.generate_bytes_sent(keys[i])
        for j in range(len(temp)):
            tem = temp[j]
            if(maxvalue < tem):
                smax = max
                max = keys[i]
                maxvalue = temp[j]
    
    return max, smax

# Returns list of Spurious Transmission List
def SRetList(t):
    flow = ReturnFlows(t)
    ky = list(flow.keys())
    ans = []

    for i in range(len(ky)):
        # print(ky[i])
        d = t.sequence_number_generator(ky[i])
        keys = list(d.keys())

        for j in range(len(keys)):
            temp = d[keys[j]]
            m = len(temp[1])
            if(m > 1):
                ans.append([ky[i], keys[j]])
    

    return ans

def MaxSRetList(t, keys):
    max = 0 
    maxkey = 0
    for i in range(len(keys)):
        # print(keys[i][0])
        d = t.sequence_number_generator(keys[i][0])
        ky = list(d.keys())

        for j in range(len(ky)):
            temp = d[ky[j]]
            m = len(temp[1])
            if(max<m):
                max = m
                maxkey = keys[i]
    
    return maxkey

#Returs list of Normal Retransmission List
def RetList(t):
    flow = ReturnFlows(t)
    ky = list(flow.keys())
    ans = []

    for i in range(len(ky)):
        # print(ky[i])
        d = t.sequence_number_generator(ky[i])
        keys = list(d.keys())

        for j in range(len(keys)):
            temp = d[keys[j]]
            m = len(temp[0])
            if(m > 1):
                ans.append([ky[i], keys[j]])
    

    return ans

def MaxRetList(t, keys):
    max = 0 
    maxkey = 0
    for i in range(len(keys)):
        # print(keys[i][0])
        d = t.sequence_number_generator(keys[i][0])
        ky = list(d.keys())

        for j in range(len(ky)):
            temp = d[ky[j]]
            m = len(temp[0])
            if(max<m):
                max = m
                maxkey = keys[i]
    
    return maxkey

def SequenceNumberPlot(t, FlowKey):
    d = t.sequence_number_generator(FlowKey)
    keys = list(d.keys())

    Flows = ReturnFlows(t)
    flow = Flows[FlowKey]

    
    # X axis is time and Y axis is Sequence Number y1 for SYN-ACK and y2 for ACK
    y1 = []
    y2 = []

    x1 = []
    x2 = []

    max = 0
    min = 1000000000000
    maxy = 0
    miny = 1000000000000
    for i in range(len(keys)):
        temp = d[keys[i]]
        n = temp[0]  # SYN-ACK
        m = temp[1] # ACK
        print(len(n), len(m))

        for j in range(len(n)):
            x1.append(float(n[j]))
            y1.append(int(keys[i]))
            if(max<float(n[j])):
                max = float(n[j])
            if(min>float(n[j])):
                min = float(n[j])
            if(maxy < float(keys[i])):
                maxy = float(keys[i])
            if(miny > float(keys[i])):
                miny = float(keys[i])

        for j in range(len(m)):
            x2.append(float(m[j]))
            print(m[j])
            y2.append(int(keys[i]) + 1)
            if(max<float(m[j])):
                max = float(m[j])
            if(min>float(m[j])):
                min = float(m[j])
            if(maxy < float(keys[i]) + 1):
                maxy = float(keys[i]) + 1
            if(miny > float(keys[i]) + 1):
                miny = float(keys[i])

    max = int(max)

    plt.plot(x1, y1, "ro")
    plt.plot(x2, y2, "go")
    plt.xlim([min-0.1,max+1])
    plt.ylim([miny - 5, maxy + 5])
    plt.show()

program_name = sys.argv[0]
n = int(sys.argv[1])

if n == 1:
    temp = cv.fileReader("lbnl.anon-ftp.03-01-11.csv")
else:
    if n == 2:
        temp = cv.fileReader("lbnl.anon-ftp.03-01-14.csv")
    else:
        temp = cv.fileReader("lbnl.anon-ftp.03-01-18.csv")


UTCP = temp.tcpflows
keys = list(UTCP.keys())

# max, smax = SelectFlow(temp)
ans = SRetList(temp)
# print("-----------------")
key = MaxSRetList(temp, ans)
print(key)

SequenceNumberPlot(temp, key[0])
