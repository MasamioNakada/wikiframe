from wikiframe.extractor import Extractor
from wikiframe.cow_say import Say 
import pandas as pd
import numpy as np

extract = Extractor('in')
say = Say('Hello World')

def val_date(col) -> bool:
    key = ["date", "times", "order_approved_at"]
    for name in key:
        return name in col

def find_date(df):
    cols = list(df.columns)
    for col in cols:
        if val_date(col):
            df[f"{col}"] = pd.to_datetime(df[f"{col}"], infer_datetime_format=True)
    return df

def col_lower(df):
    for name in df.dtypes.to_dict().keys():
        if df.dtypes.to_dict()[name] == np.dtype(object):
            df[name] = df[name].str.upper()
    return df

if __name__ == '__main__':
    data_dict = extract.extract_from_csv([col_lower, find_date])
    #data_dict2 = extract.extract_from_csv()
    print(data_dict['Clientes'].head())
    #print(data_dict2['Clientes'].head())
    say.cow_says_good()
    say.cow_says_error()