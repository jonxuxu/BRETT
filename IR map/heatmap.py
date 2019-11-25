import numpy as np
import numpy.random
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def gradient(x, y, heatmap, memo):
    scale = 0.995
    if heatmap[x][y] > 50:
        if [x+1, y] not in memo:
            heatmap[x+1][y] = heatmap[x][y]*scale
            memo.append([x+1, y])
            gradient(x+1, y, heatmap, memo)
        if [x, y+1] not in memo:
            heatmap[x][y+1] = heatmap[x][y]*scale
            memo.append([x, y+1])
            gradient(x, y+1, heatmap, memo)
        if [x-1, y] not in memo:
            heatmap[x-1][y] = heatmap[x][y]*scale
            memo.append([x-1, y])
            gradient(x-1, y, heatmap, memo)
        if [x, y-1] not in memo:
            heatmap[x][y-1] = heatmap[x][y]*scale
            memo.append([x, y-1])
            gradient(x, y-1, heatmap, memo)


# File I/O
with open('test_flight_3.txt', encoding='utf-8') as file:
    posx = []
    posy = []
    temp = []
    file.readline()
    for line in file:
        line = line.strip().split(',')
        posx.append(float(line[1]))
        posy.append(float(line[2]))
        temp.append(float(line[6]) - float(line[5]))


# Normalize data so no non-zero coordinates
minx = min(posx)
miny = min(posy)

data = [[int((x - minx)*100), int((y - miny)*100), temp]
        for (x, y, temp) in zip(posx, posy, temp)]

posx = [line[0] for line in data]
posy = [line[1] for line in data]
temp = [line[2] for line in data]

coor = [[None for j in range(max(posy)+1)] for i in range(max(posx)+1)]

for i in range(len(data)):
    x = posx[i]
    y = posy[i]
    tempVal = temp[i]
    coor[x][y] = tempVal  # coor[x][y])


posx = []
posy = []
temp = []

coordinates = []
for x in range(len(coor)):
    for y in range(len(coor[x])):
        if coor[x][y] is not None and coor[x][y] > 0:
            coordinates.append((x, y))

for (x, y) in coordinates:

    gradient(x, y, coor, [])

for x in range(len(coor)):
    for y in range(len(coor[x])):
        posx.append(x)
        posy.append(y)
        temp.append(coor[x][y])

# Create heat map
reds = sns.set_palette(sns.color_palette("coolwarm", 25)
                       )  # turn down the intensity
df = pd.DataFrame({'PositionX': posx, 'PositionY': posy, 'Temperature': temp})
data = df.pivot(index="PositionX", columns="PositionY", values="Temperature")
# heatMap = sns.heatmap(data, annot=True, cmap="coolwarm", center=1)  # change center value to change color scale
plt.figure(figsize=(95.28, 47.56))
heatMap = sns.heatmap(data, cmap='coolwarm', center=1,
                      yticklabels=False, xticklabels=False, cbar=False)
heatMap.invert_yaxis()
heatMap.set_ylabel('')
heatMap.set_xlabel('')

# Save a png of the created heatmap
fig = heatMap.get_figure()
fig.savefig("heatmap.png")

# Printing out the created maps and tables
# plt.show()
# print(df)
# print(data)
