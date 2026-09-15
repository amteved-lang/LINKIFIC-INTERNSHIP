import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Task6/students.csv")

print("Dataset:")
print(df)

print("\nDataset Shape:", df.shape)

df["Total_Marks"] = df["Python"] + df["Math"] + df["Science"]
df["Average_Marks"] = df["Total_Marks"] / 3

plt.figure(figsize=(10, 6))
plt.bar(df["Name"], df["Average_Marks"])
plt.title("Average Marks of Students")
plt.xlabel("Student")
plt.ylabel("Average Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(df["Name"], df["Average_Marks"], marker="o")
plt.title("Student Average Marks")
plt.xlabel("Student")
plt.ylabel("Average Marks")
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(df["Average_Marks"], bins=5, edgecolor="black")
plt.title("Distribution of Student Average Marks")
plt.xlabel("Average Marks")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.show()

city_counts = df["City"].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(city_counts.values, labels=city_counts.index, autopct="%1.1f%%", startangle=90)
plt.title("Students by City")
plt.show()

print("\n===== OBSERVATIONS =====")

top_student = df.loc[df["Average_Marks"].idxmax()]
lowest_student = df.loc[df["Average_Marks"].idxmin()]

print("1. The student with the highest average marks is", top_student["Name"],
      "with an average of", round(top_student["Average_Marks"], 2))

print("2. The student with the lowest average marks is", lowest_student["Name"],
      "with an average of", round(lowest_student["Average_Marks"], 2))

print("3. The overall class average is",
      round(df["Average_Marks"].mean(), 2))

print("4. The highest average marks are in",
      df["Average_Marks"].max(),
      "and the lowest average marks are",
      df["Average_Marks"].min())

print("5. The city with the highest number of students is",
      city_counts.idxmax(),
      "with", city_counts.max(), "students.")