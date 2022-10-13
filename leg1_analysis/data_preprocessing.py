import numpy
from reading_of_data import path
import numpy as np

def data_processing():
    df_list=path()

    instruments= []
    data_for_all_instrument=[]
    names_of_instrument=[]

    for instrument_name in df_list[2]:
        data_for_all_instrument.append(instrument_name.drop(columns='Unnamed: 0'))
        instruments.append(instrument_name['instrument'].unique())
    #print(data_for_all_instrument)
    for instrument in instruments:
        #print(instrument)
        names_of_instrument.append(instrument)
    names_of_instrument= np.unique(names_of_instrument)
    #print(names_of_instrument)
    return data_for_all_instrument, names_of_instrument

data_processing()


data_for_all_instrument,  names_of_instrument = data_processing()


def getting_a_particular_coin(coin_name):
    analysis_coin = [coin for coin in data_for_all_instrument if coin['instrument'].unique() == (coin_name)]
    return analysis_coin

if __name__ == "__main__":

    getting_a_particular_coin(coin_name= 'ATOMEUR')
#print(getting_a_particular_coin(coin_name='ATOMEUR'))
# ask_bid_pairs=[]
# for i in range(0, len(df_list), 2):
#     ask_bid_pairs.append((df_list[i], df_list[i+1]))
#
# #print(ask_bid_pairs[1])
# bids_list = [ask_bid_pair[0] for ask_bid_pair in ask_bid_pairs]
# print(bids_list[1])
#
# def bid_pricing(quantity, bids_list):
#     leftover_quantity = float(quantity)
#     total = 0
#     i = 0
#     while leftover_quantity > 0:
#         if leftover_quantity <= float(bids_list.iloc[i]['quantity']):
#             total += leftover_quantity * float(bids_list.iloc[i]['price'])
#             break
#         else:
#             leftover_quantity -= float(bids_list.iloc[i]['quantity'])
#             total += (float(bids_list.iloc[i]['quantity']) * float(bids_list.iloc[i]['price']))
#             i += 1
#     return total/quantity
#
# print(bid_pricing(quantity=200, bids_list=bids_list[1]))
#
#
# asks_list = [ask_bid_pair[1] for ask_bid_pair in ask_bid_pairs]
# print(asks_list[2])
#
# def ask_pricing(quantity, asks_list):
#     leftover_quantity = float(quantity)
#     total = 0
#     i = 0
#     while leftover_quantity > 0:
#         if leftover_quantity <= float(asks_list.iloc[i]['quantity']):
#             total += leftover_quantity * float(asks_list.iloc[i]['price'])
#             break
#         else:
#             leftover_quantity -= float(asks_list.iloc[i]['quantity'])
#             total += (float(asks_list.iloc[i]['quantity']) * float(asks_list.iloc[i]['price']))
#             i += 1
#     return total/quantity
#
# print(ask_pricing(quantity=200, asks_list=asks_list[1]))