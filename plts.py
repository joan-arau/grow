import matplotlib.pyplot as plt
import pandas as pd
import get_files



# get_files.get_temp()
df = pd.read_csv('/Users/joan/PycharmProjects/grow/temp/data.csv')[['hum','moist','temp','time']]
print(df)
df['time'] = pd.to_datetime(df['time'], format='%m%d%Y%H%M%S', errors = 'coerce')
print(df)

fig, axs = plt.subplots(3)

axs[2].plot(df['time'],df['hum']*0.55)
axs[2].set_title('Humidity')
axs[0].plot(df['time'],df['moist'])
axs[0].set_title('Soil Moisture')
axs[1].plot(df['time'],df['temp'])
axs[1].set_title('Temperature')

plt.show()