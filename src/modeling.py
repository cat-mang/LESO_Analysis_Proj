import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import stats
from scipy.stats import ttest_ind
from sklearn.linear_model import LinearRegression
from scipy.stats import norm
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

#Heatmap Correlations

def correlations(df):
    sns.heatmap(df.corr(numeric_only=True), annot=True,
                cmap=sns.diverging_palette(10, 220, sep=80, n=7),
                vmin = -0.5,
                vmax = 1)
    

#Linear Regression Plot

def lin_reg(df, col_1, col_2, graph_title, x_label, y_label):
    sns.lmplot(x='col_1', y='col_2', data=df, line_kws={"color":"red"})
    plt.title('graph_titel')
    plt.xlabel('x_label')
    plt.ylabel('y_label')
    plt.show()

#T Testing

def t_test(df, col_1, col_2, value):
    data = df[df[col_1]>value][col_2]
    data_2 = df[df[col_1]==value][col_2]
    t_statistic, p_value = ttest_ind(data, data_2)
    return (t_statistic, p_value)

# Lin Reg Model

def lin_reg_model(df,  dependent_col, col_1, col_2, col_3):
    # Step 1: Prepare Data
    X = df[[col_1, col_2, col_3]]
    y = df[dependent_col]

    # Step 2: Split Data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=10)

    # Step 3: Model Selection and Training
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Step 4: Model Evaluation
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    return(r2, mse)
  
#Predict Values

def prediction(model, value):
    independent_amount = value
    predicted_dependent_amount = model.predict([[independent_amount]])
    return predicted_dependent_amount