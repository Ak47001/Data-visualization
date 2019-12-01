import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('stats.csv')

plt.scatter(df['Runs'], df['Overs'])

plt.xlabel('Runs')
plt.ylabel('Overs bowled')
plt.title('Bowling Analysis')
plt.show()