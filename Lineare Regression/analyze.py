# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

async def readData(path):
    # read every line and save in variable
    with open(path, "r", encoding="utf8") as data:
        data = data.readlines()

    return data

async def preprare_data(data):
    datadict = {
        "x": [],
        "y": [],
    }
    dataarray = []

    for line in data:
        line = line.replace('\n', "")
        line = line.split(",")
        datadict["x"].append(line[0])
        datadict["y"].append(line[1])
        pair_array = [line[0], line[1]]
        dataarray.append(pair_array)

    return datadict, dataarray

def createplot(datax, datay, datadict, output_path):
    print("creating plot")
    fig, ax = plt.subplots(figsize=(5, 5))  # Create a figure and an axes.
    ax.plot(datax, datay, label='linear')  # Plot some data on the axes.
    # ax.plot(x, x ** 2, label='quadratic')  # Plot more data on the axes...
    # ax.plot(x, x ** 3, label='cubic')  # ... and some more.
    ax.set_xlabel('x label')  # Add an x-label to the axes.
    ax.set_ylabel('y label')  # Add a y-label to the axes.
    ax.set_title("DATA")  # Add a title to the axes.
    ax.legend()  # Add a legend.
    plt.grid(axis='both', color='0.95')
    fig.savefig(output_path + 'dfdataPLOT.png')

    #plt.show()
    dfdata = pd.DataFrame.from_dict(datadict)
    dfdata.to_csv(output_path + 'sorted_data.csv', header=True, quotechar=' ', index=True, sep=';', mode='a', encoding='utf8')
    return fig, ax
    #self.view.plt.plot([1, 2, 3, 4])
    #self.view.plt.ylabel('some numbers')
    #self.view.plt.show()

def analyze_data (data, fig, ax):
    print("analyze_data")
    print(data)
    # >> > X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    # >> > pca = PCA(n_components=2)
    # >> > pca.fit(X)
    # PCA(n_components=2)
    # >> > print(pca.explained_variance_ratio_)
    # [0.9924... 0.0075...]
    # >> > print(pca.singular_values_)
    # [6.30061... 0.54980...]
    return data, fig, ax

