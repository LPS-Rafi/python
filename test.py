'''
#test
a=int(input("Enter a value: "))
b=int(input("Enter a value: "))
c=int(input("Enter a value: "))
if a>b and a>c:
    print("The largest number is",a)
elif b>a and b>c:
    print("The largest number is",b)
else:
    print("The largest number is",c)

#test 2
a=int(input("Enter a value: "))
b=int(input("Enter a value: "))
c=int(input("Enter a value: "))
if a>b>c or c>b>a:
    print("The second largest is",b)
elif b>a>c or c>a>b:
    print("The second largest is",a)
elif a>c>b or b>c>a:
    print("The second largest is",c)

#task
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

b=int(input("Year "))
if (b%400==0) or (b%4==0 and b%100!=0):
    print(b,"Is a Leap Year")
else:
    print(b,"Is not a Leap Year")

a=input()
b={"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}
c={"A","B","C","D",'E','F','G','H','I','J','K','L','M','N','O','P','Q','S','T','U','V','W','X','Y','Z'}
s={"@","#","%","&","*","^"}
d=[1,2,3,4,5,6,7,8,9,0]
if (b in a) and (c in a) and (d in a) and (s in a):
    print("Strong password")
else:
    print("weak")

i=0
while i<5:
    print(i,end=" ")
    i+=1
    if i==3:
        break
else:
    print(0)

a=int(input("1= "))
b=int(input("2= "))
c=int(input("3= "))
d=int(input("4= "))
e=int(input("5= "))
avg=(a+b+c+d+e)/5
print(avg)
1
count = 0
for i in range(5):
    a = int(input("give me as: "))
    count+=a
print(count/5)
2
count=0
for i in range(5):
    a = int(input("give me : "))
    if a%2==0 and a>0:
        count+=a
print(count/5)
3
count=0
sum_=0
while count<3:
    a=int(input("give"))
    if a%2!=0 and a<0:
        count+=1
        sum_+=a
print(sum_/3)
4
a=int(input("Enter a number "))
if a>1:
    for l in range(2,a):
        if a%l==0:
            print(a,"is not a prime number")
            break
    else:            
        print(a,"is a prime")

#5
print("prime numbers are- ",end=" ")
for k in range(1,16):
    if k>1:
        for i in range(2,k):
            if k%i==0:
                break
        else:
            print(k,end=" ")
'''
"""#6
g=int(input())
for k in range(g,g-1,-1):
    print(k)"""

"""sum=0
a=int(input())
for i in range(1,a):
    if a%i==0:
        sum+=i
if sum==a:
    print(a,"is a perfect number")
else:
    print(a,"is not a perfect number")
"""
"""num=int(input())
if num%2==0:
    if num%3==0:
        if num%4==0:
            if num%2==0:
                print('"I am pro"')
        else:
            print('"Not Divisible by 4"')
    else:
        print('"Not Divisible by 3"')
else:
    print('"Not Divisible by 2"')"""

"""a=int(input())
if len(str(a))==4:
   b=a//1000
   c=a%10
   if (b+c)%2==0:
      print("Even")
   else:
      print("Odd")
else:
   print("give a proper input")"""

"""c=0
a=int(input())
for i in range(1,a+1,1):
    if a%i==0:
        c+=1
        print(i)
    else:
        continue
print(f"Total {c} divisors")

c=0
a=int(input())
b=1
while a>=b:
    if a%b==0:
        print(b)
        c+=1
    b+=1
print("Total",c,"divisors")"""
        
"""b=""
a=int(input("Enter a number "))
c=a
while a>0:
    if a%10!=a:
        b+=str(a%10)
        a//=10
    else:
        b+=str(a%10)
        a//=10
if c==int(b):
    print(c,"is Palindrome")
else:
    print(c,"is not Palindrome")"""

"""a=int(input("start"))
b=int(input("end"))
div=0
for i in range(a,b+1,1):
    if i !=0 and i != 1:
        x=0
        for j in range(1, i):
            if  i % j == 0:
                x+=1
        if x == 1:
            print(i,"is a prime number")
        else:
            print(i,"is not a prime number")"""

"""players=int(input())
c=0
div=0
while c<players:
    name=input()
    country=input()
    goles=int(input())
    c+=1
    if goles>div:
        div=goles
        output_name=name
        output_country=country
print(f"The Ballon d'Or is awarded to {name} from {country} for scoring {goles} goals this season")""" 

"""a=int(input())
c=0
while c<a:
    b=int(input("kg-"))
    c+=1
    for b in range(b,b+1,1):
        print(b*1000)"""

"""n = int(input())
s = 0
h = 1
sum = 0
print(sum,end=" ")
for i in range(1,n):
  print(h,end=" ")
  sum=h+s
  s=h
  h=sum"""

"""pod=1
a=int(input())
for i in range(1,a+1):
    pod*=i
print(pod)"""

"""a=input()
if a==a[-1:-len(a)-1:-1]:
    print(a,"is palindrome")
else:
    print(a,"is not palindrome")"""

'''sum=0
a=input()
b=""
for i in a[:len(a):]:
    if i==",":
        b=""
        continue
    elif i!=",":
        b+=str(int(i))
        if int(b)!=0 and int(b)!=1:
            x=0
            for j in range(1,int(b)):
                if  int(b) % j == 0:
                    x+=1
            if x == 1:
                sum+=int(b)
print(sum)'''

"""user = input(": ")
new = ""
for i in user :
    count = 0
    for j in user :
        if j == i:
            count += 1
    num = ord(i)
    if num >=65 and num <= 90:
        if num + count > 90:
            count = count - (90 - num)
            new += chr(64 + count)
        else:
            new += chr(num + count)
    elif num >=97 and num <= 122:
        if num + count > 122:
            count = count - (122-num)
            new += chr(96 + count)
        else:
            new += chr(num + count)
print(new)"""

'''a=input()
v=0
c=0
for i in a:
    if 65<=ord(i)<=90 or 97<=ord(i)<=122:
        if i in "aeiou":
            v+=1
        elif i in "AEIOU":
            v+=1
        else:
            c+=1
print("Vowels:",v)
print("Consonants:",c)'''

"""a=input()
for i in a:
    if 65<=ord(i)<=90:
        b=ord(i)+32
        print(chr(b),end="")
    elif 97<=ord(i)<=122:
        b=ord(i)-32
        print(chr(b),end="")
    else:
        print(i,end="")"""

'''a=input()
b=input()
for i in range(len(a)):
    if a[i]==" ":
        c1=i
        break
    else:
        continue
for j in range(-1,-len(b)-1,-1):
    if b[j]==" ":
        c2=j
        break
    else:
        continue
an=""
an+=a[0:c1:]
an+=b[c2::]
print(an)'''

"""n=int(input("N = "))
for column in range(1,n+1):
    for row in range(1,column+1):
        print("* ",end="")
    print()"""

"""n=int(input("N = "))
for column in range(1,n+1):
    for row in range(n+1,column,-1):
        print("* ",end="")
    print()"""

"""n=int(input("N = "))
for space in range(n,0,-1):
    for star in range(0,n):
        print("*",end="")
    print("7")"""

'''a=input()
big="ABCDEF"
small="abcdef"
num="0123456789"
meca=False
for i in a[2::2]:
    if i==':':
        meca=True
    elif i=="-":
        meca=True
    else:
        meca=False
else:
    if a in big or small or num:
        meca=True
    else:
        meca=False
if meca:
    print("Valid")
else:
    print("Invalid")'''

