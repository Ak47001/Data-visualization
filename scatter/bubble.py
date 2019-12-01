import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('stats.csv')

plt.scatter(df['Runs'], df['Overs'], s = df['Wickets']*50 )	# s = marker size

plt.xlabel('Runs')
plt.ylabel('Overs bowled')
plt.title('Bowling Analysis')

plt.show()