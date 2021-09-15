from pandas import read_csv

path=r"C:\Akash Files\MachineLearning_Python\MLStep_by_step\pima-indians-diabetes.csv"
data=read_csv(path)
count_class = data.groupby('class').size()
print(count_class)