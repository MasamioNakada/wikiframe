from chardet import detect
import os
from csv import Sniffer

import pandas as pd

def get_delimiter(path) -> str:
    white_list = [',', ';', ':', '|', '\t']
    if path[-3:] == 'csv':
        with open(path,'r') as file:
            firstline = file.readline()
            for sep in firstline:
                if sep in white_list:
                    return sep
            file.close()                      

def get_encoding(path):
    raw = open(path,'rb').read()
    encod = detect(raw)
    return encod['encoding']



class Load:
    def __init__(self, path:str):
        self.path = path
        self.labels = os.listdir(self.path)

    def load_from_csv(self):
        data_dict = {}
        for name in self.labels:
            full_path = f'./{self.path}/{name}'
            data_dict[name[:-4]] = pd.read_csv(full_path,sep=get_delimiter(full_path),encoding=get_encoding(full_path))
            return data_dict


