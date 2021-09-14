from pandas import read_csv

path=path=r"C:\Akash Files\Machine_Learnings\MLStep_by_step\pima-indians-diabetes.csv"
data=read_csv(path)
print(data.skew())