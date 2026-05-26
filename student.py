import pandas as pd
import matplotlib.pyplot as plt

# Sample Dataset
data = {
    "Name": ["Aman", "Riya", "Rahul", "Sneha", "Arjun"],
    "Math": [85, 78, 92, 74, 88],
    "Science": [90, 82, 89, 70, 95],
    "English": [88, 79, 85, 72, 91]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display Dataset
print("Student Dataset")
print(df)

# Average Marks
df["Average"] = (df["Math"] + df["Science"] + df["English"]) / 3

print("\nAverage Marks")
print(df[["Name", "Average"]])

# Top Performer
top_student = df[df["Average"] == df["Average"].max()]

print("\nTop Performer")
print(top_student)

# Subject-wise Average
subject_average = df[["Math", "Science", "English"]].mean()

print("\nSubject-wise Average Marks")
print(subject_average)

# Plot Graph
subject_average.plot(kind="bar")

plt.title("Average Marks by Subject")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")

plt.show()