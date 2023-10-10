# # num1 = 5
# # num2 = 10

# # if num2 > num1:
# #     print(num1)
# #     print(num2)

# # database = {
# #     'ahmad@email.com':{'name':'Ahmad', 'password':'password'},
# #     'abdul@email.com':{'name':'Abdul', 'password':'passwordx'},
# #     'umar@email.com':{'name':'Umar', 'password':'passwordx1'},
# #     }

# # email = input('Enter your email: ')

# # if email in database:
# #     password = input('Please enter your password: ')
# #     if database.get(email).get('password') == password:
# #         print('Welcome '+database.get(email).get('name'))

# # elif 2 < 1:
# #     print('Never gonna be reached')

# # elif 1 > 2:
# #     print('Invalid Email')

# # else:
# #     print('Nothing else happend')

# # Exercise
# # Check from a list of fruits if 'Banana' is included
# # If it is, print 'Yummy!' otherwise, print 'Ooops!'

# # Exercise 2
# # Q0:
# # Write a program that simulates a website
# # Users should be allowed to register
# # They should then be allowed to login
# # With their email and password
# # If their email is correct and their password
# # is also correct, the website should welcome
# # them by their names.
# # If their email is correct and their password
# # is not, notify them that their password is 
# # wrong. If thier email is wrong but their 
# # password is correct notify them that their 
# # email is wrong. If neither are correct
# # tell them their credentials are invalid

# reg_name = input("Please tell us your name: ")
# reg_email = input("Whats your email: ")
# reg_password = input("Choose a password: ")

# # Store the user in the database
# user = {'email':reg_email, 'password':reg_password, 'name':reg_name}

# login_email = input("Enter your email: ")
# login_password = input("Enter your password: ")

# if (login_email == user.get('email')) and (login_password == user.get("password")):
#     print("Hi {}, welcome to Facebook!".format(user.get("name")))
# elif (login_email == user.get('email')) and (login_password != user.get("password")):
#     print('Wrong password')
# elif (login_email != user.get('email') and login_password == user.get('password')):
#     print('Wrong email')
# else:
#     print('Invalid Credentials')
#Q1:
# Write a program that takes a number as input 
# from the user and prints "Positive" if the 
# number is greater than zero, "Negative" if 
# the number is less than zero, and "Zero" if 
# the number is equal to zero.

# number = int(input("Enter a number: "))
# if number > 0:
#     print("Positive")
# elif number < 0:
#     print("Negative")
# else:
#     print('Zero')


#Q2:
# Write a program that takes two numbers 
# as input from the user and prints the larger number.

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# if num1 < num2:
#     print(num2)
# else:
#     print(num1)

#Q3: 
# Write a program that takes a string as input 
# from the user and checks if the string starts 
# with the letter "a". If it does, print "Starts with 'a'", 
# otherwise print "Does not start with 'a'".

# name = input("Enter your name: ")
# if name.lower().startswith('a'):
#     print('Starts with "a"')
# else:
#     print('Does not start with "a"')

#Q4:
# Write a program that takes a number as input 
# from the user and checks if the number is even or odd. 
# If it is even, print "Even", otherwise print "Odd".

# num3 = int(input("Enter a number: "))
# if (num3 % 2) == 0:
#     print('Even')
# else:
#     print("Odd")

# Q5:
# Write a program that takes a grade as 
# input from the user (e.g. "A", "B", "C", "D", "F") 
# and prints "Pass" if the grade is "A", "B", or "C", 
# and "Fail" if the grade is "D" or "F".

# grade = input("Enter your Grade: ")
# pass_g = ["a", "b", "c"]
# fail_g = ["d", "f"]
# if grade.lower() in pass_g:
#     print("Pass")
# elif grade.lower() in fail_g:
#     print("Fail")

# Q6: 
# Check from a list of numbers if a float is found
# Remove it and return the result of multiplying
# it by 10.

# Pseducode:
# 1. Create a list of numbers
# 2. Check the list of numbers if there's a float
# 3. If a float is found -
#       - remove the float from the list
#       - store it somewhere
#       - multiply it by 10
#       - print the result of the multiplication

# list_of_numbers = [1, 2, 2.5, 10, 16]
# our_float = 2.5
# our_float_position = 2
# if our_float in list_of_numbers:
#     the_stored_float = list_of_numbers.pop(2)
#     result = the_stored_float * 10
#     print(result)

# Q7
# Check from a list if the number 5 is found
# if so, then remove the last item from the list and show
# the result of multiplying the removed item by 10 if the
# removed item is a number or if it can be converted to a number.

# PseudoCode:
# 1. Create a list
# 2. Check if the number 5 is found in the list
# 3. If it is found:
#       - Remove the last item from the list
#       - Store the remove item
#       - Check if the item is a number or it can be converted
#       - If that's so:
#           - Multiply the remove item by 10 and print the result

# a_list = [1, 2, 3, 4, 5, 6, 7, 8]
# if 5 in a_list:
#     stored_item = a_list.pop()
#     if type(stored_item) == int or stored_item.is_digit():
#         print(int(stored_item) * 10)


# Pseudocode:
# 1. Create a list
# 2. Check if the number 5 is in the list
# 3. If the number 5 is found:
#       - Remove the last item from the list
#       - Store the removed item
#       - Check if the stored item is a number or it can be converted to a number
#       - Show the result of multiplying the stored item by 10

# our_list = ["Alameen", 3, 5, "1.4", "Abdulateef", 16]
# if 5 in our_list:
#     stored_item = our_list.pop()
#     if type(stored_item) == int or stored_item.isdigit():
#         print(int(stored_item)*10)


# ANSWER THE FOLLOWING QUESTIONS: In each case
# start with a pseudocode.

# Q8. Write a Python program that checks if a given year
#  is a leap year or not. Use conditional statements 
# to determine whether the year is divisible by 4 
# (but not divisible by 100 unless it's also divisible by 400).

# Q9. Create a Python function that takes two integers as 
# input and returns the larger of the two.

# Q10. Write a Python function that calculates the factorial 
# of a given non-negative integer using recursion
#  (a function calling itself) and conditional statements.

# Q11. Develop a Python program that converts a given 
# temperature in Celsius to Fahrenheit. 
# Use conditional statements to perform the conversion based on 
# the user's choice.

# Q12. Create a Python function that checks if a given string 
# is a palindrome (reads the same forwards and backwards).

#num=1
#while num <=10:
 #   print(num)
#num +=2

def lists_to_dict(list1, list2):
    if len(list1) != len(list2):
        raise ValueError()

    result_dict = {}
    for i in range(len(list1)):
        result_dict[list1[i]] = list2[i]

    return result_dict

list1 = ["name", "age", "height"]
list2 = ["Ahmad Sani", 15, 1.6]
result = lists_to_dict(list1, list2)
print(result)

def string_taken(input_string):
    character_count=len(input_string)
    combinations=["ahmsa","saanahm","amsan"]

    result_dict={
        "word":input_string,
        "characters":character_count,
        "combination":combinations

    }

    return result_dict

input_string="ahmad sani"
result=string_taken (input_string)
print(result)