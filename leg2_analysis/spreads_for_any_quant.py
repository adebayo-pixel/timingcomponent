from ask_and_bid_pricing import  bid_pricing,ask_pricing
from classify_ask_bid_pairs import ask_and_bid
import numpy as np
import matplotlib.pyplot as plt
from reading_of_data import path
import pandas as pd
import datetime
from ask_and_bid_pricing import ask_and_bid,  bid_pricing,ask_pricing
from data_preprocessing import data_processing,getting_a_particular_coin

number_of_datapoints = 1000
instrument_name_dirs = path()
def all_data_spreads_for_any_purchasable_quantity():

    bid_sum=[]
    ask_sum=[]
    spreads=[]
    leg2quant_set = []

    for bid in bids_lists:
        x=[bid['quant_of_leg2'].sum(), bid['price'].sum()]
        bid_sum.append(x)
    #print(bid_sum)
    list_of_leg2quant_bid= list(list(zip(*bid_sum))[0])     #needed to find the sum of all the leg2quantity on bid side
    sum_of_all_bid = sum(list_of_leg2quant_bid)                 #the sum of all the leg2quantity on bid side
    for ask in asks_lists:
        y=[ask['quant_of_leg2'].sum(), ask['price'].sum()]
        ask_sum.append(y)
    list_of_leg2quant_ask = list(list(zip(*ask_sum))[0])
    sum_of_all_ask= sum(list_of_leg2quant_ask)
    equilibrum_quant=min(sum_of_all_ask, sum_of_all_bid)

    ask_sum = pd.DataFrame(ask_sum)
    ask_sum = ask_sum.rename(columns={0: 'quant_of_leg2', 1:'price'})

    bid_sum = pd.DataFrame(bid_sum)
    bid_sum = bid_sum.rename(columns={0: 'quant_of_leg2', 1:'price'})

    for quantity in np.linspace(0, equilibrum_quant, number_of_datapoints)[1:-1]:
        ask_price_for_analysis = ask_pricing(quantity, asks_list=ask_sum)
        bid_price_for_analysis = bid_pricing(quantity, bids_list=bid_sum)
        our_spread = (ask_price_for_analysis - bid_price_for_analysis) / (
                (ask_price_for_analysis + bid_price_for_analysis) / 2)
        spreads.append(our_spread)
        leg2quant_set.append(quantity)
    print(spreads)

    plt.plot(leg2quant_set, spreads, label='leg2 vs spread for btceur')
    plt.ylabel('spreads')
    plt.xlabel('leg2quant')
    plt.legend(loc='upper left')
    plt.show()
    return spreads, leg2quant_set







#if __name__ == "__main__":
asks_lists,bids_lists, = ask_and_bid(getting_a_particular_coin(coin_name='XXBTZEUR'))
all_data_spreads_for_any_purchasable_quantity()
#print(spreads_for_1inch)
#print(len(spreads_for_1inch))

    # timeframe = []
    # for time in instrument_name_dirs[1]:
    #     timestep = datetime.datetime.strptime(time, "%Y-%m-%dT%H_%M_%S_%fZ")
    #     timeframe.append(timestep)
    # print(timeframe)
    #
    # plt.figure(figsize=(30, 10))
    #
    # plt.plot(timeframe,spreads_for_quantity_10_bitcoin, label='quantity_10_btc')
    # plt.plot(timeframe, spreads_for_quantity_10_atom, label='quantity_10_atom')
    # plt.plot(timeframe, spreads_for_quantity_10_ape, label='quantity_10_ape')
    # plt.ylabel('spread')
    # plt.xlabel('time')
    # plt.legend(loc='upper left')
    # plt.show()




