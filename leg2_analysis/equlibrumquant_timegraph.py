from ask_and_bid_pricing import ask_and_bid,  bid_pricing,ask_pricing


import matplotlib.pyplot as plt
from reading_of_data import path
import pandas as pd
import datetime

from data_preprocessing import data_processing,getting_a_particular_coin

timeframe=[]
instrument_name_dirs = path()
def all_data_spreads(asks_lists,bids_lists):
    spreads=[]

    for ask,bid in zip(asks_lists,bids_lists):
        bid['quant_of_leg2'].sum()
        ask['quant_of_leg2'].sum()
        equilibrum_quant = min(bid['quant_of_leg2'].sum(), ask['quant_of_leg2'].sum())
        spreads.append(equilibrum_quant)
    return spreads
if __name__ == "__main__":
    asks_lists, bids_lists= ask_and_bid(getting_a_particular_coin(coin_name= 'ADAEUR'))
    spreads_for_eq_quantity_for_adaeur= all_data_spreads(asks_lists= asks_lists,bids_lists=bids_lists)

    asks_lists, bids_lists = ask_and_bid(getting_a_particular_coin(coin_name='XLTCZEUR'))
    spreads_for_eq_quantity_ltceur = all_data_spreads(asks_lists=asks_lists, bids_lists=bids_lists)

    asks_lists, bids_lists = ask_and_bid(getting_a_particular_coin(coin_name='BNTEUR'))
    spreads_for_eq_quantity_bnteur = all_data_spreads(asks_lists=asks_lists, bids_lists=bids_lists)

    asks_lists, bids_lists = ask_and_bid(getting_a_particular_coin(coin_name='SOLEUR'))
    spreads_for_eq_quantity_soleur = all_data_spreads(asks_lists=asks_lists, bids_lists=bids_lists)

    for time in instrument_name_dirs[1]:
        timestep = datetime.datetime.strptime(time, "%Y-%m-%dT%H_%M_%S_%fZ")
        timeframe.append(timestep)
    print(len(timeframe))
    #
    # plt.figure(figsize=(30, 10))
    #
    plt.plot(timeframe,spreads_for_eq_quantity_bnteur, label='eq_quantity_bnteur')
    plt.plot(timeframe, spreads_for_eq_quantity_ltceur, label='eq_quantity_ltceur')
    plt.plot(timeframe, spreads_for_eq_quantity_for_adaeur, label='eq_quantity_adaeur')
    plt.plot(timeframe,spreads_for_eq_quantity_soleur, label='eq_quantity_soleur')
    plt.ylabel('equilibrum quantity')
    plt.xlabel('time')
    plt.legend(loc='upper left')
    plt.show()




