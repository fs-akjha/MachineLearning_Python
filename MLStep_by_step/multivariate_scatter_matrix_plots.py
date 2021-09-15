from matplotlib import pyplot
from pandas import read_csv
from pandas.plotting import scatter_matrix

path=r"C:\Akash Files\MachineLearning_Python\MLStep_by_step\pima-indians-diabetes.csv"
data=read_csv(path)
scatter_matrix(data)
pyplot.show()