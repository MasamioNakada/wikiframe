from chardet import detect
import os
from csv import Sniffer
import warnings

import pandas as pd

class Extractor:
    def __init__(self, path:str):
        self.path = path
        self.labels = os.listdir(self.path) 

    def get_encoding(self,full_path) -> str:
        raw = open(full_path,'rb').read()
        encod = detect(raw)
        return encod['encoding']

    def get_delimiter(self,full_path) -> str:
        white_list = [',', ';', ':', '|', '\t']
        if self.path[-3:] == 'csv':
            with open(full_path, mode='r',encoding=self.get_encoding(full_path)) as file:
                firstline = file.readline()
                for sep in firstline:
                    if sep in white_list:
                        print(sep)
                file.close()  
        
    def extract_from_csv(self):
        data_dict = {}

        for name in self.labels:
            if name[-3:] == 'csv': 
                full_path = f'./{self.path}/{name}'
                data_dict[name[:-4]] = pd.read_csv(full_path,sep=self.get_delimiter(full_path),encoding=self.get_encoding(full_path),engine='python')
            else:
                warnings.warn(message = f'{name} is not a csv file, ingoring', category=UnicodeWarning, stacklevel=2)
        return data_dict


