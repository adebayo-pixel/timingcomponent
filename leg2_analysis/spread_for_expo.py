from ask_and_bid_pricing import bid_pricing, ask_pricing
from classify_ask_bid_pairs import ask_and_bid
import numpy as np
import matplotlib.pyplot as plt
from reading_of_data import path
import pandas as pd
import datetime
from ask_and_bid_pricing import ask_and_bid, bid_pricing, ask_pricing
from data_preprocessing import data_processing, getting_a_particular_coin


instrument_name_dirs = path()

timeframe=[]
def all_data_spreads_for_all_purchasable_quantity(asks_lists,bids_lists):
    number_of_datapoints = 10
    all_time_spread = []
    spreads = []

    leg2_quant_for_all_time=[]
    leg2quant = []
    for ask,bid in zip(asks_lists,bids_lists):
        bid['quant_of_leg2'].sum()
        ask['quant_of_leg2'].sum()
        equilibrum_quant= min(bid['quant_of_leg2'].sum(),ask['quant_of_leg2'].sum())

        for quantity in np.linspace(0, equilibrum_quant, number_of_datapoints)[1:-1]:
            ask_price_for_analysis = ask_pricing(quantity, asks_list=ask)
            bid_price_for_analysis = bid_pricing(quantity, bids_list=bid)
            our_spread = (ask_price_for_analysis - bid_price_for_analysis) / (
                    (ask_price_for_analysis + bid_price_for_analysis) / 2)
            spreads.append(our_spread)
            leg2quant.append(quantity)

        plt.plot(leg2quant, spreads, label='leg2 vs spread for btceur')
        plt.ylabel('spreads')
        plt.xlabel('leg2quant')
        plt.legend(loc='upper left')
        plt.show()




            # leg2quant_set=pd.DataFrame(leg2quant_set)
    return spreads, leg2quant


if __name__ == "__main__":
    # asks_lists, bids_lists, = ask_and_bid(getting_a_particular_coin(coin_name='ADAEUR'))
    # spreads_for_adaeur=all_data_spreads_for_all_purchasable_quantity(asks_lists=asks_lists, bids_lists= bids_lists)

    #asks_lists, bids_lists, = ask_and_bid(getting_a_particular_coin(coin_name='XXBTZEUR'))
    #spreads_for_btc=all_data_spreads_for_all_purchasable_quantity(asks_lists=asks_lists, bids_lists=bids_lists)
    #
    #asks_lists, bids_lists, = ask_and_bid(getting_a_particular_coin(coin_name='APEEUR'))
    #spreads_for_apeeur=all_data_spreads_for_all_purchasable_quantity(asks_lists=asks_lists, bids_lists=bids_lists)
    #
    asks_lists, bids_lists, = ask_and_bid(getting_a_particular_coin(coin_name='XXBTZEUR'))
    spreads_for_algoeur=all_data_spreads_for_all_purchasable_quantity(asks_lists=asks_lists, bids_lists=bids_lists)
    print(spreads_for_algoeur)


    # plt.plot(leg2_quant_for_all_time, spreads_for_btc, label='leg2 vs spread for btceur')
    # plt.plot(leg2_quant_for_all_time, spreads_for_apeeur, label='leg2 vs spread for apeeur')
    # plt.plot(leg2_quant_for_all_time,spreads_for_algoeur, label='leg2 vs spread for algoeur')







