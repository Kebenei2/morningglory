#Blocks of codes that perfoms a task


#Built-in function/Standard Library Function
y =max(67,43,89,90,23)
print("The maximum value is",y)

x =min(67,43,89,90,23)
print("The minimum value is",x)

#User-defined Function:
def name():
    print("Ian")


name() #Calling a function

def multiply():
    x = 2
    y = 8
    print(x * y)
multiply()

#Parameter/Variable and argument
def add(a , b):
    print(a + b)
    add(6,8)

def employee(name,gender,position,salary,age):
    print(name,gender,position,salary,age)

employee("John","Male","CEO","560000","56")
employee("Peter","Male","Managing Director","530000","50")




#Write a programme that displays details of 5 students.
#Use a user-defined function with the help  of a parameter and argument
#Fullname,age,course,gender

def student(fullname,age,course,gender):
    print(fullname,age,course,gender)

student(fullname=Ian Kebenei,age=17,course="Programming",gender="Male")
student(fullname=Patience Nyambura,age=17,course="MIT",gender="Female")
student(fullname=Kassim Abbuta,age=17,course="Data Science",gender="Male")
student(fullname=Damaris Kimani,age=18,course="Data Science",gender="Female")
student(fullname=Samantha Nduti,age=18,course="MIT",gender="Female")







