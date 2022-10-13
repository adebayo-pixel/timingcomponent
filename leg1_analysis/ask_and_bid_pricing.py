from classify_ask_bid_pairs import ask_and_bid
from data_preprocessing import data_processing,getting_a_particular_coin



def bid_pricing(quantity, bids_list):


    leftover_quantity = float(quantity)
    total = 0
    i = 0
    while leftover_quantity > 0:
        if leftover_quantity <= float(bids_list.iloc[i]['quantity']):
            total += leftover_quantity * float(bids_list.iloc[i]['price'])
            break
        else:
            leftover_quantity -= float(bids_list.iloc[i]['quantity'])
            total += (float(bids_list.iloc[i]['quantity']) * float(bids_list.iloc[i]['price']))
            i += 1
    return total/quantity

if __name__ == "__main__":


    #coin= ask_and_bid(getting_a_particular_coin(coin_name= 'ATOMEUR'))
    bids_lists, asks_lists= ask_and_bid(getting_a_particular_coin(coin_name= '1INCHEUR'))
    bids_price= bid_pricing(quantity=0.1, bids_list=bids_lists[1])
    print(bids_price)





def ask_pricing(quantity, asks_list):
    leftover_quantity = float(quantity)
    total = 0
    i = 0
    while leftover_quantity > 0:
        if leftover_quantity <= float(asks_list.iloc[i]['quantity']):
            total += leftover_quantity * float(asks_list.iloc[i]['price'])
            break
        else:
            leftover_quantity -= float(asks_list.iloc[i]['quantity'])
            total += (float(asks_list.iloc[i]['quantity']) * float(asks_list.iloc[i]['price']))
            i += 1
    return total/quantity

if __name__ == "__main__":
    bids_lists, asks_lists = ask_and_bid(getting_a_particular_coin(coin_name='1INCHEUR'))
    asks_price = ask_pricing(quantity=0.1, asks_list=asks_lists[0])
    print(asks_price)