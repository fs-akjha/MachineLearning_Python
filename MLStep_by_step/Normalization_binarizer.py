from pandas import read_csv
from sklearn.preprocessing import Binarizer

path=r"C:\Akash Files\MachineLearning_Python\MLStep_by_step\pima-indians-diabetes.csv"
dataframe=read_csv(path)
array=dataframe.values
binarizer=Binarizer(threshold=0.5).fit(array)
Data_binarized=binarizer.transform(array)
print("\n Binary data: \n",Data_binarized[0:5])