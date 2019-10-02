import csv
import sys

# infile = sys.argv[1]

class fileReader:
    rawdata=[]
    csv_sep=""
    fname=""

    srciplist=[]
    destiplist=[]
    tcpflows=[]

    def __init__(self,filename,sep=","):
        self.fname = filename
        self.csv_sep = sep
        self.create_data()

    def create_data(self):
        with open(self.fname,'r') as f:
            data=csv.reader(f,delimiter=self.csv_sep)
            self.rawdata = [x for x in data]

    def generate_TCP_flows(self):
        pass

    def generate_unique_ips(self):
        pass

    def info_parser(self):
        pass
