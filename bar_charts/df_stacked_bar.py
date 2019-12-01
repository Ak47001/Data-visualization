import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
from pandas import DataFrame
 


df = pd.read_csv('marks.csv')

ADS = df.loc[10:15,'ADS']
PDV = df.loc[10:15,'PDV']
FML = df.loc[10:15,'FML']
PSI = df.loc[10:15,'PSI']
DIP = df.loc[10:15,'DIP']
r = np.arange(len(ADS))
 
# Names of group and bar width
names = df.loc[10:15,'Roll Num']
barWidth = 0.75
 

plt.bar(r, ADS, color='red', edgecolor='white', width=barWidth)

plt.bar(r, PDV, bottom= list(ADS), color='blue', edgecolor='white', width=barWidth)

plt.bar(r, FML, bottom=list(ADS+PDV), color='green', edgecolor='white', width=barWidth)

plt.bar(r, PSI, bottom= list(ADS+PDV+FML), color='yellow', edgecolor='white', width=barWidth)

plt.bar(r, DIP, bottom= list(ADS+PDV+FML+DIP), color='orange', edgecolor='white', width=barWidth)


plt.xticks(r, names)
plt.xlabel("group")


# Show graphic
plt.show()

