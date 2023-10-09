import pandas as pd
import numpy as np
# from tkinter import *
# from tkinter import messagebox

x_train = pd.read_csv('diabetes.csv' , usecols= ['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age'])
y_train = pd.read_csv('diabetes.csv' , usecols= ['Outcome'])

X = x_train.values
Y = y_train.values


def dist(x1, x2):
    return np.sqrt(sum((x1 - x2) ** 2))


def knn(X, Y, querypoint, k=20):
    vals = []
    m = X.shape[0]
    for i in range(m):
        d = dist(querypoint, X[i])
        vals.append((d, Y[i]))

    vals = sorted(vals)
    vals = vals[:k]

    vals = np.array(vals,dtype=object)
    # print(vals)
    new_vals = np.unique(vals[:, 1], return_counts=True)
    index = new_vals[1].argmax()
    pred = new_vals[0][index]
    return pred


def prediction(l):
    number = knn(X, Y, l)
    return number

print(prediction([10,90,85,32,0,34.9,0.825,56]))