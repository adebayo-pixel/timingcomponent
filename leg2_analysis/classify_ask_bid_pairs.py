from data_preprocessing import data_processing,getting_a_particular_coin

def ask_and_bid(analysis_coin):
#analysis_coin = getting_a_particular_coin(coin_name='1INCHEUR')

    ask_bid_pairs=[]
    for i in range(0, len(analysis_coin), 2):
        ask_bid_pairs.append((analysis_coin[i], analysis_coin[i+1]))


    asks_list = [ask_bid_pair[0] for ask_bid_pair in ask_bid_pairs]
    #print(asks_list)
    bids_list = [ask_bid_pair[1] for ask_bid_pair in ask_bid_pairs]
    return asks_list, bids_list

asks_lists, bids_lists = ask_and_bid(getting_a_particular_coin(coin_name= 'TRIBEEUR'))

#print(asks_lists)
#print(bids_lists)

