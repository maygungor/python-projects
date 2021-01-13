import random 
num = random.randint(1,10)
your_try = 0
score = 100
print("You have 5 try")

while your_try<5:
    number = int(input("Enter a number: "))
    your_try+= 1  
    if num > number:
         print("Your number is lower")
         score -= 20
         
    elif number>num:
         print("Your number is bigger")
         score -= 20
         
    elif number == num:
         print(f"Congratulations. You are correct . Your score is  {score} and you knew it your {your_try}.try")
         break #doğru olduğunda döngüyü durduracak

if number != num:
     print("I'am sorry. ")