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

    def __get_encoding(self,full_path,encoding={}) -> str:
        '''
        This function will detect the encoding of the .csv file.

        Parameters:
        -----------
        full_path : The full path of the file.

        Returns:
        --------
        encoding : The encoding of the file.
        '''
        if len(encoding) != 0:
            for enc in encoding.keys():
                if enc in full_path:
                    print(f'retornando {encoding[enc]}')
                    return encoding[enc]
                
        raw = open(full_path,'rb').read()
        encod = detect(raw)
        if encod['confidence'] <= 0.7:
            warnings.warn(message = f'Chardet could not resolve encoding by {full_path}, encoding default -> utf-8', category=UnicodeWarning, stacklevel=2)
            return 'utf-8'
        else:
            return encod['encoding']

    def __get_delimiter(self,full_path,sep=[]) -> str:
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
        white_list = [',',';', ':', '|', '\t']
        if sep == str:
            white_list.append(sep)
        if len(sep) != 0:
            for s in sep:
                white_list.append(s)
        if self.path[-3:] == 'csv':
            with open(full_path, mode='r',encoding=self.get_encoding(full_path)) as file:
                firstline = file.readline()
                for sep in firstline:
                    if sep in white_list:
                        return sep
                    else:
                        warnings.warn(message = 'can not find a standard delimiter, using default delimiter ","', category=UnicodeWarning, stacklevel=2)
                file.close()  
        
    def extract_from_csv(self, sep ={}, encoding ={} ,func = [],func_custom ={}, verbose = False) -> dict:
        '''
        This function will extract all the csv files in the folder and convert them to a dictionary of dataframe.

        Parameters:
        -----------
        sep : Especifies the delimiter of the csv file. (default [',',';', ':', '|', '\t'])
        encoding : Especifies the encoding of the csv file. (if not especified, it will be detected automatically)
        func : A list of functions that will be applied to the dataframe. (e.g. [func1, func2, func3])
        func_custom : A dictionary of functions that will be applied to the especific dataframe. (e.g. {'dataframe_1':[func1,func2], 'dataframe2':func3})
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

        if type(sep) == dict:
            sep = list(sep.values())

        for name in self.labels:
            if name[-3:] == 'csv':
                full_path = f'{self.path}/{name}'
                data_dict[name[:-4]] = read_csv(full_path,sep=self.__get_delimiter(full_path,sep),encoding=self.__get_encoding(full_path,encoding),engine='python')
            else:
                warnings.warn(message = f'{name} is not a csv file, ingoring', category=UnicodeWarning, stacklevel=2)

        if callable(func):
            for key in data_dict.keys():
                data_dict[key] = func(data_dict[key])
                if verbose == True:
                    print(f'{key} is transformed')

        if type(func) == list:
            if len(func) != 0:
                for func_name in func:
                    for key in data_dict.keys():
                        data_dict[key] = func_name(data_dict[key])
                        if verbose == True:
                            print(f'{key} is transformed')
        
        if len(func_custom) != 0:
            for name in func_custom.keys():
                if callable(func_custom[name]):
                    data_dict[name] = func_custom[name](data_dict[name])
                else:
                    for func in func_custom[name]:
                        data_dict[name] = func(data_dict[name])
        return data_dict



        


