from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()

data = iris.data
target = iris.target

clf = KNeighborsClassifier()
clf.fit(data, target)

preds = clf.predict([[21,13,14,11]])

print(preds)
