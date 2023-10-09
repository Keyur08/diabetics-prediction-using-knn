import pandas as pd
import numpy as np

x_train = pd.read_csv('training_diabetes.csv' , usecols= ['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age'])
y_train = pd.read_csv('training_diabetes.csv' , usecols= ['Outcome'])

X = x_train.values
Y = y_train.values


def dist(x1, x2):
    return np.sqrt(sum((x1 - x2) ** 2))


def knn(X, Y, querypoint, k=20):
    vals = []
    m = X.shape[0]
    indexes=[]
    for i in range(m):
        d = dist(querypoint, X[i])
        vals.append((d, Y[i]))

    vals = sorted(vals)
    vals = vals[:k]
    oneCount=0
    zeroCount=0
    pred=1
    for i in vals:
        if i[1][0]==0:
            zeroCount+=1
        else:
            oneCount+=1
    if zeroCount>oneCount:
        pred=0
    

    return pred


def prediction(l):
    number = knn(X, Y, l)
    return number

print(prediction([1,106,70,28,135,34.2,0.142,22]))