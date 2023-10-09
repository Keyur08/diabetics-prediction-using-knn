import pandas as pd
from random import randint
df1=pd.read_csv("diabetes.csv")
total=len(df1)
training_rows=538
training_indexes=[]
testing_indexes=[]
count=0
while count!=training_rows:
    a=randint(0,training_rows-1)
    if a not in training_indexes:
        training_indexes.append(a)
        count+=1


for i in range(total):
    if i not in training_indexes:
        testing_indexes.append(i)
training_df=df1.iloc[training_indexes]
testing_df=df1.iloc[testing_indexes]
# training_df.to_csv("training_diabetes.csv",index=False)
# testing_df.to_csv("testing_diabetes.csv",index=False)
