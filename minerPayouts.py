#Imports
import requests
from pycoingecko import CoinGeckoAPI
from datetime import datetime
#User defines
p_key_ethermine='03e55fd61796743daa47399fc3cffea19b336db6'
file_path='./'
cg = CoinGeckoAPI()
data=[];

api_path_ethermine='https://api.ethermine.org/miner/'+p_key_ethermine+'/payouts'
r_ethermine_payouts=requests.get(api_path_ethermine)
r_etehrmine_jsonData=r_ethermine_payouts.json()
for i in range(len(r_etehrmine_jsonData['data'])):
    ts=r_etehrmine_jsonData['data'][i]['paidOn']
    tx_date=datetime.utcfromtimestamp(ts).strftime('%d-%m-%Y') #time coversion
    coin_price_date=cg.get_coin_history_by_id('ethereum',tx_date)
    ether_amount=r_etehrmine_jsonData['data'][i]['amount']/1e18
    tx_hash=r_etehrmine_jsonData['data'][i]['txHash']
    value_payout=ether_amount*ether_amount
    data.append({'Transaction_Number':i,'Transaction_Date':tx_date,'TxHash':tx_hash,'Ether_Amount':ether_amount,'coin_price':coin_price_date,'Value':value_payout})

print(data)

