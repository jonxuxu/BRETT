import numpy as np
import numpy.random
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# File I/O
with open('out.txt', encoding='utf-8') as file:
    posx = []
    posy = []
    temp = []
    file.readline()
    for line in file:
        line = line.strip().split(',')
        posx.append(float(line[1]))
        posy.append(float(line[2]))
        temp.append(float(line[4]) - float(line[3]))

# Create heat map
reds = sns.set_palette(sns.color_palette("coolwarm", 25))  # turn down the intensity
df = pd.DataFrame({'PositionX': posx, 'PositionY': posy, 'Temperature': temp})
data = df.pivot(index="PositionX", columns="PositionY", values="Temperature")
# heatMap = sns.heatmap(data, annot=True, cmap="coolwarm", center=1)  # change center value to change color scale
heatMap = sns.heatmap(data, cmap='coolwarm', center=1, yticklabels=False, xticklabels=False, cbar=False)
heatMap.invert_yaxis()
heatMap.set_ylabel('')
heatMap.set_xlabel('')
plt.show()

# Sorted data
print(df)
print(data)
