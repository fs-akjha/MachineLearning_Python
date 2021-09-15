from pandas import read_csv
from numpy import set_printoptions
from sklearn import preprocessing

path=r"C:\Akash Files\MachineLearning_Python\MLStep_by_step\pima-indians-diabetes.csv"
dataframe=read_csv(path)
array=dataframe.values
data_scaler=preprocessing.MinMaxScaler(feature_range=(0,1))
data_rescaled=data_scaler.fit_transform(array)
set_printoptions(precision=1)
print("\n Scaled data:\n",data_rescaled[0:10])