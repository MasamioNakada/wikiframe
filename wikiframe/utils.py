from os import makedirs

from requests import head


def export_csv(dict:dict,folder:str,sep=',',index=True,header=True) -> str:
    '''This function will export a dictionary of dataframe to csv in a folder.
    
    Parameters:
    -----------
    dict : The dictionary of dataframe.
    folder: The folder that the csv files will be exported to.
    sep: The delimiter of the csv file export. (default ',')    
    index: If True, the index will be exported. (default True)
    header: If True, the header will be exported. (default True)
    '''
    makedirs(folder,exist_ok=True)
    for key in dict.keys():
        dict[key].to_csv(f'{folder}/{key}.csv',sep=sep)
    return print(f"{len(dict.keys())} datasets exportados correctamente en {folder} ")

