#Import data preparation script.
import GetData
#Seaborn for visualization. 
%matplotlib inline
from matplotlib import pyplot as plt
import numpy as np
from matplotlib import cm

#Show data from GetData module. 
#Use the resulting data as visualization data. 
datab = GetData.data_dict
for data in datab:
    print(data)
    print(datab[data].shape)
    print(datab[data])


#Visualiza Data.
companies = []
for data in datab:
    companies.append(data)
#Generate colors for the amount of datasets we have. 
colors = iter(cm.rainbow(np.linspace(0, 1, len(datab))))
#Generate timeseries plot for every dataset in the dictionary. 
plt.ylabel('USD($)')
plt.xlabel('Year')
for data in datab:
    plt.plot(datab[data].timestamp, datab[data].close, color = next(colors))
plt.legend(companies)