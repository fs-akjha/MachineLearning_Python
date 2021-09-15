from pandas import read_csv

path=r"C:\Akash Files\MachineLearning_Python\MLStep_by_step\Iris.csv"
data=read_csv(path)
print(data.shape)
print(data.dtypes)
print(data[:5])