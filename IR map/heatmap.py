import numpy as np
import numpy.random
import matplotlib.pyplot as plt
import seaborn as sns
import math

# File I/O
with open('test_flight_3.txt', encoding='utf-8') as file:
    posx = []
    posy = []
    file.readline()
    for line in file:
        line = line.strip().split(',')
        x = line[1]
        y = line[2]
        temp = math.floor(float(line[6]) - float(line[5]))
        if temp > 0:
            for i in range(0, temp):
                posx.append(x)
                posy.append(y)
        else:
            posx.append(x)
            posy.append(y)

# Create heat map
reds = sns.set_palette(sns.color_palette("coolwarm", 25))  # turn down the intensity
datax = np.array(posx)
datay = np.array(posy)
plt.figure(figsize=(95.28, 47.56))
heatMap = sns.kdeplot(datax, datay, n_levels=50, shade=True, cmap='Reds', shade_lowest=False)
plt.show()
fig = heatMap.get_figure()
fig.savefig("heatmap.png")

