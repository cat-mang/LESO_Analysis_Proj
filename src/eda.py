import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import stats

#Open and Read File
def read_file(df, file_path):
    df = pd.read_csv('file_path')


#Clean Data

def fix_capitalization(df, col):
    df[col] = df[col].str.upper()
    return df

def fix_date (df,col):
    df[col] = pd.to_datetime(df[col], format='mixed')
    return df

def drop_na(df,col):
    df = df.dropna(subset=[col])
    return df

#Multiply out the amount of items by the quantity

def expand_quantity(df, item_column, quantity_column)
    df = df.groupby(item_column).sum(numeric_only=True)
    return df

#Group the data by County

def groupby_county(df, state_column, county_column):
    df_grouped = df.groupby(['state_column', 'county_column']).sum(numeric_only=True)
    new_df = df_grouped.reset_index()
    return new_df

#Save as new CSV file

def new_file(df, new_file_name):
    df.to_csv('new_file_name', index=False)


#Filter out Items by Name

def filter_items(df, col, item_list):
    filtered_df = df[df[col].isin(item_list)]
    return filtered_df


