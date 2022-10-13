from classify_ask_bid_pairs import ask_and_bid
from data_preprocessing import data_processing,getting_a_particular_coin



def bid_pricing(quantity, bids_list):


    leftover_quantity = float(quantity)
    total = 0
    i = 0
    while leftover_quantity > 0:
        if leftover_quantity <= float(bids_list.iloc[i]['cum_sum']):
            total += leftover_quantity * float(bids_list.iloc[i]['price'])
            break
        else:
            leftover_quantity -= float(bids_list.iloc[i]['cum_sum'])
            total += (float(bids_list.iloc[i]['cum_sum']) * float(bids_list.iloc[i]['price']))
            i += 1
    return total/quantity





def ask_pricing(quantity, asks_list):
    leftover_quantity = float(quantity)
    total = 0
    i = 0
    while leftover_quantity > 0:
        if leftover_quantity <= float(asks_list.iloc[i]['cum_sum']):
            total += leftover_quantity * float(asks_list.iloc[i]['price'])
            break
        else:
            leftover_quantity -= float(asks_list.iloc[i]['cum_sum'])
            total += (float(asks_list.iloc[i]['cum_sum']) * float(asks_list.iloc[i]['price']))
            i += 1
    return total/quantity

if __name__ == "__main__":
    asks_lists, bids_lists = ask_and_bid(getting_a_particular_coin(coin_name='XLTCZEUR'))
    asks_price = ask_pricing(quantity=0.1, asks_list=asks_lists[0])
    print(asks_price)
