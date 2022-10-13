import numpy
from reading_of_data import path
import numpy as np

def data_processing():
    #global data_for_all_instrument
    df_list=path()

    instruments= []
    data_for_all_instrument = []
    names_of_instrument=[]

    for instrument_name in df_list[2]:

        if instrument_name.empty==True:
            pass
        else:

            instrument_name['quant_of_leg2'] = instrument_name['price'] * instrument_name['quantity']

            instrument_name['quant_of_leg2']=instrument_name['quant_of_leg2'].abs()
            instrument_name['cum_sum'] = instrument_name['quant_of_leg2'].cumsum()
            #print(instrument_name)

            data_for_all_instrument.append(instrument_name.drop(columns='Unnamed: 0'))
            #print(data_for_all_instrument)
            instruments.append(instrument_name['instrument'].unique())

    for instrument in instruments:
        #print(instrument)
        names_of_instrument.append(instrument)
    names_of_instrument= np.unique(names_of_instrument)
    #print(names_of_instrument)
    return data_for_all_instrument,names_of_instrument

#print(data_processing())




def getting_a_particular_coin(coin_name):
    data_for_all_instrument, names_of_instrument = data_processing()
    #print(names_of_instrument)
    #print(data_for_all_instrument)
    analysis_coin = [coin for coin in data_for_all_instrument if coin['instrument'].unique() == (coin_name)]
    return analysis_coin

if __name__ == "__main__":

    print(getting_a_particular_coin(coin_name= 'tETHEUR'))
