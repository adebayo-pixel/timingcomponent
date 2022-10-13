import os
import pandas as pd
def path():
    parent_dir_path= '/hafeesdatadownload/kraken'
    dirs = os.listdir(parent_dir_path)
    exchange_name = []
    bid_ask_file = []
    for exchangefolder in dirs:

        exchange_name.append(exchangefolder)
    #print(exchange_name)

    for exchange in exchange_name:
        instrument_dir_path = os.path.join(parent_dir_path, exchange + '/')
        #print(instrument_dir_path)
        instrument_name_dirs = os.listdir(instrument_dir_path)

        #print(instrument_name_dirs)
        #print(len(instrument_name_dirs))
        for instrument_name_dir in instrument_name_dirs:
            files = os.path.join(instrument_dir_path, instrument_name_dir + '/')
            #print(files)
            file_list = os.listdir(files)
            for file_name in file_list:
                #print(file_list)
                bid_ask_file.append(os.path.join(files, file_name))

    df_list = []
    for file in bid_ask_file:
        #print(file)
        df = pd.read_csv(file)
        # print(df)
        df_list.append(df)
        #print(df_list)

    return bid_ask_file, instrument_name_dirs, df_list

path()







# final_df = df.append([df for df in df_list])
# final_df.to_csv('final.csv', index=False)
# print(final_df.to_csv)