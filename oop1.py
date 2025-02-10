class Person:
    def __init__(self, name, age,occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

def speak(self):
    print(self.name,"is speaking")

person1 = Person("John",23,"Teacher")
print(person1.name)
print(person1.age)
print(person1.occupation)

person2 = Person("Samantha",26,"Accountant")
print(person2.name)
person2.speak()