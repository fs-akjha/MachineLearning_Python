from pandas import read_csv
from numpy import array, set_printoptions
from sklearn.preprocessing import Normalizer

path=r"C:\Akash Files\MachineLearning_Python\MLStep_by_step\pima-indians-diabetes.csv"
dataframe=read_csv(path)
array=dataframe.values
Data_normalizer=Normalizer(norm='l2').fit(array)
Data_normalized=Data_normalizer.transform(array)
set_printoptions(precision=2)
print("\n Normalized data \n",Data_normalized[0:3])