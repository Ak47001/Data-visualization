import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('stats.csv')

plt.scatter(df['Runs'], df['Overs'], s = df['Wickets']*50)

plt.ylim(40,180)

for line in range(0,df.shape[0]):
     plt.text(df.Runs[line], df.Overs[line], df.Name[line], horizontalalignment='center', size='medium', color='black', weight='semibold')

plt.xlabel('Runs')
plt.ylabel('Overs bowled')
plt.title('Bowling Analysis')

plt.show()