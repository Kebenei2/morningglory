# 1.program to check whether a year is a leap year or not
year = 2017
#To get year(interger input) from the user
#year =int(input("Enter a year"))

#divided by 100 means century year (ending with 00)
#century year divided by 400 is leap year

if (year % 400 ==0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

#not divided by 100  means not a century year
#year divided by 4 is a leap year
elif (year % 4 == 0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))

#if not divided by both 400 (century year)and 4 (not century year)
#year is not leap year
else:
    print("{0} is not a leap year".format(year))



#2.Program to check whether a letter is a consonant or a vowel
#taking user input
q = input("Enter a character: ")

if(q=="A" or q=="a" or q=="E" or q=="e" or q=="I" or q=="i" or q=="O" or q=="o" or q=="U" or q=="u"):
    print(q,"is a Vowel")
else:
    print(q,"is  a Consonant")
