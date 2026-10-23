import numpy as np
"""marks = np.array([[70, 80, 90],
[60, 75, 85],
[88, 92, 79],
[55, 65, 70]])
print("shape:",marks.shape)
print("Dtype:",marks.dtype)
print("size:",marks.size)
print("slicing:",marks[:2,2])

student_avg = marks.mean(axis=1)
print("student_avg:",np.round(student_avg,2))
subject_avg = marks.mean(axis=0)
print("subject_avg:",np.round(subject_avg,2))
Broadcasting = marks + 5
print("\nGrace_marks:\n",Broadcasting)
weights = [0.3, 0.3, 0.4]
weighted_scores = np.dot(marks,weights)
print("weighted_scores:",weighted_scores)
arr =np.arange(12).reshape(3,4)
print("\narange & reshaping:\n",arr)"""

import pandas as pd

data = """id,name,department,salary,city
1,Arun,Sales,30000,Chennai
2,Priya,HR,45000,Chennai
3,Rahul,IT,60000,Bangalore
4,Divya,IT,75000,Chennai
5,Karthik,Finance,90000,Mumbai
6,Meena,Sales,52000,Bangalore
7,Suresh,IT,68000,Chennai
8,Anitha,HR,48000,Mumbai"""
with open("employees.csv", "w") as file:
    file.write(data)
df = pd.read_csv("employees.csv")

# print(df)
# print(df.head())
# df.info()
# print(df.describe())
print(df["name"])
print(df[["name","salary"]])
chennai_employees=df.loc[df["city"]== "Chennai","name"]
print("chennai_employees:",",".join(chennai_employees))
print(df.iloc[0:3, 1:3])


high_salary = df[df["salary"]>50000]
print(high_salary)
print("salary above 50000:",len(high_salary),"employees")

IT_dept = df[df["department"] == "IT" ]

print("IT department:",",".join(IT_dept["name"]))

arr= np.arange(1,25)
reshaped = arr.reshape(2,3,4)
print(reshaped)
print("overall_shape:",reshaped.shape)

for i, slice_arr in enumerate(reshaped):
    print(f"slice {i} shape:",slice_arr.shape)