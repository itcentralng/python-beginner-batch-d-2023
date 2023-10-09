#reg_email=input("Enter your email" )
#reg_password=input("Enter your password" )
#reg_name=input("Enter your name" )

#user={'email':reg_email, 'password':reg_password,'name': reg_name}


#login_email=input("Enter your email")
#login_password=input("Enter your password")

#if (login_email == user.get("email")) and (login_password == user.get("password")):
 #   print("Hi {}, welcome to Facebook!".format(user.get("name")))
#elif login_email == user.get("email") and login_password != user.get("password"):
 #   print("password not correct")
#elif login_email != user.get("email") and login_password == user.get("password"):
 #   print("email is not correct")
#else:
 #   print("Credentials are invalid")


  

  







#number=(input("Enter a number:"))
#if  number > 0:
 #   print("positive")
#if number < 0:
 #   print("negative")
#if number == 0:
 #   print("zero")


#num1=input("Enter number 1: "))
#num2=(input("Enter number 2: "))

#if num1 > num2:
 #   print("the larger number is: {num1}")
#elif num2 > num1:
 #   print("the larger number is: {num2}")
#else:
 #   print("both numbers are equal")

#input_string = "alameen"
#input("Enter a string")

#if input_string.startswith("a"):
 #   print("start with 'a'")
#else:
#    print("doesn't starts with'a'" )





#num=int(input("Enter a number:"))

#if num %2==0:
 #   print("Even")
#else:
#    print("Odd")



#grades=input("Enter your grade(A,B,C,D,F):")

#if grades in["A","B","C"]:
 #   print("pass")
#elif grades in["D","F"]:
 #   print("Fail")
#else:
 #   print("invalid")

#numbers=[1,2,3,4,5,6,7,8,9,10]

#for number in numbers:
 #   print(number)

#for number in numbers:
 #    if number %2==1:
  #       print(number)


#for number in numbers:
#    if number == 3:


# for number in range(2,16):
#   if number % 3 == 0 and number % 5 == 0:
#     print('FizzBuzz')
#   elif number %3==0:
#     print("Fizz")
#   elif number %5==0:
#     print("Buzz") 
# else:
#   print(number)


#name="ahmad"
#vowels=['a','e','i','o','u']
#for char in name:
 # if char.lower in vowels:
  #  print(char)

user_scores={}

states_and_capitals ={
    
    "Abuja": "Abuja",
    "Kaduna": "Kaduna",
    "Borno": "Maiduguri",

}

def start_game (username):
    score=0
    total_questions= len(states_and_capitals)

    states= list(states_and_capitals.keys())
    

    for state in states:
        capital = states_and_capitals[state]
        user_answer=input("whats the capital of{state}?").strip()
        if user_answer.lower()== capital.lower():
            print("correct! you earned 5 points.")
            scores += 5
        else:
            print("Wrong! The correct answer is {capital}. 3 points")
            score -=3
            print ("your current score: {score} points")




   
   





