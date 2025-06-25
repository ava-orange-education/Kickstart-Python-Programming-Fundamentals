from sklearn.datasets import fetch_california_housing
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the california Housing dataset
california = fetch_california_housing()
# Convert the dataset into a pandas DataFrame for better visualization
california_df = pd.DataFrame(california.data, columns=california.feature_names)
# Add the target (house prices) to the DataFrame
california_df['PRICE'] = california.target
# Display the first five rows of the data
print(california_df.head())



# Split the data into features (X) and target (y)
X = california_df.drop('PRICE', axis=1)
y = california_df['PRICE']
# Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Training data size: {X_train.shape}")
print(f"Testing data size: {X_test.shape}")


# Create a Linear Regression model
model = LinearRegression()
# Train the model using the training data
model.fit(X_train, y_train)
print("Model training completed!")


# Make predictions on the testing data
y_pred = model.predict(X_test)
# Calculate the Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)
# Calculate the R-squared score
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared Score: {r2:.2f}")


