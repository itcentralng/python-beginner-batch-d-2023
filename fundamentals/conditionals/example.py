num1 = 5
num2 = 10

if num2 > num1:
    print(num1)
    print(num2)

database = {
    'ahmad@email.com':{'name':'Ahmad', 'password':'password'},
    'abdul@email.com':{'name':'Abdul', 'password':'passwordx'},
    'umar@email.com':{'name':'Umar', 'password':'passwordx1'},
    }

email = input('Enter your email: ')

if email in database:
    password = input('Please enter your password: ')
    if database.get(email).get('password') == password:
        print('Welcome '+database.get(email).get('name'))

elif 2 < 1:
    print('Never gonna be reached')

elif 1 > 2:
    print('Invalid Email')

else:
    print('Nothing else happend')

# Exercise
# Check from a list of fruits if 'Banana' is included
# If it is, print 'Yummy!' otherwise, print 'Ooops!'

# Exercise 2
# Q0:
# Write a program that simulates a website
# Users should be allowed to register
# They should then be allowed to login
# With their email and password
# If their email is correct and their password
# is also correct, the website should welcome
# them by their names.
# If their email is correct and their password
# is not, notify them that their password is 
# wrong. If thier email is wrong but their 
# password is correct notify them that their 
# email is wrong. If neither are correct
# tell them their credentials are invalid
#Q1:
# Write a program that takes a number as input 
# from the user and prints "Positive" if the 
# number is greater than zero, "Negative" if 
# the number is less than zero, and "Zero" if 
# the number is equal to zero.
#Q2:
# Write a program that takes two numbers 
# as input from the user and prints the larger number.
#Q3: 
# Write a program that takes a string as input 
# from the user and checks if the string starts 
# with the letter "a". If it does, print "Starts with 'a'", 
# otherwise print "Does not start with 'a'".
#Q4:
# Write a program that takes a number as input 
# from the user and checks if the number is even or odd. 
# If it is even, print "Even", otherwise print "Odd".
# Q5:
# Write a program that takes a grade as 
# input from the user (e.g. "A", "B", "C", "D", "F") 
# and prints "Pass" if the grade is "A", "B", or "C", 
# and "Fail" if the grade is "D" or "F".