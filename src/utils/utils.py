import pandas as pd

def get_df(dataset : str, test=False, output=False): 
    test_, input_ = "example-set", "output"
    if not output:
        input_ = 'input'
    if test:
        test_ = 'test-set'
    main_dir = "C2C-2024-DataSet/DataSets"
    df = pd.read_csv("{}/{}/{}_{}.csv".format(main_dir, test_, input_, dataset))
    return df