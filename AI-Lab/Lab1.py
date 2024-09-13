#Example
'''
for i in range(20):
    if i%3==0:
        print (i)
    if i%5==0:
     print ("Bingo")
    print ("---")
'''



#Activity 1
'''
num=int(input("Enter a Number: "))
if num%2==0:
print("Number is Even")
else:
  print("Number is Odd")
'''



#Activity 1(Repeat)
'''n=int(input("Enter a number "))
remainder=n%2
if(remainder==0):
    print(n," number is even")
else:
    print(n," number is odd")'''



#Activity 2
'''
sum=0
s=input("Enter Value")
n=int(s)
while n!=0:
    sum=sum+n
    s=input("Enter Value")
    n=int(s)
print("Sum is: ",sum)
'''



#Activity 3
'''
isprime= True
i=2
n=int(input("Enter a number: "))
while i<n:
    remainder=n%i
    if remainder==0:
        isprime=False
        break
    else:
        i=i+1
if isprime:
    print("Number is Prime")
else:
    print("Number is not Prime")
'''


#Activity 4
'''
summ=0
i=0
while i<=4:
    s=input("Enter a Number ")
    n=int(s)
    summ=summ+n
    i=i+1
print("Sum is",summ)
'''



#Activity 5   
'''
summ=0
i=0
while i<=10:
    summ=summ+i
    i=i+1

print("Sum is ",summ)
'''



#Activity 6
'''
batch=input("Enter batch: ")
program=input("Enter Program: ")
reg=input("Enter Reg: ")
print(batch,"-",program,"-",reg)
'''

    


#Activity 7
'''
import random
Min=1
Max=9
Num=random.randint(Min,Max)
Guess=None
Another=None
Try=0
Running= True
print("Alright")
while Running:
    Guess=input('Guess the Number: ')
    if int(Guess) < Num:
        print ("Wrong, too low.")
    elif int (Guess ) > Num:
        print ("Wrong, too high.")
    elif Guess.lower() == "exit":
        print ("Better luck next time.")
    elif int(Guess ) == Num:
        print ("Yes, that's the one, %s." % str(Num))
    if Try < 2:
        print ("Impressive, only %s tries." % str(Try))
    elif Try > 2 and Try < 10:
        print ("Pretty good, %s tries." % str(Try))
    else:
        print ("Bad, %s tries." % str(Try))
    
Running = False
Try += 1'''



#Lab Task 1
'''num = int(input("Enter a number "))
tmp = num
r=0
while tmp>0:
    n = tmp%10
    r= n + r*10
    tmp= int(tmp/10)
print("Reverse of",num,"will be",r)
'''




#Lab Task 2
'''
max=int(input("please enter the maximum value: "))
even_Sum=0
odd_Sum=0
for num in range(1,max+1):
    if (num%2==0):
        even_Sum=even_Sum+num
    else:
        odd_Sum=odd_Sum+num
print("The sum of Even numbers 1 to {0} = {1}".format(num,even_Sum))
print("The sum of odd numbers 1 to {0} = {1}".format(num,odd_Sum))
'''



#Lab Task 3
'''
n=int(input('Times to be displayed:'))
f=(0,1)
for i in range(2,n):
    f+=(f[i-2]+f[i-1],)
print(f)
'''




#Lab Task 4
'''
Marks = int(input("Enter Your Marks between 1 to 100: "))
if (Marks>=91):
    print("Your Grade is A")
elif Marks>=81 and Marks<91:
    print("Your Grade is B")
elif Marks>=71 and Marks<81:
    print("Your Grade is C")
elif Marks>=61 and Marks<71:
    print("Your Grade is D")
elif Marks>=50 and Marks<61:
    print("Your Grade is E")
else:
    print("Your Grade is F")
'''




#Lab Task 5
'''
fact = 1
num=int(input('Enter a number: '))

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       fact = fact*i
   print("The factorial of",num,"is",fact)
'''
       
            





