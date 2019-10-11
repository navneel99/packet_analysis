import csv
import sys

# infile = sys.argv[1]

class fileReader:
    rawdata=[]
    tcpdata=[]
    ftpdata=[]
    csv_sep=""
    fname=""

    srciplist=[]
    destiplist=[]

    serverips=[]
    clientips=[]

    tcpflows={} #(src_ip,src_p,dst_ip,dst_p):[list of connections(SYN,ACK,FIN,RST)]

    def __init__(self,filename,sep=","):
        self.fname = filename
        self.csv_sep = sep
        self.create_data()
        self.generate_TCP_flows()

    def create_data(self):
        with open(self.fname,'r') as f:
            data=csv.reader(f,delimiter=self.csv_sep)
            for x in data:
                self.rawdata.append(x)
                if (x[4] == "TCP"):
                    self.tcpdata.append(x)
                else:
                    self.ftpdata.append(x)
            # self.rawdata = [x for x in data]
            # self.tcpdata = [x if x[4] == "TCP" for x in data]
            # self.ftpdata = [x if x[4] == "FTP" for x in data]
    def generate_duration_flow(four_tuple):
        pass

    def generate_TCP_flows(self):
        for row in self.tcpdata:
            src_ip = row[2]
            dst_ip = row[3]
            relevant_string = ""
            for s in row[6]:
                if s != "[":
                    relevant_string+=s
                else:
                    break
            prt_l = [x.strip(" ") for x in relevant_string.split(">")]
            src_p = prt_l[0]
            dst_p = prt_l[1]

            if src_p == "21":
                if src_ip not in self.serverips:
                    self.serverips.append(src_ip)
                if dst_ip not in self.clientips:
                    self.clientips.append(dst_ip)
            elif dst_p == "21":
                if src_ip not in self.clientips:
                    self.clientips.append(src_ip)
                if dst_ip not in self.serverips:
                    self.serverips.append(dst_ip)

            dict_key = (src_ip,src_p,dst_ip,dst_p)
            flip_key = (dst_ip,dst_p,src_ip,src_p)

            if src_ip not in self.srciplist:
                self.srciplist.append(src_ip)

            if dst_ip not in self.destiplist:
                self.destiplist.append(dst_ip)

            if (dict_key not in self.tcpflows and flip_key not in self.tcpflows):
                self.tcpflows[dict_key] = []
                self.tcpflows[dict_key].append(row)
            elif (flip_key not in self.tcpflows):
                self.tcpflows[dict_key].append(row)
            else:
                self.tcpflows[flip_key].append(row)

            # self.tcpflows[dict_key].append(row) #Add the first packet to the flow


    # def info_parser(self):
    #     for row in self.rawdata:
    #         if (row[5] == "TCP"):
    #
    #
    #     pass
