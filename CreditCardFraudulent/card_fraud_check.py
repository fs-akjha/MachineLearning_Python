import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#loading dataset to a Pandas Dataframe
credit_card_data=pd.read_csv('creditcard.csv')

#first 5 rows of a dataset
credit_card_data.head()
#last 5 rows of a dataset
credit_card_data.tail()

#dataset informations
credit_card_data.info()

#checking the number of missing values in each column
# credit_card_data.isnull().sum()

#The distribution of legit transactions and Fraudulent transactions
credit_card_data['Class'].value_counts()
#0--> Normal Transactions
#1--> Fradulent Transactions
#separating the data for analysis
legit=credit_card_data[credit_card_data.Class == 0]
fraud=credit_card_data[credit_card_data.Class == 1]
# print(legit.shape)
# print(fraud.shape)

#statistical measures of the data
legit.Amount.describe()
fraud.Amount.describe()

#compare the values for both transactions
credit_card_data.groupby('Class').mean()

#Under-Sampling
#build a sample dataset containing similer distribution of normal transaction and Fraudulent Transactions
legit_sample=legit.sample(n=492)

#Concatenating 2 Dataframes
new_dataset=pd.concat([legit_sample,fraud],axis=0)
new_dataset.head()
new_dataset.tail()

new_dataset['Class'].value_counts()

new_dataset.groupby('Class').mean()

#Splitting the data into Features and Targets
X=new_dataset.drop(columns='Class',axis=1)
Y=new_dataset['Class']

#Split the data into Training data and Testing data
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,stratify=Y,random_state=2)
print(X.shape,X_train.shape,X_test.shape)

#Model Training
model=LogisticRegression()
#Training the Logistic Regression Model with Training Data
model.fit(X_train,Y_train)

#Model Evaluation based on Accuracy Score
#Accuracy on training data
X_train_predction=model.predict(X_train)
training_data_accuracy=accuracy_score(X_train_predction,Y_train)
print("Accuracy on training data: ",training_data_accuracy)

#Accuracy on test data
X_test_prediction=model.predict(X_test)
test_data_accuracy=accuracy_score(X_test_prediction,Y_test)
print("Accuracy on Testing data: ",test_data_accuracy)
