#Imports
import requests
from pycoingecko import CoinGeckoAPI
from datetime import datetime
import csv
import time

#User defines
p_key_ethermine1='03e55fd61796743daa47399fc3cffea19b336db6'
p_key_ethermine2='0x39ebc5649481087d5a5632da25ffd3e89db5dc36'




def payoutData_API(ethermin_key):


    cg = CoinGeckoAPI()
    data=[];
    api_path_ethermine='https://api.ethermine.org/miner/'+ethermin_key+'/payouts'
    r_ethermine_payouts=requests.get(api_path_ethermine)
    r_etehrmine_jsonData=r_ethermine_payouts.json()

    for i in range(len(r_etehrmine_jsonData['data'])-1,0,-1):
        ts=r_etehrmine_jsonData['data'][i]['paidOn']
        tx_date=datetime.utcfromtimestamp(ts).strftime('%d-%m-%Y') #time coversion
        coin_price_date=cg.get_coin_history_by_id('ethereum',tx_date)['market_data']['current_price']['eur']
        time.sleep(1)
        ether_amount=r_etehrmine_jsonData['data'][i]['amount']/1e18
        tx_hash=r_etehrmine_jsonData['data'][i]['txHash']
        value_payout=ether_amount*coin_price_date
        data.append({'Transaction_Number':len(r_etehrmine_jsonData['data'])-i,'Transaction_Date':tx_date,'TxHash':tx_hash,'Ether_Amount':ether_amount,'coin_price':coin_price_date,'Value':value_payout})

    # write a row to the csv file
    file_path='./CSV_'+ethermin_key + ".csv"
    # open the file in the write mode
    f = open(file_path, 'w')
    # create the csv writer
    keys=data[0].keys()
    writer = csv.DictWriter(f,keys)
    writer.writeheader()
    writer.writerows(data)
    f.close()

payoutData_API(p_key_ethermine1)
payoutData_API(p_key_ethermine2)

