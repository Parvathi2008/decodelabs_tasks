# Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

print("=" * 65)
print("      PRODUCT RETURN CLASSIFICATION MODEL")
print("=" * 65)

# Load dataset
df = pd.read_excel("Product-Sales-Region.xlsx")

# Display dataset
print("\nFirst 5 Rows:\n")
print(df.head())

print("\nDataset Information:\n")
print(df.info())

print("\nDataset Shape:", df.shape)

# Remove unnecessary columns
drop_columns = [
    "OrderID",
    "CustomerName",
    "Date",
    "OrderDate",
    "DeliveryDate"
]

for col in drop_columns:
    if col in df.columns:
        df.drop(col, axis=1, inplace=True)

# Convert all categorical columns into numeric values
df = pd.get_dummies(df, drop_first=True)

# Features and Target
X = df.drop("Returned", axis=1)
y = df["Returned"]

print("\nFeatures:")
print(X.columns.tolist())

print("\nTarget Column: Returned")

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Records :", len(X_train))
print("Testing Records  :", len(X_test))

# Create Classification Model
model = DecisionTreeClassifier(random_state=42)

# Train Model
model.fit(X_train, y_train)

print("\nModel Training Completed Successfully!")

# Prediction
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print(f"\nModel Accuracy : {accuracy*100:.2f}%")

print("\nClassification Report:\n")
print(classification_report(y_test, predictions))

print("\nFirst 10 Predictions\n")

for i in range(10):
    print(
        f"Actual: {y_test.iloc[i]}    Predicted: {predictions[i]}"
    )

print("\nClassification Completed Successfully!")
