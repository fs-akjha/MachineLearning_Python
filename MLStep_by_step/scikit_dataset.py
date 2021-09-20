from sklearn.datasets import load_iris
iris=load_iris()
X=iris.data
Y=iris.target
feature_names=iris.feature_names
target_name=iris.target_names
print("Feature Names:",feature_names)
print("Target Names:",target_name)
print("\n First 10 rows of X: \n",X[:10])