import pandas as pd
import math
from spread_for_expo  import all_data_spreads_for_all_purchasable_quantity
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
    spreads, leg2quant = all_data_spreads_for_all_purchasable_quantity(asks_lists,bids_lists)
    appending_exp_integral_result_for_timeframes=[]
    spreads_set= [spreads[x:x+8] for x in range(0, len(spreads), 8)]
    #print(spreads_set)
    leg2quant_set = [leg2quant[x:x+8] for x in range(0, len(leg2quant), 8)]
    for each_list_in_spread,each_list_in_leg2quant_set in zip(spreads_set, leg2quant_set):

        for x,y, j, t in zip(each_list_in_spread, each_list_in_spread[1:], each_list_in_leg2quant_set, each_list_in_leg2quant_set[1:]):
            exp_integral_result= ((math.exp(-x)+ math.exp(-y))/2)* (t - j)

            appending_exp_integral_result_for_timeframes.append(exp_integral_result)
    exp_result = [appending_exp_integral_result_for_timeframes[x:x + 7] for x in range(0, len(appending_exp_integral_result_for_timeframes), 7)]
    #print(exp_result)
    actual_exp_result = [sum(x) for x in exp_result]
    #print(statistics.mean(actual_exp_result), statistics.stdev(actual_exp_result), min(actual_exp_result), max(actual_exp_result))


    return statistics.mean(actual_exp_result), statistics.stdev(actual_exp_result), min(actual_exp_result), max(actual_exp_result)


data_for_all_instrument, names_of_instrument = data_processing()

df = pd.DataFrame()
for all_instrument in names_of_instrument:
    print(all_instrument)
    asks_lists,bids_lists, = ask_and_bid(getting_a_particular_coin(coin_name= all_instrument))

    data = exp_inte(asks_lists,bids_lists)

    print(data)

    df = df.append({'instrument': all_instrument, 'mean': data[0], 'std': data[1], 'min': data[2], 'max': data[3]},
                   ignore_index=True)

df.to_csv('bitfinex.csv', index=False)

    #print(exp_inte(bids_lists, asks_lists))


    # m, s, mi, ma, i = [], [], [], [],[]
    # m.append(mean), s.append(std), mi.append(min), ma.append(max), i.append(all_instrument)
    # df = pd.DataFrame({'instrument': i, 'mean': mean, 'std': std, 'min': min, 'max': max})
    # df.to_csv('file_name.csv', index=False)
    # print(exp_inte(bids_lists, asks_lists))


# instrument_df = pd.DataFrame(names_of_instrument, columns=['instrument'], index=None)
    # df = pd.DataFrame(data, columns=['mean', 'Std', 'Min', 'Max'], index=None)
    # dataframe = pd.concat([instrument_df, df],  axis=1, join='inner')
    # dataframe.to_csv('bitstamp.csv', index=False)




















#print(exp_integral)
# tj=[exp_integral[x:x+7] for x in range(0, len(exp_integral), 7)]
# print(tj)
# res= [sum(x) for x in tj]
# print(statistics.mean(res), statistics.stdev(res), min(res), max(res))

# timeframe = []
# for time in instrument_name_dirs[1]:
#     timestep = datetime.datetime.strptime(time, "%Y-%m-%dT%H_%M_%S_%fZ")
#     timeframe.append(timestep)
#     #print(timeframe)
#
# plt.figure(figsize=(20, 6))
# plt.plot(timeframe,actual_exp_result, label='exp_integral_APEEUR')
# plt.ylabel('spread')
# plt.xlabel('time')
# plt.legend(loc='upper left')
# plt.show()