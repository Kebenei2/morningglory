
#parent/super/base class
class animal:
    def speak(self):
        print("Animal is speaking")

#child class/sub class/derived class
class dog (animal):
    def speak(self):
        print("Dog is speaking")
    def bark(self):
        print("Dog is barking")


class cat(dog):
    def meow(self):
        print("Cat is meowing")

a = animal()
d = dog()

c = cat()