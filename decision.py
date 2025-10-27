from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = load_iris()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

clf = DecisionTreeClassifier(criterion='entropy', random_state=0)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print("Decision Tree Structure:\n")
print(export_text(clf, feature_names=data.feature_names))
print("\nAccuracy:", accuracy_score(y_test, y_pred))
