from load import Load
load = Load('in')
if __name__ == '__main__':
    #print(delimiter('./in/Compra.csv'))
    #print(encoding('./in/Compra.csv'))
    data_dict = load.load_from_csv()
    print(data_dict)
    #print(data_dict.keys())


