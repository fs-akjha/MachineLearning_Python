from matplotlib import pyplot
from pandas import read_csv

path=r"C:\Akash Files\MachineLearning_Python\MLStep_by_step\pima-indians-diabetes.csv"
data=read_csv(path)
data.plot(kind='box',subplots=True,layout=(3,3),sharex=False,sharey=False)
pyplot.show()