import numpy as np
marks = np.array([[70, 80, 90],
[60, 75, 85],
[88, 92, 79],
[55, 65, 70]])
print("Shape:",marks.shape)
print("DataType:",marks.dtype)
print("Size:",marks.size)

print(marks[:2,-1])
student_avg = marks.mean(axis=1)
subject_avg = marks.mean(axis=0)
print("student_avg:",np.round(student_avg,2))
print("subject_avg:",np.round(subject_avg,2))

grace_marks = marks + 5
print("Grace_marks:",grace_marks)

weights = [0.3, 0.3, 0.4]
weighted_scores = np.dot(marks,weights)
print("weighted_scores:",weighted_scores)

arrange = np.arange(12).reshape(3,4)
print("\nreshape array 3*4:\n",arrange)

import pandas as pd

data = """id,name,department,salary,city
1,Arun,Sales,30000,Chennai
2,Priya,HR,45000,Chennai
3,Rahul,IT,60000,Bangalore
4,Divya,IT,75000,Chennai
5,Karthik,Finance,90000,Mumbai
6,Meena,Sales,52000,Bangalore
7,Suresh,IT,68000,Chennai
8,Anitha,HR,48000,Mumbai
"""

with open("employees.csv", "w") as file:
    file.write(data)
df = pd.read_csv("employees.csv")

print(df)
print(df.head())
df.info()
print(df.describe())
print(df["name"])
print(df[["name", "salary"]])
chennai = df.loc[df["city"] == "Chennai", "name"]
print("Chennai:", ", ".join(chennai))
print(df.iloc[0:3, 1:3])
high_salary = df[df["salary"] > 50000]

print("Salary above 50000:", len(high_salary), "employees")
it_employees = df[df["department"] == "IT"]
print("IT department:", ", ".join(it_employees["name"]))