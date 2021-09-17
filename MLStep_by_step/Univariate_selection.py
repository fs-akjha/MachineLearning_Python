from pandas import read_csv
from numpy import set_printoptions
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

path=r"C:\Akash Files\MachineLearning_Python\MLStep_by_step\pima-indians-diabetes.csv"
dataframe=read_csv(path)
array=dataframe.values
X=array[:,0:8]
Y=array[:,8]
test=SelectKBest(score_func=chi2,k=4)
fit=test.fit(X,Y)
set_printoptions(precision=2)
print(fit.scores_)
featured_data=fit.transform(X)
print("\n Featured data: \n",featured_data[0:4])
