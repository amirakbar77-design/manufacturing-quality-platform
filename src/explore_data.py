import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score,
)

df = pd.read_csv("data/raw/ai4i2020.csv")

print(df.head())
print()
print(df.shape)
print()
print(df.columns)

print()
df.info()

print()
print(df.isna().sum())

print()
print(df["Machine failure"].value_counts())

print()
print(df["Machine failure"].value_counts(normalize=True))

feature_columns = [
    "Type",
    "Air temperature [K]",
    "Process temperature [K]",
    "Rotational speed [rpm]",
    "Torque [Nm]",
    "Tool wear [min]",
]

target_column = "Machine failure"

x = df[feature_columns]
y = df[target_column]

X_train, X_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

baseline_predictions = np.zeros(len(y_test), dtype=int)

baseline_accuracy = accuracy_score(y_test, baseline_predictions)

print()
print("Baseline accuracy:", baseline_accuracy)

print()
print("Confusion matrix:")
print(confusion_matrix(y_test, baseline_predictions))

print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("y_train:", y_train.shape)
print("y_test:", y_test.shape)

print()
print("Feature matrix shape:", x.shape)
print("Target shape:", y.shape)

print()
print(x.head())

print()
print(y.head())

print()
print("Training target proportions:")
print(y_train.value_counts(normalize=True))

print()
print("Test target proportions:")
print(y_test.value_counts(normalize=True))

baseline_precision = precision_score(
    y_test,
    baseline_predictions,
    zero_division=0,
)

baseline_recall = recall_score(
    y_test,
    baseline_predictions,
)

baseline_f1 = f1_score(
    y_test,
    baseline_predictions,
)

print()
print("Baseline metrics")
print("----------------")
print(f"Accuracy:  {baseline_accuracy:.3f}")
print(f"Precision: {baseline_precision:.3f}")
print(f"Recall:    {baseline_recall:.3f}")
print(f"F1 score:  {baseline_f1:.3f}")
