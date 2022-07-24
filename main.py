from load import Load
load = Load('in')
if __name__ == '__main__':
    data_dict = load.load_from_csv()
    print(data_dict.keys())


