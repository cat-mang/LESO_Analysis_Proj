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

def expand_quantity(df, item_column, quantity_column):
    df = df.groupby(item_column).sum(numeric_only=True)
    return df

#Group the data by County

def groupby_county(df, state_column, county_column):
    df_grouped = df.groupby(['state_column', 'county_column']).sum(numeric_only=True)
    grouped_df = df_grouped.reset_index()
    return grouped_df

#Save a new CSV file

def new_file(df, new_file_name):
    df.to_csv('new_file_name', index=False)


#Filter out Items by Name

def filter_items(df, col, item_list):
    filtered_df = df[df[col].isin(item_list)]
    return filtered_df


#Merge DataFrames
def merge_data(df_1, df_2, col_1, col_2, method):
    new_df = pd.merge(df_1, df_2, on=[col_1, col_2], how=method)
    new_df.fillna(0, inplace=True)
    return new_df

#Replace Counties with Standardized Names
def standardize_counties(df, col, old_name, new_name):
    df[col] = df[col].str.replace(old_name, new_name)
    return df

