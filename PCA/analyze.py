# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

async def readData(path):
    # read every line and save in variable
    with open(path, "r", encoding="utf8") as data:
        data = data.readlines()

    return data

async def preprare_data(data):
    datadict = {
        "program": [],
        "lines": [],
        "iReadTextTempTableSequenceReplace1": [],
        "parseStrings": [],
        "parseInclude": [],
        "parseNonBlockPreProcStatements": [],
        "iParsePreProcBlockStatements": [],
        "iParseBlockStatementsOpen": [],
        "iParseBlockStatementsClose": [],
        "ifcanfind": [],
        "writeStatementsInCSV": []
    }
    for line in data:
        line = line.replace('\n', "")
        line = line.split(",")
        datadict["program"].append(line[0])
        datadict["lines"].append(int(line[1].split(":")[1]))
        datadict["iReadTextTempTableSequenceReplace1"].append(int(line[2].split(":")[1]))
        datadict["parseStrings"].append(int(line[3].split(":")[1]))
        datadict["parseInclude"].append(int(line[4].split(":")[1]))
        datadict["parseNonBlockPreProcStatements"].append(int(line[5].split(":")[1]))
        datadict["iParsePreProcBlockStatements"].append(int(line[6].split(":")[1]))
        datadict["iParseBlockStatementsOpen"].append(int(line[7].split(":")[1]))
        datadict["iParseBlockStatementsClose"].append(int(line[8].split(":")[1]))
        datadict["ifcanfind"].append(int(line[9].split(":")[1]))
        datadict["writeStatementsInCSV"].append(int(line[10].split(":")[2]))

    dfdata = pd.DataFrame.from_dict(datadict)
    dfdata = dfdata.sort_values('lines')


    return dfdata

def analyze_data (data):
    # >> > X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    # >> > pca = PCA(n_components=2)
    # >> > pca.fit(X)
    # PCA(n_components=2)
    # >> > print(pca.explained_variance_ratio_)
    # [0.9924... 0.0075...]
    # >> > print(pca.singular_values_)
    # [6.30061... 0.54980...]

    print(data)