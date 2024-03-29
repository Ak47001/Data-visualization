import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
 

rc('font', weight='bold')
 
# Values of each group
ADS = [12, 28, 1, 8, 22]
PDV = [28, 7, 16, 4, 10]
ML = [25, 3, 23, 25, 17]
 
# Heights of ADS + PDV (TO DO better)
#bars = [40, 35, 17, 12, 32]
bars = [ ADS[i] + PDV[i] for i in range(len(ADS))]
 
# The position of the bars on the x-axis
r = [0,1,2,3,4]
 
# Names of group and bar width
names = ['A','B','C','D','E']
barWidth = 0.75
 
# Create brown bars
plt.bar(r, ADS, color='red', edgecolor='white', width=barWidth)
# Create green bars (middle), on top of the first ones
plt.bar(r, PDV, bottom=ADS, color='blue', edgecolor='white', width=barWidth)
# Create green bars (top)
plt.bar(r, ML, bottom=bars, color='#2d7f5e', edgecolor='white', width=barWidth)
 
# Custom X axis
#plt.xticks(r, names, fontweight='bold')
plt.xticks(r, names)
plt.xlabel("group")


# Show graphic
plt.show()

