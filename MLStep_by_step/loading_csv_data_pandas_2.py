from pandas import read_csv

path=r"C:\Akash Files\Machine_Learnings\MLStep_by_step\Iris.csv"
headernames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(path, names=headernames)
print(data.shape)
print(data[:3])