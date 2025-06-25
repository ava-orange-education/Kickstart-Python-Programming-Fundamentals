from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = load_iris()
# Display the features and labels
X = iris.data
y = iris.target
print(f"Features: {X[:5]}")
print(f"Labels: {y[:5]}")


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print(f"Training data size: {X_train.shape}")
print(f"Testing data size: {X_test.shape}")


# Create a Decision Tree model
model = DecisionTreeClassifier()
# Train the model
model.fit(X_train, y_train)
print("Model training completed!")


# Make predictions with the testing set
y_pred = model.predict(X_test)
# Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy * 100:.2f}%")


