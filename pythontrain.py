# # # # # # # a = "joe"
# # # # # # # b = 9
# # # # # # # print(type(a))
# # # # # # # print(type(b))

# # # # # # # #control flow
# # # # # # # marks = 50
# # # # # # # if marks >= 50:
# # # # # # #  print("you have scored 1st class")
# # # # # # # elif marks >= 75:
# # # # # # #  print("you have scored distinction")
# # # # # # # else :
# # # # # # #  print("you fail")


# # # # # # n = 8
# # # # # # for i in range(5,n):
# # # # # #     print(i)

# # # # # q  = ["joe","bharath","anna"]
# # # # # for i in range (len(q)):
# # # # #  print(q[i])

# # # # cou = 5
# # # # while cou < 9:
# # # #     cou = cou + 1
# # # #     print("joe")

# # # #try,except, finally
# # # try:
# # #     num = int(input("enter the number :"))
# # #     c=45/num
# # # except ZeroDivisionError:
# # #     print("dont use zero")
# # # except ValueError:
# # #     print("error number")
# # # finally:
# # #     print("im working finally")

# # city = "joe"
# # print(city.upper())

# # student = {"name" : "joe", "age": 3}
# # print(student["age"])

# # point = (10, 20)
# # print(point[1])

# # for i in range(1,10):
# #     print(i)

# # count = 1
# # while count<=5:
# #     print(count)
# #     count += 2

# # for i in range(1,6):
# #     if i ==2:
# #         continue
# #     if i ==5:
# #         break
# #     print (i)

# # students = ["Arun", "Priya", "Kumar"]

# # for name in students:
# #     print(name)

# # def joe(a,b):
# #     return a + b
# # bharath = joe(10,30)
# # print(bharath)

# # def surya(a,b):
# #     return a/b
# # joe = surya(40,4)
# # print(joe)

# # def joe(*args):
# #     return sum(args)
# # print(joe(10,20))
# # print(joe(10,100,100))
# # print(joe(100,100))

# # def joe(**kwargs):
# #      print(kwargs)
# # joe(name ="mj",age="56")
# # joe = lambda i : i*i
# # print(joe(6))
# # numbers = [1,2,3,4,9,18,18,27,26]
# # even_number= [k for k in numbers if k % 2 !=0]
# # print(even_number)
# # numbers = (1,4,5,6,7)
# # def joe(n):
# #     return n*4
# # bharath = list(map(joe,numbers))
# # print(bharath)

# # numbers = (1,4,5,6,7)
# # def joe(n):
# #     return n%4==0
# # bharath = list(filter(joe,numbers))
# # print(bharath)

# class chess:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def joiners(self):
#         print(self.name,self.age)
# s1 = chess("joe", 16)
# s2 = chess("mani",101)
# s1.joiners()
# s2.joiners()

# class marks:
#     def __init__(self,maths,science):
#         self.maths = maths
#         self.science = science
#     def board(self):
#         print(self.maths,self.science)

# m1 = marks("maths puli",99)
# m1.board()

# class joe:
#     def play(self):
#         print("joe is playing")
# class rohit(joe):
#     def eat(self):
#         print("joe is eating")
# jothi = rohit()
# jothi.play()
# jothi.eat()
# class game:
#     def cricketing(self):
#         print("joe is playing")
# class cricket(game):
#     def cricketing(self):
#         print("joe is on 85")
# class volleyball(game):
#     def cricketing(self):
#         print("joe is on 100")
# joe = cricket()
# Jothi = volleyball()
# bh = game()

# joe.cricketing()
# Jothi.cricketing()
# bh.cricketing()

# class student:
#     def __init__(self,name):
#         self.name = name
# class tenth(student):
#     def __init__(self, name,marks):
#         super().__init__(name)
#         self.marks = marks
# joe = tenth("joe",100)
# print(joe.name)
# print(joe.marks)

# def ATM(money):
#     if money <100:
#         raise ValueError("money cannot be -ve")
#     print("your money here:", money)
# ATM(100)
class InsufficientBalanceError(Exception):
    pass


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError(
            "Insufficient balance"
        )

    return balance - amount

try:
    remaining = withdraw(500, 800)
    print(remaining)

except InsufficientBalanceError as e :
    print(e)