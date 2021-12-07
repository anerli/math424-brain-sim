import pandas as pd
import matplotlib.pyplot as plt

df_6p = pd.read_csv('6p.csv')
df_5p = pd.read_csv('5p.csv')
df_4p = pd.read_csv('4p.csv')
df_3p = pd.read_csv('3p.csv')

plt.figure(figsize=(16,9))
plt.xlabel('Update Step')
plt.ylabel('Update Time')
plt.plot(df_6p['UpdateTime'].iloc[1:], label='6 Processes')
plt.plot(df_5p['UpdateTime'].iloc[1:], label='5 Processes')
plt.plot(df_4p['UpdateTime'].iloc[1:], label='4 Processes')
plt.plot(df_3p['UpdateTime'].iloc[1:], label='3 Processes')

plt.legend()
plt.show()

plt.figure(figsize=(16,9))
plt.xlabel('Update Step')
plt.ylabel('Neurons Fired')
plt.plot(df_6p['NeuronsFired'], label='6 Processes')
plt.plot(df_5p['NeuronsFired'], label='5 Processes')
plt.plot(df_4p['NeuronsFired'], label='4 Processes')
plt.plot(df_3p['NeuronsFired'].iloc[1:], label='3 Processes')

plt.legend()
plt.show()

