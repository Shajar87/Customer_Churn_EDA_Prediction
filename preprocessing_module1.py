# preprocessing_module.py
import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(df):

    #Fill missing values
    df.ffill(inplace=True)

    if df.shape[0] == 1: 
            scaled_data = df
    else:
            #Scale Features
            scaler = StandardScaler()
            scaled_data = scaler.fit_transform(df)
    return scaled_data
