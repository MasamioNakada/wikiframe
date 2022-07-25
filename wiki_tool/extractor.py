import os
import warnings

from pandas import read_csv
from chardet import detect

class Extractor:
    '''
    This tool will help you to extract .csv files from folder to a dictionary of dataframe.

    Parameters
    ----------
    path : Put the path of the folder you want to extract.

    Notes:
    ------
    Returns a dictionary of dataframe.

    Only csv files will be extracted.

    Encoding will be detected automatically.

    Delimiter will be detected automatically.

    Examples:
    ---------
    >>> from wiki-tools import Extractor
    >>> extract = Extractor('in')
    >>> data_dict = extract.extract_from_csv()
    >>> print(data_dict.keys()) # will print the name of the dataframe
    
    '''
    def __init__(self, path:str):
        self.path = path
        self.labels = os.listdir(self.path) 

    def get_encoding(self,full_path) -> str:
        '''
        This function will detect the encoding of the .csv file.

        Parameters:
        -----------
        full_path : The full path of the file.

        Returns:
        --------
        encoding : The encoding of the file.
        '''
        raw = open(full_path,'rb').read()
        encod = detect(raw)
        return encod['encoding']

    def get_delimiter(self,full_path) -> str:
        '''
        This function will detect the delimiter of the .csv file.
        
        Parameters:
        -----------
        full_path : The full path of the file.

        Returns:
        --------
        delimiter : The delimiter of the file.

        Notes:
        ------
        Standard delimiter is (',', ';', ':', '|', '\t').
        If the delimiter is not detected, it will return ','.

        '''
        white_list = (',', ';', ':', '|', '\t')
        if self.path[-3:] == 'csv':
            with open(full_path, mode='r',encoding=self.get_encoding(full_path)) as file:
                firstline = file.readline()
                for sep in firstline:
                    if sep in white_list:
                        return sep
                    else:
                        warnings.warn(message = 'can not find a standard delimiter, using default delimiter ","', category=UnicodeWarning, stacklevel=2)
                file.close()  
        
    def extract_from_csv(self, func, verbose = False) -> dict:
        '''
        This function will extract all the csv files in the folder and convert them to a dictionary of dataframe.

        Parameters:
        -----------
        func : A list of functions that will be applied to the dataframe. (e.g. [func1, func2, func3])
        verbose : If True, will print the name of the dataframe that is transformed. (default False)

        Returns:
        --------
        data_dict : A dictionary of dataframe.

        Notes:
        ------
        The order of the dataframe in the dictionary is the same as the order of the csv files in the folder.
        func could be a list of functions or a single function.

        Examples:
        ---------
        >>> from wiki-tools import Extractor
        >>> extract = Extractor('in')
        >>> data_dict = extract.extract_from_csv([func1, func2, func3],True)
        
        '''
        data_dict = {}

        for name in self.labels:
            if name[-3:] == 'csv': 
                full_path = f'./{self.path}/{name}'
                data_dict[name[:-4]] = read_csv(full_path,sep=self.get_delimiter(full_path),encoding=self.get_encoding(full_path),engine='python')
            else:
                warnings.warn(message = f'{name} is not a csv file, ingoring', category=UnicodeWarning, stacklevel=2)

        if callable(func):
            for key in data_dict.keys():
                data_dict[key] = func(data_dict[key])
                if verbose == True:
                    print(f'{key} is transformed')
            return data_dict

        if type(func) == list:
            if len(func) != 0:
                for func_name in func:
                    for key in data_dict.keys():
                        data_dict[key] = func_name(data_dict[key])
                        if verbose == True:
                            print(f'{key} is transformed')
                return data_dict

        


