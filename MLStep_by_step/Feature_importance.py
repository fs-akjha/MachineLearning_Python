from pandas import read_csv
from sklearn.ensemble import ExtraTreesClassifier

path=r"C:\Akash Files\MachineLearning_Python\MLStep_by_step\pima-indians-diabetes.csv"
dataframe=read_csv(path)
array=dataframe.values
X=array[:,0:8]
Y=array[:,8]
model=ExtraTreesClassifier()
model.fit(X,Y)
print(model.feature_importances_)