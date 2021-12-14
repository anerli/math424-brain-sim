import pandas as pd
import matplotlib.pyplot as plt

df_6p = pd.read_csv('6p.csv')
df_5p = pd.read_csv('5p.csv')
df_4p = pd.read_csv('4p.csv')
df_3p = pd.read_csv('3p.csv')
df_2p = pd.read_csv('2p.csv')
df_1p = pd.read_csv('1p.csv')

print(df_6p['UpdateTime'].iloc[1:].mean())
print(df_5p['UpdateTime'].iloc[1:].mean())
print(df_4p['UpdateTime'].iloc[1:].mean())
print(df_3p['UpdateTime'].iloc[1:].mean())
print(df_2p['UpdateTime'].iloc[1:].mean())
print(df_1p['UpdateTime'].iloc[1:].mean())

print(1/df_6p['UpdateTime'].iloc[1:].mean())
print(1/df_5p['UpdateTime'].iloc[1:].mean())
print(1/df_4p['UpdateTime'].iloc[1:].mean())
print(1/df_3p['UpdateTime'].iloc[1:].mean())
print(1/df_2p['UpdateTime'].iloc[1:].mean())
print(1/df_1p['UpdateTime'].iloc[1:].mean())

plt.figure(figsize=(16,9))
plt.xlabel('Update Step')
plt.ylabel('Update Time (seconds)')
plt.plot(df_6p['UpdateTime'].iloc[1:], label='6 Processes')
plt.plot(df_5p['UpdateTime'].iloc[1:], label='5 Processes')
plt.plot(df_4p['UpdateTime'].iloc[1:], label='4 Processes')
plt.plot(df_3p['UpdateTime'].iloc[1:], label='3 Processes')
plt.plot(df_2p['UpdateTime'].iloc[1:], label='2 Processes')
plt.plot(df_1p['UpdateTime'].iloc[1:], label='1 Process')

plt.legend()
plt.show()

plt.figure(figsize=(16,9))
plt.xlabel('Update Step')
plt.ylabel('Neurons Fired')
plt.plot(df_6p['NeuronsFired'], label='6 Processes')
plt.plot(df_5p['NeuronsFired'], label='5 Processes')
plt.plot(df_4p['NeuronsFired'], label='4 Processes')
plt.plot(df_3p['NeuronsFired'], label='3 Processes')
plt.plot(df_2p['NeuronsFired'], label='2 Processes')
plt.plot(df_1p['NeuronsFired'], label='1 Process')

plt.legend()
plt.show()

