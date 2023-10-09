from pandas import read_csv
from test import prediction

training_df=read_csv("training_diabetes.csv")
testing_df=read_csv("testing_diabetes.csv",usecols=[0,1,2,3,4,5,6,7])
testing_df_outcome=read_csv("testing_diabetes.csv",usecols=[8])
testing_outcome_list=testing_df_outcome.values.tolist()
actual_outcome=[]
columns=training_df.columns
testing_data=[]
prediction_data=[]
for i in range(len(testing_df)):
    testing_data.append(testing_df.iloc[[i]].values.tolist()[0])
    actual_outcome.append(testing_df_outcome.iloc[[i]].values.tolist()[0][0])

for i in testing_data:
    prediction_data.append(prediction(i))
with open("outputSet.txt","w") as f:
    for i in prediction_data:
        f.write(str(i)+" \n")

def getAccuracy(truePred_values,actualTrue_values):
    return (truePred_values/(actualTrue_values)*100)
truePred=0
for i in range(len(testing_df)):
    # print(testing_outcome_list[i][0],prediction_data[i])
    if testing_outcome_list[i][0]==prediction_data[i]:
        truePred+=1
# print(truePred)
print("Accuracy Of Our Model is ",getAccuracy(truePred,len(testing_outcome_list)),"%")