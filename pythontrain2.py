# with open("student.txt","r")as file:
#     read=file.read()
#     print(read)


# import csv
# with open("student.csv","w")as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name","Age","Marks"])
#     writer.writerow(["Joe","26","Pass"])

# import csv
# with open("student.csv","r",newline="")as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

'''import json

student = {
    "name": "Ravi",
    "age": 20,
    "skills": ["Python", "SQL"]
}

with open("studenthj.json", "w") as file:
    json.dump(student, file, indent=4)'''

'''import json

with open("student.json", "r") as file:
    data = json.load(file)

print(data["name"])
print(data["skills"])'''

# from pathlib import Path
# file_path = Path("joe.txt")
# # print(file_path.name)
# # file_path.write_text("Name=joe \nCourse:python",encoding = "utf-8")
# # print("sucessfully done")
# content = file_path.read_text(encoding="utf-8")
# print(content)
# from fastapi import FastAPI

# app = FastAPI()

# students = [
#     {"id": 1, "name": "Mani","book":"maths"},
#     {"id": 2, "name": "Daya","book":"science"}
# ]

# @app.get("/home")
# def home():
#     return {"message": "Hello World"}

# @app.get("/students")
# def get_students():
#     return students
# @app.post("/students")
# def create_student(student: dict):


#     students.append(student)


#     return{
#         "message":"Student created",
#         "student":student
#     }


# @app.put("/students/{student_id}")


# def update_student(student_id:int,student:dict):


#     for item in students:


#         if item["id"]==student_id:


#             item["name"]=student["name"]


#             return{
#                 "message":"Student Updated",
#                 "Student":"item"
#             }


#         return{
#             "message":"Student not found"
#         }




# @app.delete("/students/{student_id}")   


# def delete_student(student_id:int):


#     for item in students:


#         if item["id"]==student_id:


#             students.remove(item)


#             return{
#                 "message":"Student deleted"
#                  }


#         return{
#             "message":"Student not found"
#         }
from fastapi import FastAPI
app = FastAPI()
# students = [{"id" : 1,"name" : "joe"},
#             {"id" : 2,"name" : "jack"},
#             {"id" : 3,"name" : "johnny"}
#             ]
# @app.get("/home")
# def home():
#     return{"this is your homepage response"}
# @app.get("/students")
# def get_students():
#     return(students)

# @app.post("/students")
# def joecreate_students(student: dict):
#     students.append(student)
#     return{
#         "id":4,"name":"RAVI"
#     }
# def update_student(student_id:int,student:dict):


#     for item in students:


#         if item["id"]==student_id:


#             item["name"]=student["name"]


#             return{
#                 "message":"Student Updated",
#                 "Student":"item"
#             }
#         return {
#         "message": "Student not found"
#     }
# @app.delete("/students/{student_id}")
# def delete_student(student_id:int):
#     for item in students:
#         if item["id"] ==student_id:
#             students.remove(item)
#             return{
#                 "message":"student deleted"
#             }
#         return{
#             "message":"student not found"
#         }
# @app.get("/user/user_id")
# def user_profile(user_id:int):
#     if (user_id == 1):
#         return{
#             "name" : "joe",
#             "job" : "dev",
#             "company":"yoho"


#         }
#     else:
#         return{
#             "name":"john" + str(user_id),
#             "job" : "Test",
#             "company":"Tata"
#         }

# import numpy as np

# a = np.array([1,2,3])
# b=np.array([2,4,6])
# print(np.dot(a,b))
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