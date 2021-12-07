import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('log.csv')

plt.figure(figsize=(16,9))
plt.xlabel('Update Step')
plt.ylabel('Update Time')
plt.plot(df['UpdateTime'])
plt.show()

plt.figure(figsize=(16,9))
plt.xlabel('Update Step')
plt.ylabel('Neurons Fired')
plt.plot(df['NeuronsFired'])
plt.show()

