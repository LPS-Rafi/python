'''
#task 1
a = int(input())
b = int(input())
print("Sum =",a+b)
print("Product =",a*b)
print("Difference =",a-b)

#task 2
import math
r = float(input('Radius '))
ar = math.pi*r**2
cir = 2*math.pi*ar
print("Area is",ar)
print("Circumference is",cir)

#task 3
x = int(input("First number "))
y = int(input("Second number "))
if x>y:
    print("First is greater")
elif y>x:
    print("Second is greater")
else:
    print("The numbers are equal")

#task 4
w = int(input())
z = int(input())
if w>=z:
    print(w-z)
else:
    print(z-w)

#task 5
a= int(input("Enter a number: "))
if a%2 ==0 :
    print("The number is even")
else:
    print("The number is odd")

#task 6 & 7 & 8
a= int(input())
if a%2==0 and a%5==0:
    print(a,"Is a multiple of 2 & 5")
elif a%5==0:
    print(a,"Is a multiple of 5")
elif a%2==0:
    print(a,"Is a multiple of 2")
else:
    print(a,"Is not a multiple of neither 2 & 5")

#task 9
a=int(input("Enter the number of seconds- "))
h=a//3600
m=(a%3600)//60
s=a%60
print(f'Hour: {h} Minutes: {m} Seconds: {s}')

#task 10
hour=int(input("Enter work hour: "))
if 0<=hour<=168:
    if hour<=40:
        print("salary",hour*200,"Tk")
    elif hour>40:
        print("salary",8000+((hour-40)*300),"Tk")
else:
    print("Please enter a valid hour")

#task 11
s=int(input("Enter the value of S-"))
formula01=3000-(125*(s**2))
formula02=12000/(4+((s**2)/14900))
if s<100:
    print("L=",formula01)
else:
    print("L=",formula02)

#task 12
t=int(input("Time in hour(24hour format)- "))
if 0<=t<=23:
    if 4<=t<=6:
        print("Breakfast time")
    elif 12<=t<=13:
        print("Lunch time")
    elif 16<=t<=17:
        print("Snacks time")
    elif 19<=t<=20:
        print("Dinner time")
    else:
        print("Patience is a virtue")
else:
    print("Enter a valid time")

#task 13
a=int(input("Enter your mark number "))
if 90<=a<=100:
    print("I'm GPA 5")
elif 80<=a<=89:
    print("A")
elif 70<=a<=79:
    print("B")
elif 60<=a<=69:
    print("C")
elif 50<=a<=59:
    print("D")
elif 40<=a<=49:
    print("E")
elif 0<=a<40:
    print("F")
else:
    print("Please enter a valid mark number")

#task 14
a=int(input("Enter the distance in meter - "))
b=int(input("Enter the time in seconds - "))
c=a/1000
d=b/3600
k=c/d
if k<60:
    print("Velocity-",k,"Km/h")
    print("Too slow.Needs more changes.")
elif 60<=k<=90:
    print("Velocity-",k,"Km/h")
    print("Velocity is okay.The car is ready!")
else:
    print("Velocity-",k,"Km/h")
    print("Too fast.Only a few changes should suffice.")

#task 15
cg=float(input("Enter your CGPA - "))
creds=int(input("Enter your completed credits - "))
if creds>=30 and 0<=cg<=4.00:
    if 3.80<=cg<=3.89:
        print("The student is eligible for a waiver of 25 percent")
    elif 3.90<=cg<=3.94:
        print("The student is eligible for a waiver of 50 percent")
    elif 3.95<=cg<=3.99:
        print("The student is eligible for a waiver of 75 percent")
    elif cg==4.00:
        print("The student is eligible for a waiver of 100 percent")
    else:
        print("The student is not eligible for waiver because of CGPA")
else:
    print("The student is not eligible for a waiver")

#task 20
a= int(input("Enter an integer "))
if not a%2==0 and not a%5==0:
    print(a)
else:
    print("No")

#task 21
a=int(input())
if not a%2==0 or not a%5==0:
    print(a)
else:
    print("No")

#task 22
a=int(input("The number of canvases- "))
b=int(input("The number of paint tubes- "))
m=(a*120)+(b*75)
if 0<=m<=299:
    print("Previous total:",m)
    print("New total after discount:",m)
elif 300<=m<=499:
    print("Previous total:",m)
    n=m-10
    print("New total after discount:",n)
elif 500<=m<=749:
    print("Previous total:",m)
    n=m-20
    print("New total after discount:",n)
elif 750<=m<=999:
    print("Previous total:",m)
    n=m-50
    print("New total after discount:",n)
elif m>=1000:
    print("Previous total:",m)
    n=m-150
    print("New total after discount:",n)
else:
    print("Enter a valid numbers")
'''
#task23
a=float(input("Give us the temperature in fahrenheit "))
b=round(((a-32)*0.56),2)
if b<20:
    print(b,"degrees C")
    print("Winter")
elif 20<=b<=25:
    print(b,"degrees C")
    print("Autumn")
elif 25<b<30:
    print(b,"degrees C")
    print("Spring")
elif b>=30:
    print(b,"degrees C")
    print("Summer")