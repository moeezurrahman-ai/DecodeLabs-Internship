import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# ==========================================================
# Project 2: Iris Flower Classification
# Internship: DecodeLabs
# Track: Artificial Intelligence
# Author: Moeez Ur Rahman
# ==========================================================

# ----------------------------------------------------------
# 1. Load the dataset
# ----------------------------------------------------------

data = pd.read_csv(
    "iris.data",
    header=None,
    names=[
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width",
        "species"
    ]
)

print("Iris Dataset")
print("-" * 50)
print(f"Number of samples: {len(data)}")
print(f"Number of features: 4")

# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Display class distribution
print("\nSpecies Distribution:")
print(data["species"].value_counts())


# ----------------------------------------------------------
# 2. Separate features and target
# ----------------------------------------------------------

X = data[
    [
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width"
    ]
]

y = data["species"]


# ----------------------------------------------------------
# 3. Split the dataset
# ----------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nDataset Split")
print("-" * 50)
print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")


# ----------------------------------------------------------
# 4. Create and train the KNN classifier
# ----------------------------------------------------------

model = KNeighborsClassifier(n_neighbors=5)

model.fit(X_train, y_train)

print("\nModel Training")
print("-" * 50)
print("KNN classifier trained successfully.")


# ----------------------------------------------------------
# 5. Make predictions
# ----------------------------------------------------------

y_pred = model.predict(X_test)


# ----------------------------------------------------------
# 6. Evaluate the model
# ----------------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Evaluation")
print("-" * 50)
print(f"Accuracy: {accuracy * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))


# ----------------------------------------------------------
# 7. Test the model with a new flower
# ----------------------------------------------------------

new_flower = pd.DataFrame(
    [[5.1, 3.5, 1.4, 0.2]],
    columns=[
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width"
    ]
)

prediction = model.predict(new_flower)

print("\nNew Flower Prediction")
print("-" * 50)
print("Predicted species:", prediction[0])