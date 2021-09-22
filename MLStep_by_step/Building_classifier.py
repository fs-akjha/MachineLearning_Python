import sklearn

from sklearn.datasets import load_breast_cancer
data=load_breast_cancer()
label_names=data['target_names']
labels=data['target']
feature_names=data['feature_names']
features = data['data']

print(label_names)
print(feature_names[0])
print(feature_names[1])
print(features[0])
print(features[1])