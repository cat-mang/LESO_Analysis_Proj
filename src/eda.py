import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import stats

#Open and Read File
def read_file(df, file_path):
    '''
    Reads a .csv file as a DataFrame
    
    ARGS:
        df = dataframe
        file_path = relative path url of the csv file
    RETURN
        df
    ''' 
    df = pd.read_csv(file_path)


#Clean Data

def fix_capitalization(df, col):
    '''
    Capitalizes strings in a column
    
    ARGS:
        df = dataframe
        col = column name
    RETURN
        df
    ''' 
    df[col] = df[col].str.upper()
    return df

def fix_date (df,col):
    '''
    changes the type of column with a date to DateTime
    
    ARGS:
        df = dataframe
        col = column name
    RETURN
        df
    ''' 
    df[col] = pd.to_datetime(df[col], format='mixed')
    return df

def drop_na(df,col):
    '''
    drops nan values in a column
    
    ARGS:
        df = dataframe
        col = column name
    RETURN
        df
    ''' 
    df = df.dropna(subset=[col])
    return df

#Multiply out the amount of items by the quantity

def expand_quantity(df, item_column):
    '''
    groups dataframe by a column and provides the total quantity per item
    
    ARGS:
        df = dataframe
        item_col = column name that needs to be multiplied by quanity column
    RETURN
        df
    ''' 
    df = df.groupby(item_column).sum(numeric_only=True)
    return df

#Group the data by County

def groupby_county(df, state_column, county_column):
    '''
    groups a DataFrame by state and county
    
    ARGS:
        df = dataframe
        state_column = column name with state data
        county_column = column name with county data
    RETURN
        df grouped
    ''' 

    df_grouped = df.groupby([state_column, county_column]).sum(numeric_only=True)
    grouped_df = df_grouped.reset_index()
    return grouped_df

#Save a new CSV file


def new_file(df, new_file_name):
    '''
    saves df as a .csv file
    
    ARGS:
        df = dataframe
        new_file_name = .csv file name
    RETURN
        df
    ''' 
    df.to_csv(new_file_name, index=False)


#Filter out Items by Name

def filter_items(df, col, item_list):
    '''
    takes a list of strings to clean a dataset to match the string values
    
    ARGS:
        df = dataframe
        col = column name
        item_list = list of strings
    RETURN
        df with only the specified string values in the column
    ''' 
    filtered_df = df[df[col].isin(item_list)]
    return filtered_df


#Merge DataFrames
def merge_data(df_1, df_2, col_1, method, col_2):
    '''
    merges 2 DataFrames
    
    ARGS:
        df_1 = first dataframe
        df_2 = second dataframe
        col_1 = column to merge on
        col_2 = second column to merge on (optional)
        method = how to merge
    RETURN
        merged df
    ''' 
    new_df = pd.merge(df_1, df_2, on=[col_1, col_2], how=method)
    new_df.fillna(0, inplace=True)
    return new_df

#Replace Counties with Standardized Names


def standardize_counties(df, col, old_name, new_name):
    '''
    replaces strings in a column
    
    ARGS:
        df = dataframe
        col = column name
        old_name = string to be replaced
        new_name = string replacement value
    RETURN
        df
    ''' 
    df[col] = df[col].str.replace(old_name, new_name)
    return df

