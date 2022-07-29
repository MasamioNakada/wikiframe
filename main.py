import encodings
from wikiframe.extractor import Extractor
from wikiframe.utils import export_csv
from transform import col_lower, find_date, col_upp,dupli_id,date_order_val

import pandas as pd
import numpy as np

extract = Extractor('in')

func_list = [col_lower , find_date, dupli_id]

func_custom = {
   'olist_customers_dataset' : col_upp,
    'order_delta' :date_order_val
}

encoding= {
     'review_delta.csv':'utf-8'
}

if __name__ == '__main__':
    data_dict = extract.extract_from_csv(sep=[','],encoding=encoding,func=func_list,func_custom=func_custom)
    export_csv(data_dict,'out')
