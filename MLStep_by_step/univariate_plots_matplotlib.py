from os import read
from pandas import read_csv
from matplotlib import pyplot

path=r"C:\Akash Files\MachineLearning_Python\MLStep_by_step\pima-indians-diabetes.csv"
data=read_csv(path)
data.hist()
pyplot.show()