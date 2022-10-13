import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
import math
from spreads_for_actual_quantity import all_data_spreads
from data_preprocessing import data_processing,getting_a_particular_coin
from classify_ask_bid_pairs import ask_and_bid
from reading_of_data import path
import datetime
import numpy as np
import csv

import matplotlib.pyplot as plt
#from classify_ask_bid_pairs import ask_and_bid
import statistics


instrument_name_dirs = path()
def exp_inte(asks_lists,bids_lists):
    spread_for_bids, quantities_on_bid_side = all_data_spreads(asks_lists,bids_lists)
    appending_exp_integral_result_for_timeframes = []

    for each_list_in_spread,each_list_in_leg2quant_set in zip(spread_for_bids, quantities_on_bid_side):
        appending_exp_integral_result_for_each_timeframes = []

        for x,y, j, t in zip(each_list_in_spread, each_list_in_spread[1:], each_list_in_leg2quant_set, each_list_in_leg2quant_set[1:]):

            exp_integral_result = ((math.exp(-x)+ math.exp(-y))/2)* (t - j)

            appending_exp_integral_result_for_each_timeframes.append(exp_integral_result)
        #exponential_result=sum(appending_exp_integral_result_for_each_timeframes)

        appending_exp_integral_result_for_timeframes.append(appending_exp_integral_result_for_each_timeframes)
    actual_exp_result= [sum(x) for x in appending_exp_integral_result_for_timeframes]
    #print(len(actual_exp_result))

    return statistics.mean(actual_exp_result), statistics.stdev(actual_exp_result), min(actual_exp_result), max(actual_exp_result)

data_for_all_instrument, names_of_instrument = data_processing()
names_of_instrument=names_of_instrument.tolist()
#list_to_remove = ['tETHEUR']
#names_of_instrument = list(set(names_of_instrument) - set(list_to_remove))
#names_of_instrument=sorted(names_of_instrument)
#print(names_of_instrument)
df = pd.DataFrame()
for all_instrument in names_of_instrument:
    print(all_instrument)
    asks_lists,bids_lists, = ask_and_bid(getting_a_particular_coin(coin_name= all_instrument))

    data = exp_inte(asks_lists,bids_lists)

    print(data)

    df = df.append({'instrument': all_instrument, 'mean': data[0], 'std': data[1], 'min': data[2], 'max': data[3]},
                   ignore_index=True)

df.to_csv('kra_bid.csv', index=False)
















# if __name__ == "__main__":
#     asks_lists,bids_lists, = ask_and_bid(getting_a_particular_coin(coin_name= 'TRIBEEUR'))
#     data = exp_inte(asks_lists,bids_lists)
#
#     timeframe = []
#     for time in instrument_name_dirs[1]:
#         timestep = datetime.datetime.strptime(time, "%Y-%m-%dT%H_%M_%S_%fZ")
#         timeframe.append(timestep)
#     #print(timeframe)
#
#     plt.figure(figsize=(20, 6))
#     plt.plot(timeframe,data, label='exp_integral_ATOM_bid_quantity')
#     plt.ylabel('exp_result')
#     plt.xlabel('time')
#     plt.legend(loc='upper left')
#     plt.show()