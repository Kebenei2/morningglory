


def prime(number):

    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return False
            else:
                return True
number = int(input("Enter a number: "))
if prime(number):
    print("It is a prime number")
else:
    print("It is not a prime number")








