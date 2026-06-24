import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

df["Average"] = df[["Math","Science","English"]].mean(axis=1)

print(df[["Student","Average"]])

plt.bar(df["Student"], df["Average"])
plt.title("Student Average Scores")
plt.xlabel("Students")
plt.ylabel("Average Score")
plt.show()