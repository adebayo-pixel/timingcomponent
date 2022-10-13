from ask_and_bid_pricing import ask_and_bid,  bid_pricing,ask_pricing


import matplotlib.pyplot as plt
from reading_of_data import path
import pandas as pd
import datetime

from data_preprocessing import data_processing,getting_a_particular_coin


instrument_name_dirs = path()
def all_data_spreads(bids_lists, asks_lists, quantity:float)-> list[float]:
    spreads=[]

    for ask,bid in zip(asks_lists,bids_lists):
        ask_price_for_analysis = ask_pricing(quantity, asks_list=ask)
        bid_price_for_analysis = bid_pricing(quantity, bids_list=bid)
        our_spread = (ask_price_for_analysis - bid_price_for_analysis) / (
                (ask_price_for_analysis + bid_price_for_analysis) / 2)
        spreads.append(our_spread)
    return spreads
if __name__ == "__main__":
    bids_lists, asks_lists= ask_and_bid(getting_a_particular_coin(coin_name= 'ATOMEUR'))
    spreads_for_quantity_0_1= all_data_spreads(bids_lists=bids_lists, asks_lists= asks_lists,quantity=0.1)
    bids_lists, asks_lists = ask_and_bid(getting_a_particular_coin(coin_name='ATOMEUR'))
    spreads_for_quantity_10 = all_data_spreads(bids_lists=bids_lists, asks_lists=asks_lists, quantity=10000)
    print(spreads_for_quantity_0_1)

    timeframe = []
    for time in instrument_name_dirs[1]:
        timestep = datetime.datetime.strptime(time, "%Y-%m-%dT%H_%M_%S_%fZ")
        timeframe.append(timestep)
    print(timeframe)

    plt.figure(figsize=(20, 6))

    plt.plot(timeframe, spreads_for_quantity_0_1, label='quantity_0_1')
    plt.plot(timeframe,spreads_for_quantity_10, label='quantity_10')
    plt.ylabel('spread')
    plt.xlabel('time')
    plt.legend(loc='upper left')
    plt.show()




