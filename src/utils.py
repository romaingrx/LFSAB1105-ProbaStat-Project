import pandas as pd
import numpy as np

def readCPU1():
    with open('./res/CPU1.txt','r') as f:
        df = pd.DataFrame(columns=[f.readline().replace('"','').replace('\n','').split(';')])
        line=f.readline()
        while line is not '':
            df.loc[len(df)] = line.replace('\n','').split(';')
            line=f.readline()
        df[df.columns[0]] = df[df.columns[0]].astype('float')
        df[df.columns[1]] = df[df.columns[1]].astype('bool')
    return df

def readCPU2():
    with open('./res/CPU2.txt','r') as f:
        df = pd.DataFrame(columns=[f.readline().replace('"','').replace('\n','').split(';')], dtype=('float','int'))
        line=f.readline()
        while line is not '':
            df.loc[len(df)] = line.replace('\n','').split(';')
            line=f.readline()
        df[df.columns[0]] = df[df.columns[0]].astype('float')
        df[df.columns[1]] = df[df.columns[1]].astype('int')
    return df
