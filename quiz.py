#number = int(input("Choose a number: " ))
#if number %2==0:
    #print(str(number)+" Even number")
#else:
    #print(str(number)+" odd number")
#age = int(input("Enter your age : "))
#if age < 12:
    #print("You are a child ")
#elif age < 20:
    #print("You are a teeneger")
#elif age < 60:
    #print("you are an adult")
#else:
    #print("You are a Senior")
#Exercise 3: Age Group Classifier
#Exercise 4: Grading System
#Ask the user to enter their exam score and use if-elif-else to output:
#score= int(input("Enter your exam score: "))
#if score >= 90:
    #print("Well done you're one of the elites \n you got an A")
#elif score >= 80:
    #print("Good job you're close to the top \n you got a B")
#elif score >= 70:
    #print("you did well push for more next semester \n you got a C")
#elif score>= 60:
    #print("You did okay you can do better \n you got a D")
#elif score< 60:
    #print ("you need to work harder you're just lazy \n you got F")




#Excersie : Write a program that asks the user to enter the marks of 8 units and then calculate the total marks and average.
greet=input("Are you ready to upload your marks ? (yes/no): ")
if greet=="yes":
    marks1=int(input("Enter your marks for Operating System: "))
    marks2=int(input("Enter your marks for Computer Maths: "))
    marks3=int(input("Enter your marks for Computer Maintenance: "))
    marks4=int(input("Enter your marks for Java Programming: "))
    marks5=int(input("Enter your marks for C++: "))
    marks6=int(input("Enter your marks for Word Application: "))
    marks7=int(input("Enter your marks for Computing project: "))
    marks8=int(input("Enter your marks for Industrial Attachment: "))
else: 
    print("You are not ready to upload your marks")
total_marks=marks1+marks2+marks3+marks4+marks5+marks6+marks7+marks8
print("Your total marks are: " + str(total_marks))
if total_marks >= 500:
    print("Congratulations you have passed")
elif total_marks >= 400:
    print("Pull up your socks and work harder next time")
elif total_marks <= 300:
    print("You are a fraud and you should do better!! ")
     