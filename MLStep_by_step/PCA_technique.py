from numpy import array
from pandas import read_csv
from sklearn.decomposition import PCA

path=r"C:\Akash Files\MachineLearning_Python\MLStep_by_step\pima-indians-diabetes.csv"
dataframe=read_csv(path)
array=dataframe.values
X=array[:,0:8]
Y=array[:,8]
pca=PCA(n_components=3)
fit=pca.fit(X)
print("Explained Variance: %s"%fit.explained_variance_ratio_)
print(fit.components_)