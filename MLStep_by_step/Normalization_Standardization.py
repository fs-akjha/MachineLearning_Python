from sklearn.preprocessing import StandardScaler
from pandas import read_csv
from numpy import set_printoptions

path=r"C:\Akash Files\MachineLearning_Python\MLStep_by_step\pima-indians-diabetes.csv"
dataframe=read_csv(path)
array=dataframe.values
data_scaler=StandardScaler().fit(array)
data_rescaled=data_scaler.transform(array)
set_printoptions(precision=2)
print("\n Rescales data:\n",data_rescaled[0:5])