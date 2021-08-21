from datetime import datetime
from numpy import datetime64
import requests
import csv
from configparser import ConfigParser
import pandas as pd


configpath = '....(Path)\\Config\\Configuration.cfg'
config = ConfigParser()
config.read(configpath)

#Get the basic settings from config file

#API Key
Apikey = config['APISETTING']['API_KEY']
#Companies
Equity_List = config['APISETTING']['Equity'].split(',')
#Type of data
Function = config['APISETTING']['Function']
#Data size
OutputSize = config['APISETTING']['OutputSize']




#Get data with API key 
def get_data(FUNCTION, EQUITY, OUTPUTSIZE, APIKEY):
    url = str('https://www.alphavantage.co/query?function=' + FUNCTION + \
                                                    '&symbol=' + EQUITY + \
                                                '&outputsize=' + OUTPUTSIZE + \
                                                '&apikey=' + APIKEY + '&datatype=csv')
    with requests.Session() as s:
        download = s.get(url)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        DATA = pd.DataFrame(cr)
    return DATA

#Format / Clean raw data
def format_data(DATA):
    DATA.columns = DATA.iloc[0]
    DATA = DATA.drop(DATA.index[0])
    return DATA

#Setting the data types for all column.
def set_dtypes(DATA):
    DATA['timestamp'] = pd.to_datetime(DATA['timestamp'])
    DATA[['open', 'low', 'high', 'close']] = DATA[['open', 'low', 'high', 'close']].astype(float)
    DATA['volume'] = DATA['volume'].astype(int)
    return DATA

#Gather all the data sets and its company labels into a dictionary.
#Use the functions created above to execute main sript at the same time.  
data_dict = {}
for Equity in Equity_List:
    data_dict.update({Equity : set_dtypes(format_data(get_data(Function, Equity, OutputSize, Apikey)))})

#The resulting data will be used on a visualization script.
#This python file will be imported into Data Visualization script as a module.
