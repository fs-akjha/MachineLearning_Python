from os import read
from pandas import read_csv,set_option

path=r"C:\Akash Files\Machine_Learnings\MLStep_by_step\pima-indians-diabetes.csv"

data=read_csv(path)
set_option('display.width',100)
set_option('precision',2)
correlations=data.corr(method="pearson")
print(correlations)