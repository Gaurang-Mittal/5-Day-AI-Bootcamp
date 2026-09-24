import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report



df = pd.read_csv("student_results.csv")
print(df.head())
# df.groupby("result")[["study_hours","attendance","assignments"]].mean()
# print(df.head())



plt.figure(figsize=(7,4))
plt.scatter(df["study_hours"], df["attendance"], c=df["result"])
plt.xlabel("Study hours")
plt.ylabel("Attendance")
plt.title("Student performance pattern")
plt.show()



X = df[["study_hours", "attendance", "assignments"]]
y = df["result"]



print("X shape:", X.shape)
print("y shape:", y.shape)

model=DecisionTreeClassifer()
model.fit(X,y)
print("Model training complete!")

# model_predictions = model.predict(X)