from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
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

numeric_features = [
    "Air temperature [K]",
    "Process temperature [K]",
    "Rotational speed [rpm]",
    "Torque [Nm]",
    "Tool wear [min]", ]


categorical_features = [
    "Type",
]

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features,
        ),
        (
            "numeric",
            StandardScaler(),
            numeric_features,
        ),
    ]
)

X_train_prepared = preprocessor.fit_transform(X_train)
X_test_prepared = preprocessor.transform(X_test)

print()
print("Prepared training shape:", X_train_prepared.shape)
print("Prepared test shape:", X_test_prepared.shape)
print()
print(preprocessor.get_feature_names_out())

model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("classifier", LogisticRegression(max_iter=1000)),
    ]
)

model.fit(X_train, y_train)
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions, zero_division=0)
recall = recall_score(y_test, predictions)
f1 = f1_score(y_test, predictions)

print()
print("Logistic Regression")
print("-------------------")
print(f"Accuracy:  {accuracy:.3f}")
print(f"Precision: {precision:.3f}")
print(f"Recall:    {recall:.3f}")
print(f"F1 score:  {f1:.3f}")

print()
print("Confusion matrix:")
print(confusion_matrix(y_test, predictions))

balanced_model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        (
            "classifier",
            LogisticRegression(
                max_iter=1000,
                class_weight="balanced",
            ),
        ),
    ]
)

balanced_model.fit(X_train, y_train)

balanced_predictions = balanced_model.predict(X_test)

balanced_accuracy = accuracy_score(y_test, balanced_predictions)
balanced_precision = precision_score(
    y_test,
    balanced_predictions,
    zero_division=0,
)
balanced_recall = recall_score(y_test, balanced_predictions)
balanced_f1 = f1_score(y_test, balanced_predictions)

print()
print("Balanced Logistic Regression")
print("----------------------------")
print(f"Accuracy:  {balanced_accuracy:.3f}")
print(f"Precision: {balanced_precision:.3f}")
print(f"Recall:    {balanced_recall:.3f}")
print(f"F1 score:  {balanced_f1:.3f}")

print()
print("Confusion matrix:")
print(confusion_matrix(y_test, balanced_predictions))
